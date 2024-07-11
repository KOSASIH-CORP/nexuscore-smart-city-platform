from pydantic import BaseModel

class EmergencyResponse(BaseModel):
    id: int
    incident_type: str
    location: str
    response_time: str
    status: str
