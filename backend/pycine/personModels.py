from pydantic import BaseModel
from typing import Optional


class Person(BaseModel):
    id: int
    name: str
    popularity: Optional[float] = None
    known_for_department: Optional[str] = None
    profile_path: Optional[str] = None

class PersonResults(BaseModel):
    results: list[Person]
    page: int
    total_pages: int
    total_results: int