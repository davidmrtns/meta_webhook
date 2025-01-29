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

'''
{'object': 'page', 'entry': [{'id': '266732166692625', 'time': 1738175166, 'changes': [{'field': 'leadgen', 'value': {'adgroup_id': None, 'ad_id': None, 'created_time': 1738175164, 'leadgen_id': '953494233552595', 'page_id': '266732166692625', 'form_id': '959174276185865'}}]}]}
'''