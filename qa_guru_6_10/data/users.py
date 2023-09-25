import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: str
    photo: str
    address: str
    state: str
    city: str
