import dotenv
import os
from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ConfigDict, BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated
from bson import ObjectId
from pycine import moviemodels
import motor.motor_asyncio
from pymongo import ReturnDocument
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pycine import tmdb

dotenv.load_dotenv(".env") 
uri = os.environ["MONGODB"]
client = motor.motor_asyncio.AsyncIOMotorClient(uri)
db = client['tmdb'] 
moviescol = db['movies']


app = FastAPI()


origins = [
 "http://localhost",
 "http://localhost:*",
 "http://localhost:5173",
]
app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)


@app.get("/")
def hello():
    return{"status":"pycine is running"}

@app.get(
   "/find/",
    response_description="List all movies",
    response_model=moviemodels.MovieCollection,
    response_model_by_alias=False,
)
async def list_movies():
    return moviemodels.MovieCollection(movies=await moviescol.find().to_list(20))



@app.get("/movie/{id}")
def get_movie(id:int):
    return tmdb.get_movie(id)

@app.get("/movie")
def search_movies():
    params = {
        "sort_by": "vote_average.desc"
    }
    return tmdb.search_movies(params)

@app.get("/movies/top")
def search_movies():
    return tmdb.search_movies()

@app.get("/person/{id}")
def get_person(id:int):
    return tmdb.get_person(id)

@app.get("/person/{id}/allmovies")
def get_person(id:int):
    return tmdb.get_person_movies(id)

@app.get("/byname/person/{name}")
def search_person(name:str):
    return tmdb.search_person(name)

@app.get("/trending/person/{type}")
def treding_person(type:str):
    return tmdb.treding_person(type)


@app.get("/popular/person")
def treding_person():
    return tmdb.popular_person()

