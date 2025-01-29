from pydantic import BaseModel
from typing import List, Optional


class LeadValue(BaseModel):
    adgroup_id: Optional[str] = None
    ad_id: Optional[str] = None
    created_time: int
    leadgen_id: str
    page_id: str
    form_id: str

class LeadChange(BaseModel):
    field: str
    value: LeadValue

class LeadEntry(BaseModel):
    id: str
    time: int
    changes: List[LeadChange]

class LeadGenSchema(BaseModel):
    object: str
    entry: List[LeadEntry]