import os
import json
from app import db
from services.models import TeachersModel, GoalsModel

path = f"{os.getcwd()}/data.json"

with open(path, "r") as f:
    data_teacher = json.load(f)

with open(path, "r") as f:
        data_goal = json.load(f)
        #return data['goals']

#print(data_teacher['teachers'])
emoji = {"travel": "⛱",
         "study": "🏫",
         "work": "🏢",
         "relocate": "🚜",
         "prog": "⌨"}


for teacher in data_teacher['teachers']:
    print(teacher)

    teacher_data = TeachersModel(name=teacher["name"],
                                 about=teacher["about"],
                                 rating=teacher["rating"],
                                 picture=teacher["picture"],
                                 price=teacher["price"],
                                 free_time=teacher["free"],
                                 )
    db.session.add(teacher_data)

    for goal in teacher["goals"]:
        goal_data = GoalsModel(name_eng=goal,
                               name_ru=data_goal["goals"][goal],
                               emoji=emoji[goal],
                               )
        db.session.add(goal_data)
        goal_data.teachers.append(teacher_data)

# db.session.commit()
