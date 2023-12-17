# mongodb compass 띄우기
from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할

# mongodb에 접속(connection) -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017/")   # mongoClient : class를 담은 변수

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['fruits']

# insert 작업 진행
mixed_fruit = {"name": "포도", 
              "color": ["보라색", "갈색", "노란색"],  # color : list
              "origin": "한국", 
              "price_per_kg": 8000}
result = collection.insert_one(mixed_fruit)
pass

# 분리 입력 (fruits, fruits_colors)
# insert fruits 작업 진행
dict_fruit = {"name": "포도",
              "origin": "한국", 
              "price_per_kg": 8000}
result = collection.insert_one(dict_fruit)
#  insertedId: ObjectId("657bf165a8da734b4f59f458")  # name, origin, price_per_kg insert_one 한 결과값
result.inserted_id
print("result.inserted_id".format(result.inserted_id))  # result : class
inserted_id = result.inserted_id   # 앞 inserted_id : 현재 파일에서 사용하는 변수,  뒤 inserted_id : class 안에 있음 => 영역이


# insert fruits_colors 작업 진행
# [{"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "보라색"}
#  , {"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "갈색"}
#  , {"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "노란색"}]  #mongoDB에 넣어보고 코드화시킨다

fruits_colors = [{"color": "보라색"}
                , {"color": "갈색"}
                , {"color": "노란색"}]

list_fruits_colors = list()
for dict_color in fruits_colors :
    dict_color["fruits_id"] = inserted_id  # for문에 첫 번째로 돌 때 [{"fruits_id" : ObjectId("657bf165a8da734b4f59f458"),"color": "보라색"} 와 같이 만들어진다.
    list_fruits_colors.append(dict_color)
    pass    # for문이 끝나고나면 insert 하기만 하면됨

# collection fruits_colors
collection_fruits_colors = database["fruits_colors"]

collection_fruits_colors.insert_many(list_fruits_colors)

# insert 한 값 find from fruits_colors
documents = collection_fruits_colors.find( {"fruits_id" : { "$eq" : inserted_id } } )

pass

# db.fruits_colors.find( {fruits_id : { $eq : ObjectId("657bf165a8da734b4f59f458") } } ) ;