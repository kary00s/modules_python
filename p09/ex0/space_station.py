from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)

def main(): 
    try:
        valid = SpaceStation(
            station_id="SS-001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 1, 1, 9, 0, 0),
            is_operational=True,
            notes="All systems nominal.",
        )

        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        print(f"Station ID: {valid.station_id}")
        print(f"Name: {valid.name}") 
        print(f"Crew Size: {valid.crew_size} people") 
        print(f"Power Level: {valid.power_level}%") 
        print(f"Oxygen Level: {valid.oxygen_level}%") 
        print(f"Last Maintenance: {valid.last_maintenance}") 
        if valid.is_operational is True:
            stats = "Operational" 
        else:
            stats = "Non-operational"
        print(f"Status: {stats}") 
        print(f"Notes: {valid.notes}") 
    except Exception as e:
        print(e)


    try:
        print("\n========================================")
        print("Expected validation error:")
        invalid = SpaceStation(
            station_id="SS-002",
            name="national Space Station",
            crew_size=9999,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 1, 1, 9, 0, 0),
            is_operational=True,
            notes="All systems nominal.",
        )
        print(f"Crew Size: {invalid.crew_size} people") 
    except Exception as e:
        print(e.errors()[0]["msg"], end="\n\n")
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)