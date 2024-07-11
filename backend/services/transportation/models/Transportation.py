from pydantic import BaseModel

class Transportation(BaseModel):
    id: int
    vehicle_type: str
    route: str
    schedule: str
    status: str
