#!/bin/usr/evn python3

from __future__ import annotations
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from enum import Enum


class Rank(str, Enum):
    CADET = 'cadet',
    OFFICER = 'officer',
    LIEUTENANT = 'lieutenant',
    CAPTAIN = 'captain',
    COMMANDER = 'commander'


class CrewMember(BaseModel):
    """Check and validate crew member data"""
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = Field(True)


class SpaceMission(BaseModel):
    """Check and validate Space mission data"""
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: list[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = Field("planned")
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_id(self) -> SpaceMission:
        """Validate ID starts with 'M'"""
        if self.mission_id.startswith('M'):
            return self
        raise ValueError("Mission ID must start with 'M'")

    @model_validator(mode='after')
    def validate_crew_member(self) -> SpaceMission:
        """Validate there is at least one Captain or Commander
            in the Space Mission"""
        for member in self.crew:
            if (
                member.rank == Rank.CAPTAIN or
                member.rank == Rank.COMMANDER
            ):
                return self
        raise ValueError(
            "Mission must have at least one Commander or Captain"
            )

    @model_validator(mode='after')
    def validate_long_mission_experience(self) -> SpaceMission:
        """Check the years of experience of each crew member
        in a long mission"""
        members = len(self.crew)
        experienced_member = 0
        if self.duration_days > 365:
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_member += 1
            if experienced_member >= (members / 2):
                return self
            raise ValueError("Long missions need 50% "
                             "experienced crew (5+ years)")
        return self

    @model_validator(mode='after')
    def validate_active_members(self) -> SpaceMission:
        """Validate all crew members in the mission are active"""
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main():
    """Show a valid mission with crew details and an
    invalid mission that fails validation."""

    print("Space Mission Crew Validation")
    print("=========================================")

    valid_data = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "captain",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 19,
                "is_active": True
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "captain",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 30,
                "is_active": True
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "commander",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "captain",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
    }
    try:
        mission_1 = SpaceMission.model_validate(valid_data)
        print("Valid mission created:")
        print(f"Mission: {mission_1.mission_name}")
        print(f"ID: {mission_1.mission_id}")
        print(f"Destinantion: {mission_1.destination}")
        print(f"Duration: {mission_1.duration_days} days")
        print(f"Budget: ${mission_1.budget_millions}M")
        print(f"Crew size: {len(mission_1.crew)}")
        print("Crew members:")
        for member in mission_1.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].replace("Value error, ", ""))

    # not_valid
    print("\n=========================================")
    not_valid_data = {
        "mission_id": "M2024_TITAN",
        "mission_name": "Solar Observatory Research Mission",
        "destination": "Solar Observatory",
        "launch_date": "2024-03-30T00:00:00",
        "duration_days": 451,
        "crew": [
            {
                "member_id": "CM001",
                "name": "Sarah Williams",
                "rank": "cadet",
                "age": 43,
                "specialization": "Mission Command",
                "years_experience": 3,
                "is_active": True
            },
            {
                "member_id": "CM002",
                "name": "James Hernandez",
                "rank": "cadet",
                "age": 43,
                "specialization": "Pilot",
                "years_experience": 3,
                "is_active": True
            },
            {
                "member_id": "CM003",
                "name": "Anna Jones",
                "rank": "cadet",
                "age": 35,
                "specialization": "Communications",
                "years_experience": 3,
                "is_active": True
            },
            {
                "member_id": "CM004",
                "name": "David Smith",
                "rank": "cadet",
                "age": 27,
                "specialization": "Security",
                "years_experience": 15,
                "is_active": True
            },
            {
                "member_id": "CM005",
                "name": "Maria Jones",
                "rank": "captain",
                "age": 55,
                "specialization": "Research",
                "years_experience": 30,
                "is_active": True
            }
        ],
        "mission_status": "planned",
        "budget_millions": 2208.1
        }
    try:
        mission_2 = SpaceMission.model_validate(not_valid_data)
        print("Valid mission created:")
        print(f"Mission: {mission_2.mission_name}")
        print(f"ID: {mission_2.mission_id}")
        print(f"Destinantion: {mission_2.destination}")
        print(f"Duration: {mission_2.duration_days} days")
        print(f"Budget: ${mission_2.budget_millions}M")
        print(f"Crew size: {len(mission_2.crew)}")
        print("Crew members:")
        for member in mission_2.crew:
            print(f"- {member.name} ({member.rank}) - {member.specialization}")
    except ValidationError as e:
        for err in e.errors():
            print(err["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
