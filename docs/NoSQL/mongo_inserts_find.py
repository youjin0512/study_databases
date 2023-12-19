# mongodb compass 띄우기
from pymongo import MongoClient     # pymongo : module, Mongoclient : class      # client : mongoDB의 compass 같은 역할

# mongodb에 접속(connection) -> 자원에 대한 class
# mongoClient = MongoClient("mongodb://localhost:27017/")   # mongoClient : class를 담은 변수  # 내 주소
mongoClient = MongoClient("mongodb://192.168.0.136:27017")   # mongoClient : class를 담은 변수 # 경하님 IP

# database 연결
database = mongoClient["local"]

# collection 작업
collection = database['posts']

# insert 작업 진행
documents = collection.find({}, {"_id":1, "title":1, "likes":1})   # _id, title, likes를 projection  # documents = cursor

# cast cursor to list
list_documents = list(documents)
print("list_documents length : {}".format(len(list_documents)))   # list_documents length : 6 (6개)
for document in documents:   # documents에 대하여 next 라는 fucntion으로 돌고 있음.
    # cursor는 next를 하면 다음 레코드라고 지정해줌 -> record의 위치값   cursor : next를 눌러서 순차적으로 위치값을 나타냄.
    print("document : {}".format(document))
    pass
pass