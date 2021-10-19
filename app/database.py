from pymongo import MongoClient
from app.schemas import user_helper

# client = MongoClient('mongodb://localhost:27017/')
client = MongoClient('mongodb+srv://SameerJoshi:SameerJoshi@ncc-bim.q8vmf.mongodb.net/ncc_bim?retryWrites=true&w=majority')
db = client.ncc_bim
student_collection = db['students']
user_collection = db['users']

async def add_user(user_data: dict) -> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({'_id': user.inserted_id})
    return user_helper(new_user)
