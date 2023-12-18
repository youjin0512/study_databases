# MongoDB와 연결
from pymongo import MongoClient
mongoClient = MongoClient('mongodb://localhost:27017/')
database = mongoClient['local'] 
todos_list = database['todos_list']
participants = database['participants']
participants_todos = database['participants_todos']


# 참여자, ToDo List, Status 항목을 추가
todos_list.update_many({}, {'$set': {'참여자': "", 'Todo List': "", 'Status': ""}})

# 저장할 데이터 생성
data = {"title": ["주간 보고서 작성", "이메일 확인 및 응답", "회의 준비", "프로젝트 계획서 수정", "팀 멤버와의 1:1 면담"]}

# 데이터를 DB에 저장
participants_todos.insert_one(data)

# ToDo 리스트 생성
insert_todo_list = [
    {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
    {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
    {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
    {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
    {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},
]


# ToDo 리스트를 DB에 저장
if todos_list.count_documents({}) == 0 :
    todos_list.update_many(insert_todo_list)


# 참여자 리스트 생성
participant_list = ['참여자1', '참여자2', '참여자3']

# for i, participant in enumerate(participant_list, start=1):
#     # 참여자, ToDo List, Status 항목의 값을 설정
#     todos_list.update_one({'_id': i}, {'$set': {'참여자': participant, 'Todo List': f'{i}. 주간 보고서 작성', 'Status': '완료'}})

for participant in participant_list:
    # 참여자의 이름 입력
    name = input("Input Your Name: ")

    # 참여자가 참여자1일 경우, 두 번의 ToDo 항목 입력
    if name == '참여자1':
        repeat_times = 2
    else:
        repeat_times = 1

    for _ in range(repeat_times):
        print("ToDo List 중 하나 선택 하세요 !")
        print("1. 주간 보고서 작성, 2. 이메일 확인 및 응답, 3. 회의 준비, 4. 프로젝트 계획서 수정, 5.팀 멤버와의 1:1 면담")
        title_no = input("Title 번호: ")
        status = input("Status: ")
        end_flag = input("종료 여부: ")

        # 참여자 정보 업데이트
        participants.update_one({'name': name}, {'$set': {'name': name}}, upsert=True)
        # participants.update_one({'name': name}, {'$set': {'name': name}}, upsert=True)는 MongoDB의 update_one 메소드를 사용하여 데이터를 업데이트하는 코드입니다.
        # update_one 메소드는 첫 번째 인자로 주어진 조건에 맞는 단 하나의 문서(document)를 찾아 두 번째 인자로 주어진 내용으로 업데이트합니다.
        # 여기서 사용된 $set은 MongoDB의 update 연산자로, 특정 필드의 값을 설정하거나 변경하는 역할을 합니다.
        # 즉, 'name': name으로 주어진 조건에 맞는 문서를 찾아, 해당 문서의 'name' 필드를 name 값으로 설정하거나 변경합니다.
        # 마지막에 upsert=True 옵션이 주어져 있는데, 이는 upsert 옵션을 활성화하는 것입니다. upsert는 update와 insert를 합친 말로,
        # 해당 조건에 맞는 문서가 존재하면 업데이트하고, 존재하지 않으면 새로운 문서를 삽입하는 동작을 의미합니다.
        # 따라서, 이 코드는 참여자의 이름이 name인 문서를 찾아 그 'name' 필드를 name 값으로 업데이트하고, 그런 문서가 없으면 새로운 문서를 삽입하도록 하는 역할을 합니다.
        # 이렇게 하면 참여자의 이름이 데이터베이스에 항상 최신 상태로 유지되게 됩니다.

        # 업무 정보 업데이트
        todo_item = todos_list.find_one({'_id': int(title_no)})

        # ToDo 항목의 유효성 체크
        if todo_item is None:
            print("")
            continue

        participants_todos.insert_one({'participant': name, 'todo': todo_item['title'], 'status': status})

        # 종료 조건 확인
        # 종료여부(계속:c, 종료:q, 프로그램 종료:x)
        if end_flag == 'c':
            pass
        elif end_flag == 'q':
            break
        elif end_flag == 'x':
            break

    print("\n------------------------")  # 각 참여자의 입력이 끝난 후에 한 줄을 띄우고, 그 다음 줄에 점선을 출력

print("프로그램이 종료되었습니다.")