from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class FeatureTypes(Enum):
    LEGEND_ITEM = "legend_item"
    POLYGON = "polygon"
    LINE = "line"
    POINT = "point"
    AREA_EXTRACTION = "area_extraction"


class FeatureSearchByCog(BaseModel):
    feature_types: List[FeatureTypes] = Field(default_factory=list, description="List of features to return")
    system_versions: Optional[List[tuple]] = Field(
        default_factory=list, description="List of system and system version pairs"
    )
    search_text: str = Field(default="", description="String text to search for in legend descriptions")
    validated: Optional[bool] = None
    legend_ids: Optional[List[str]] = Field(
        default_factory=list, description="List of legend ids to filter on if known"
    )
    georeferenced_data: bool = Field(default=False, description="Return georeferenced values")
    page: int = Field(description="Page", default=0)
    size: int = Field(description="Number of results", default=10)
