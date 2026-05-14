#!/bin/usr/evn python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


# ... -> valor por defecto
# ge ->  greater or equal
# le -> less than or equal
class ValidationSystem(BaseModel):
    """Check and validate station data"""
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = Field(True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():
    """Demostrate valid and invalid ValidationSystem model"""
    print("Space Station Data Validation")
    print("========================================")
    try:
        valid_station = ValidationSystem(
            station_id="ISS001",
            name="International Space Station",
            crew_size="6",
            power_level="85.5",
            oxygen_level="92.3",
            last_maintenance=datetime(2026, 4, 11, 13, 25, 59),
            is_operational=True
        )
        status = "Operational" if valid_station.is_operational else "Inactive"
        # print valid_station data:
        print("Valid station created:")
        print(f"ID: {valid_station.station_id}")
        print(f"Name: {valid_station.name}")
        print(f"Crew: {valid_station.crew_size} people")
        print(f"Power: {valid_station.power_level}%")
        print(f"Oxygen: {valid_station.oxygen_level}%")
        print(f"Statuss: {status}")
    except ValidationError as e:
        error = e.errors()
        zero = error[0]
        msg = zero['msg']
        print(f"{msg}")
    print()
    print("========================================")
    print("Expected validation error:")
    try:
        not_valid_station = ValidationSystem(
            station_id="ISS001",
            name="International Space Station",
            crew_size="21",
            power_level="85.5",
            oxygen_level="92.3",
            last_maintenance=datetime(2026, 4, 11, 13, 25, 59),
            is_operational=True
        )
        print(not_valid_station)
    except ValidationError as e:
        error = e.errors()
        zero = error[0]
        msg = zero['msg']
        print(f"{msg}")


if __name__ == "__main__":
    main()
