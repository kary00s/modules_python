from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum, auto
from datetime import datetime



class Rank(Enum):
    CADET = auto()
    OFFICER = auto()
    LIEUTENANT = auto()
    CAPTAIN = auto()
    COMMANDER = auto()


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    lanch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_id_validator(self):
        if not self.mission_id.startswith("M"):
            raise Exception("Mission ID must start with 'M'")
        return self
    @model_validator(mode="after")
    def rank_validator(self):
        counter = 0
        for item in self.crew:
            if item.rank == Rank.CAPTAIN or item.rank == Rank.COMMANDER:
                counter += 1
        if counter == 0:
            raise Exception("Must have at least one Commander or Captain")
        return self
    @model_validator(mode="after")
    def duration_validator(self):
        counter = 0
        total = len(self.crew)
        if self.duration_days < 365:
            for item in self.crew:
                if item.years_experience > 5:
                    counter += 1
                if counter < total / 2:
                    raise Exception(
                        "Long missions (> 365 days) require at least 50% experienced crew (5+ years)"
                    )
        return self

    @model_validator(mode="after")
    def active_validator(self) ->  any:
        counter = 0
        for item in self.crew:
            if item.is_active is False :
                raise Exception("All crew members must be active")
        return self

def main():
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        valid = SpaceMission(
                            mission_id="M2024_MARS",
                            mission_name="Mars Colony Establishment",
                            destination="Mars",
                            lanch_date=datetime.now(),
                            duration_days=900,
                            crew=[
                                CrewMember(
                                    member_id="M01",
                                    name="Sarah Connor",
                                    rank=Rank.COMMANDER,
                                    age=40,
                                    specialization="Mission Command",
                                    years_experience=6,
                                    is_active=True)
                                ,
                                CrewMember(
                                    member_id="M02",
                                    name="John Smith",
                                    rank=Rank.LIEUTENANT,
                                    age=50,
                                    specialization="navigation",
                                    years_experience=9,
                                    is_active=True,)
                                ,
                                CrewMember(
                                    member_id="M03",
                                    name="Alice Johnson",
                                    rank=Rank.OFFICER,
                                    age=25,
                                    specialization="Engineering",
                                    years_experience=14,
                                    is_active=True)]
                                ,
                            mission_status="Mars",
                            budget_millions=2500.0
                        )
        print(f"Mission: {valid.mission_name}")
        print(f"Destination: {valid.destination}")
        print(f"Duration: {valid.duration_days} days")
        print(f"Budget: ${valid.budget_millions}M")
        print(f"Crew size: {len(valid.crew)}")
        print("Crew members:")
        for item in valid.crew:
            print(
                f"- {item.name}"
                f" ({item.rank.name.lower()}) - {item.specialization}"
            )
    
    
        print("\n=========================================")
        prtin("Expected validation error:")
        invalid = SpaceMission(
                                mission_id="M2026_MOON",
                                mission_name="Moon Colony a77",
                                destination="Moon",
                                lanch_date=datetime.now(),
                                duration_days=10,
                                crew=[
                                    CrewMember(
                                        member_id="M01",
                                        name="yassin alo",
                                        rank=Rank.LIEUTENANT,
                                        age=40,
                                        specialization="Nothing",
                                        years_experience=6,
                                        is_active=True)
                                ,
                                    CrewMember(
                                        member_id="M02",
                                        name="karim nahiz",
                                        rank=Rank.CADET,
                                        age=50,
                                        specialization="navigation",
                                        years_experience=9,
                                        is_active=True,)
                                    ,
                                    CrewMember(
                                        member_id="M03",
                                        name="marouan nahiz",
                                        rank=Rank.OFFICER,
                                        age=26,
                                        specialization="Cadet",
                                        years_experience=14,
                                        is_active=True)]
                                ,
                                mission_status="Mars",
                                budget_millions=2500.0
                            )
        print(f"Mission: {invalid.mission_name}")
        print(f"Destination: {invalid.destination}")
        print(f"Duration: {invalid.duration_days} days")
        print(f"Budget: ${invalid.budget_millions}M")
        print(f"Crew size: {len(invalid.crew)}")
        print("Crew members:")
    except Exception as e:
        print(e)

main()
