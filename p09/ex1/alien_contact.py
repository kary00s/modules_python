from datetime import datetime
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from enum import Enum, auto


class ContactType(Enum):
    RADIO = auto()
    VISUAL = auto()
    PHYSICAL = auto()
    TELEPATHIC = auto()


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(gt=0.0, lt=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def contact_id_validator(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        return self

    @model_validator(mode="after")
    def physical_validator(self):
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def telepathic_validator(self):
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at "
                                 "least 3 witnesses")
        return self

    @model_validator(mode="after")
    def signal_validator(self):
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include a message")
        return self


def main():
    try:
        valid = AlienContact(
            contact_id="AC_2026_001",
            timestamp=datetime(2020, 1, 1, 3, 50, 50),
            location="Area 51, khouribga",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            is_verified=True,
        )

        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")
        print("ID: ", valid.contact_id)
        print("Type: ", valid.contact_type)
        print("Location: ", valid.location)
        print("Signal: ", valid.signal_strength)
        print("Duration: ", valid.duration_minutes)
        print("Witnesses: ", valid.witness_count)
        print("Message: ", valid.message_received)

        print("\n======================================")
        print("Expected validation error:")
        invalid = AlienContact(
            contact_id="AC_2026_002",
            timestamp=datetime.now(),
            location="Smoking Area, 1337",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="We will destroy your planet ",
            is_verified=True,
        )
        print(invalid.witness_count)
    except Exception as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
