from pydantic import BaseModel

class CrimeReport(BaseModel):
    id: int
    crime_type: str
    location: str
    date: str
    status: str
