# * quest
# - fruit_info 리스트를 mongo에 저장
# - 최소 function 2개 : connect, insert(저장)

from pymongo import MongoClient   # mongodb compass 띄우기
def connect():
    mongoClient = MongoClient("mongodb://localhost:27017")  # mongodb에 접속(connection)
    database = mongoClient["local"]  # database 연결하는 변수
    collection = database['fruits']  # collection 작업 변수
    return collection

def insert(collection,dict_fruit):
    collection.insert_one(dict_fruit)
    return

fruit_info = [
            {"name": "사과", "color": "빨강", "origin": "한국", "price_per_kg": 4000},
            {"name": "바나나", "color": "노랑", "origin": "필리핀", "price_per_kg": 3000},
            {"name": "오렌지", "color": "주황", "origin": "미국", "price_per_kg": 5000},
            {"name": "포도", "color": "보라", "origin": "한국", "price_per_kg": 8000},
            {"name": "수박", "color": "초록", "origin": "한국", "price_per_kg": 15000}
]  #리스트

for i in range(len(fruit_info)):    # fruit_into 리스트의 개수를 range안에 넣어 for 함수로 돌리기
    dict_fruit = fruit_info[i]
    collection = connect()
    insert(collection,dict_fruit)