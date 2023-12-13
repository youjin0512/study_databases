# mongodb compass 띄우기
from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할

# mongodb에 접속(connection) -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017/")   # mongoClient : class를 담은 변수

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
collection.insert_one({"name": "수박",  #function
                       "color": "초록",
                       "origin": "한국",
                       "price_per_kg": 15000}
                       )
dict_fruit = {"name": "포도", "color": "보라", "origin": "한국", "price_per_kg": 8000}
collection.insert_one(dict_fruit)
pass