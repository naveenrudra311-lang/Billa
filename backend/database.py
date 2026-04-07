from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["start_ai"]

resume_collection = db["resumes"]