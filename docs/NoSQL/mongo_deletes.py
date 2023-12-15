# mongodb compass 띄우기
from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할

# mongodb에 접속(connection) -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017/")   # mongoClient : class를 담은 변수

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert many 작업 진행
list_fruits = [
    {"name": "사과", "color": "빨강", "origin": "한국", "price_per_kg": 4000},
    {"name": "바나나", "color": "노랑", "origin": "필리핀", "price_per_kg": 3000},
    {"name": "오렌지", "color": "주황", "origin": "미국", "price_per_kg": 5000},
    {"name": "포도", "color": "보라", "origin": "한국", "price_per_kg": 8000},
    {"name": "수박", "color": "초록", "origin": "한국", "price_per_kg": 15000}
]
insert_result = collection.insert_many(list_fruits)

list_inserted_ids = insert_result.inserted_ids        #_ids가 return 된다  #inserted_ids : 리스트

# delete inserted records by _ids
collection.delete_many({"_id":list_inserted_ids[0]})   # 인덱스 0 삭제
pass