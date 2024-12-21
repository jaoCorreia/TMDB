

import os 
import dotenv
dotenv.load_dotenv(".env")
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = os.environ["MONGODB"]
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['tmdb'] 
moviescol = db['movies']



try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    print(client['tmdb']['movies'].list_search_indexes())

    movie = {
        'id': 218,
        'title': 'Terminator',
        'genres': ['Action', 'Sci-fi'], 
        'original_language': 'en-Us'
    }
    # INSERT 
    # moviescol.insert_one(movie)

    #READ
    print(moviescol.find_one({"id": 218}))
except Exception as e:
    print(e)