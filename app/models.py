# app/models.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()  # Load biến môi trường từ .env

# URL kết nối MongoDB Atlas từ biến môi trường
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['plant_database']

def get_all_plants():
    return list(db.plants.find())

def add_plant(plant_data):
    db.plants.insert_one(plant_data)

def update_plant(plant_id, plant_data):
    db.plants.update_one({'_id': plant_id}, {'$set': plant_data})

def delete_plant(plant_id):
    db.plants.delete_one({'_id': plant_id})

def get_plant_by_code(plant_code):
    return db.plants.find_one({'plant_code': plant_code})

def get_plants_by_code(plant_code):
    return list(db.plants.find({'plant_code': plant_code}))
