import json
import os
from pathlib import Path
from urllib.parse import quote

import geopandas
import httpx
import re 

from cdrc.common import get_projection_id, return_properties
from cdrc.schemas import FeatureSearchByCog


class CDRClient:
    def __init__(self, token, output_dir="."):
        # self.cog_url = "https://s3.amazonaws.com/public.cdr.land"
        self.cog_url = "http://192.168.1.85:9000/public.cdr.land"
        self.projection_id = ""
        self.output_dir = output_dir
        # self.base_url = "https://api.cdr.land/v1"
        self.base_url = "http://192.168.1.85:8333/v1"
        self.headers = {"accept": "application/json", "Authorization": f"Bearer {token}"}
        self.client = httpx.Client(timeout=None)

    def features_search(self, cog_id, feature_types, system_versions, validated):
        payload = {
            "feature_types": feature_types,
            "system_versions": system_versions,
            "search_text": "",
            "validated": validated,
            "legend_ids": [],
            "georeferenced_data": True,
            "page": 0,
            "size": 20,
        }
        validated_payload = FeatureSearchByCog(**payload).model_dump()
        validated_payload["feature_types"] = [ft.value for ft in validated_payload["feature_types"]]
        all_data = []
        while True:
            print(f"collecting records from cdr:  current amount {len(all_data)} records")
            response = self.client.post(
                f"{self.base_url}/features/{cog_id}", json=validated_payload, headers=self.headers
            )
            if response.status_code != 200:
                print(response.text)
                print("There was an error connecting to the cdr.")
                break
            data = response.json()
            if not data:
                print("Finished collecting features")
                break

            all_data.extend(data)
            validated_payload["page"] = validated_payload["page"] + 1

        return all_data

    def legend_builder(self, legend_features):
        system = legend_features.get("system")
        system_version = legend_features.get("system_version")
        label = legend_features.get("label")
        abbreviation = legend_features.get("abbreviation")
        category = legend_features.get("category")
        legend_contour_feature = {
            "type": "Feature",
            "geometry": legend_features.get("px_geojson"),
            "properties": {
                "legend_id": legend_features.get("legend_id", ""),
                "category": category,
                "label": label,
                "abbreviation": abbreviation,
                "description": legend_features.get("description"),
                "validated": legend_features.get("validated"),
                "system": system,
                "system_version": system_version,
                "model_id": legend_features.get("model_id"),
                "confidence": legend_features.get("confidence"),
                "map_unit_age_text": legend_features.get("map_unit_age_text"),
                "map_unit_lithology": legend_features.get("map_unit_lithology"),
                "map_unit_b_age": legend_features.get("map_unit_b_age"),
                "map_unit_t_age": legend_features.get("map_unit_t_age"),
            },
        }

        obj = {"type": "FeatureCollection", "features": [legend_contour_feature]}
        thing = label[:10] + "__" + abbreviation[:10]
        thing = thing.strip().lower()
        if thing =="__":
            thing = legend_features.get("description","")[:10]
            thing = re.sub(r'\s+', '', thing).lower()

        with open(
            os.path.join(
                self.output_dir + f"/{legend_features.get('cog_id')}/pixel",
                f"{system}__{system_version}__{thing}_{category}_legend_contour.geojson",
            ),
            "w",
        ) as out:
            out.write(json.dumps(obj, indent=2))

    def set_latest_projection_id(self, feature):
        cdr_projection_id = get_projection_id(feature)
        if self.projection_id != cdr_projection_id:
            self.projection_id = cdr_projection_id

    def legend_feature_builder(self, legend_features):
        """
        For each feature associated with a legend item build the Feature obj to save as geojson or geopackage.
        """
        system = legend_features.get("system")
        system_version = legend_features.get("system_version")
        label = legend_features.get("label","")
        abbreviation = legend_features.get("abbreviation","")
        category = legend_features.get("category")
        description = legend_features.get("description","")

        pixel_features = []
        geom_features = []
        print(f"Starting process for {category} extractions. {len(legend_features[f'{category}_extractions'])}")

        for result in legend_features[f"{category}_extractions"]:
            self.set_latest_projection_id(result)
            feature = {
                "type": "Feature",
                "geometry": result["px_geojson"],
                "properties": return_properties(legend_features, result),
            }
            pixel_features.append(feature)
            if result.get("projected_feature"):
                geom_feature = {
                    "type": "Feature",
                    "geometry": result.get("projected_feature")[0].get("projected_geojson"),
                    "properties": return_properties(legend_features, result),
                }
                geom_features.append(geom_feature)
            else:
                print("Feature is not georeferenced in the cdr")

        px_obj = {"type": "FeatureCollection", "features": pixel_features}
        thing = label[:10] + "__" + abbreviation[:10]
        thing = thing.strip().lower()

        if thing =="__":
            thing = description[:10]
            thing = re.sub(r'\s+', '', thing).lower()

        with open(
            os.path.join(
                self.output_dir + f"/{legend_features.get('cog_id')}/pixel",
                f"{system}__{system_version}__{thing}_{category}_features.geojson",
            ),
            "w",
        ) as out:
            out.write(json.dumps(px_obj, indent=2))

        if geom_features:
            geom_obj = {"type": "FeatureCollection", "features": geom_features}

            df = geopandas.GeoDataFrame.from_features(geom_obj)
            # always 4326 from cdr
            vector = df.set_crs("EPSG:4326", allow_override=True)
            vector.to_file(
                os.path.join(
                    self.output_dir + f"/{legend_features.get('cog_id')}/projected",
                    f"{system}__{system_version}__{thing}_{category}_features.gpkg",
                ),
                driver="GPKG",
            )

    def build_geopackage(self, cog_id, feature_types, system_versions, validated):
        print("Starting to build geopackage")

        legend_items = self.features_search(cog_id, feature_types, system_versions, validated)
        print("Finished getting legend items and features")
        if not legend_items:
            print("CDR didn't return any features for this search returned")
            return
        Path(self.output_dir + "/" + cog_id + "/pixel").mkdir(parents=True, exist_ok=True)
        Path(self.output_dir + "/" + cog_id + "/projected").mkdir(parents=True, exist_ok=True)

        for legend_item in legend_items:
            self.legend_builder(legend_item)
            
            self.legend_feature_builder(legend_item)

        print("Downloading cog and projected cog")
        self.download_projected_and_pixel_cog(cog_id=cog_id)

    def download_cog(self, cog_id):
        r = httpx.get(f"{self.cog_url}/cogs/{cog_id}.cog.tif")
        open(f"{self.output_dir}/{cog_id}/pixel/{cog_id}.cog.tif", "wb").write(r.content)

    def download_projected_and_pixel_cog(self, cog_id):
        self.download_cog(cog_id=cog_id)
        if self.projection_id:
            path = f"/maps/cog/projection/{self.projection_id}"

            encoded_url_path = quote(path)

            resp = self.client.get(self.base_url + encoded_url_path, headers=self.headers)
            if resp.status_code == 403 or resp.status_code == 404:
                print("Unable to find projection.")
                return
            if resp.status_code == 200:
                data = resp.json()
                if data.get("download_url"):
                    url_ = self.cog_url+quote(f"/test/cogs/{cog_id}/{data.get("system")}/{data.get("system_version")}/{self.projection_id}")
                    r = httpx.get(url_)
                    if r.status_code !=200:
                        print(r.status_code)
                        return
                    open(f"{self.output_dir}/{cog_id}/projected/{self.projection_id}", "wb").write(r.content)
