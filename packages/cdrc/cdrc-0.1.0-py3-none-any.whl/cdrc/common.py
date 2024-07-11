import hashlib


def get_projection_id(feature):
    if feature.get("projected_feature"):
        if len(feature.get("projected_feature", [])) > 0:
            proj_id = feature.get("projected_feature", [])[0].get("cdr_projection_id")
            return proj_id
    return ""


def return_properties(legend_features, feature):
    return {
        "px_bbox": feature.get("px_bbox", []),
        "legend_id": legend_features.get("legend_id", []),
        "label": legend_features.get("label"),
        "abbreviation": legend_features.get("abbreviation"),
        "description": legend_features.get("description", ""),
        "system": legend_features.get("system"),
        "system_version": legend_features.get("system_version"),
        "model_id": feature.get("model_id"),
        "confidence": feature.get("confidence"),
        "map_unit_age_text": legend_features.get("map_unit_age_text"),
        "map_unit_lithology": legend_features.get("map_unit_lithology"),
        "map_unit_b_age": legend_features.get("map_unit_b_age"),
        "map_unit_t_age": legend_features.get("map_unit_t_age"),
        "projection_id": get_projection_id(feature),
    }


def hash_string(input_string, algorithm="sha256"):
    hash_object = hashlib.new(algorithm)
    encoded_string = input_string.encode("utf-8")
    hash_object.update(encoded_string)
    return hash_object.hexdigest()
