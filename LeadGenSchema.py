from pydantic import BaseModel


class ValueSchema(BaseModel):
    ad_id: str
    form_id: str
    leadgen_id: str
    create_time: int
    page_id: str
    adgroup_id: str

class LeadGenSchema(BaseModel):
    field: str
    value: ValueSchema