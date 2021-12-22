from pymongo import MongoClient
from app.schemas import user_helper


client = MongoClient('mongodb+srv://username:password@databasehost/database_name')
db = client.ncc_bim
student_collection = db['students']
user_collection = db['users']

async def add_user(user_data: dict) -> dict:
    user = user_collection.insert_one(user_data)
    new_user = user_collection.find_one({'_id': user.inserted_id})
    return user_helper(new_user)
