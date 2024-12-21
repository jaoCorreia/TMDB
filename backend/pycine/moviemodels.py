
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
PyObjectId = Annotated[str, BeforeValidator(str)]
from pydantic import BaseModel
from typing import Optional
class Movie(BaseModel):
    
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    genres: Optional[list] = None
    original_language: str
    overview: str
    popularity: Optional[float] = None
    poster_path: Optional[str] = None
    release_date: str
    vote_count: Optional[int] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
    )

class MovieCollection(BaseModel):
    movies: list[Movie]

class MovieResults(BaseModel):
    results: list[Movie]
    page: int 
    total_pages: int
    total_results: int 
    