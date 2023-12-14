# * quest
# - fruit_info 리스트를 mongo에 저장
# - 최소 function 2개 : connect, insert(저장)

from pymongo import MongoClient
def connect():
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["local"]
    collection = database['fruits']
    return collection

def insert(collection,dict_fruit):
    collection.insert_one(dict_fruit)
    return

fruit_info = [
            {"name": "수박", "color": "초록", "origin": "한국", "price_per_kg": 15000},
            {"name": "바나나", "color": "노랑", "origin": "필리핀", "price_per_kg": 3000},
            {"name": "오렌지", "color": "주황", "origin": "미국", "price_per_kg": 5000},
            {"name": "포도", "color": "보라", "origin": "한국", "price_per_kg": 8000},
            {"name": "수박", "color": "초록", "origin": "한국", "price_per_kg": 15000}
]

for i in range(len(fruit_info)):
    dict_fruit = fruit_info[i]
    collection = connect()
    insert(collection,dict_fruit)