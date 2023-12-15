# docs/quests/solvingProblem_functions.py, solvingProblem_main.py
# - refer : Datasets, Screen Definition
# - 문제 풀기를 CRUD(insert, find, update, delete) 작성
# - 변수 리스트 -> DB 저장(문항과 답항 하나 레코드) -> 응답된 해답 저장
# - 최소 function 2개 사용(solvingProblem_functions은 import로 사용)

from pymongo import MongoClient   # mongodb compass 띄우기
def connect():
    mongoClient = MongoClient("mongodb://localhost:27017")  # mongodb에 접속(connection)
    database = mongoClient["local"]  # database 연결하는 변수
    collection = database['solvingProblem']  # collection 작업 변수
    return collection


def insert_quiz_list():
    quiz_list = [
        {
            "question": "Python의 생성자 함수 이름은 무엇인가요?",
            "choices": ["__init__", "__main__", "__str__", "__del__"],
            "answer": "__init__",
            "answer_number": 1,
            "score": 20
        },
        {
            "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
            "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
            "answer": "print('Hello, World!')",
            "answer_number": 1,
            "score": 20
        },
        {
            "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
            "choices": ["//", "/* */", "#", "--"],
            "answer": "#",
            "answer_number": 3,
            "score": 20
        },
        {
            "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
            "choices": ["size()", "length()", "len()", "sizeof()"],
            "answer": "len()",
            "answer_number": 3,
            "score": 20
        },
        {
            "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
            "choices": ["str()", "int()", "char()", "float()"],
            "answer": "int()",
            "answer_number": 2,
            "score": 20
        }
    ]#리스트
    return quiz_list

solvingProblem = []
collection = connect()     
quiz_list = insert_quiz_list()

for x in quiz_list:  # 위의 리스트를 x라는 변수에 넣는 것을 반복한다.
    if collection.count_documents(x) == 0: # 동일한 내용이 collection에 있는지 확인하고, 없을 경우만 내용을 저장하도록 한다.
        collection.insert_one(x) #MongoDB에 연결하여 리스트에 있는 내용을 한 라인씩 입력한다.
        pass 

insert_quiz_list()

def run(): 
    quiz_list = list(collection.find()) # collection에 있는 모든 문서를 가져와 list로 만들고, 그것을 quiz_list라고 지정한다. --> Q. vscode에서 만들어서 몽고db로 connect 하는걸로 알고 있는데 collection에 있는 문서를 가져 온다는말이 아직 이해되지 않음.
    user_name = input("이름을 입력해 주세요: ") 
    final_score = 0 
    for i in range(len(quiz_list)): 
        quiz = quiz_list[i] 
        print(str(i+1) + ". " + quiz["question"], end=" ")  # question
        print(str(quiz["score"])+"점")                      # score Q.20점이라는 점수가 어떻게 나오게 하는걸까?
        for j in range(len(quiz["choices"])):
            choice = quiz["choices"][j]                     # choice라는 변수에 quiz_list의 choices 항목을 j에서 가져온다.
            print(str(j+1)+". "+choice)                     # str(j+1) = choice 항목 번호 가져오기(question이 여러개이므로)
        user_answer =int(input("답을 입력해 주세요(번호로 입력): ")) 
        if user_answer == quiz["answer_number"]: 
            final_score += quiz["score"] 
        collection.update_one({'_id': quiz['_id']}, {"$set": {user_name: user_answer}})   # update.one : 한 가지 항목에 대하여 수정한다. Q. 그 안에 값들 이해 불가
    print(user_name + "님의 점수는 " + str(final_score) + "점 입니다.")
    return