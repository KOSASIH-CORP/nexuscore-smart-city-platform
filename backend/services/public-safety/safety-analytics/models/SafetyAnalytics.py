from pydantic import BaseModel

class SafetyAnalytics(BaseModel):
    id: int
    location: str
    crime_rate: float
    safety_index: float
