# 클래스 만들기

class todolistproblem() : #todolistproblem class
    def __init__(self):
        self.call_todo = []
        self.call_parti = []
        self.call_parti_todo = []
        self.todo_list=[]

    def mongo (self, collection_todo,collection_parti,collection_parti_todo): #값들 불러오기
        from pymongo import MongoClient
        mongoclient = MongoClient("mongodb://localhost:27017")
        database = mongoclient["local"]
        self.coll_todo = database[collection_todo]
        self.coll_parti = database[collection_parti]
        self.coll_parti_todo = database[collection_parti_todo]
        self.todo_list = list(self.coll_todo.find({}, {"_id":1, "title":1}))


    # 참여자 이름 입력하고 print하기
    def doit (self) :
        # 첫 번째 while문으로 parti는 참여자의 이름에 해당됨
        while True :
            parti = input("Input Your Name: ")
            # participants collection에 참여자 입력
            result = self.coll_parti.insert_one({"parti" : parti})
            parti_id = result.inserted_id # 참여자의 id

            # 두 번째 while문
            while True :             
                print("ToDo List 중 하나 선택 하세요!")
                for i in range(5) :
                    print("{}.{}".format(i+1,self.todo_list[i]["title"]))
                title_num = int(input("Title 번호 : "))
                todo_title = self.todo_list[title_num-1]['title']
                title_status = input("Status : ")

                # 불러온 todo_list의 '_id'를 불러옴
                
                self.coll_parti_todo.insert_one({'참여자_id':parti_id, '참여자' : parti,
                                                "Todo title":todo_title, "Status":title_status})
                
                #종료 여부 확인
                print("")
                keepgoing = input("종료 여부를 알려주십시오. : ")
                print("")
                if keepgoing == "c" :
                    continue
                elif keepgoing == "q" :
                    print("---------")
                    break
                elif keepgoing =='x' : 
                    print("---------")
                    print("프로그램이 종료되었습니다.")
                    return