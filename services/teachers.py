from random import choice
from services.models import TeachersModel


class Teachers:
    """
    Класс, реализующий логику работы с данными о преподавателях
    """
    # Русские названия дней недели
    week = {'mon': 'Понедельник',
            'tue': 'Вторник',
            'wed': 'Среда',
            'thu': 'Четверг',
            'fri': 'Пятница',
            'sat': 'Суббота',
            'sun': 'Воскресенье'
            }

    def __init__(self, teacher_id):
        self.id = teacher_id
        teacher = TeachersModel.query.get(self.id)
        self.name = teacher.name
        self.about = teacher.about
        self.rating = teacher.rating
        self.picture = teacher.picture
        self.price = teacher.price
        self.goals = teacher.goals
        self.free_time = teacher.free_time

    def get_free_time(self):
        """
        Данная функция извлекает свободные часы преподавателя из БД
        :return: dict
        """
        free_time = self.free_time
        free_hours = {}

        for i in free_time:
            times = []
            for key, val in free_time[i].items():
                if val is True:
                    times.append(key)

            temp_data = free_hours.fromkeys([i], times)
            free_hours.update(temp_data)

        return free_hours


def __get_teachers__(teachers_id):
    """
    Данная функция подготавливает список преподавателей, убирая лишнии данные, для дальнейшего использования в функциях:
    get_goal_teachers и get_some_teachers.
    :param teachers_id: list идентификаторов преподавателей
    :return: list of dict
    """
    teachers = []
    for teacher_id in teachers_id:
        teacher = Teachers(teacher_id)

        teacher = {"name": teacher.name,
                   "about": teacher.about,
                   "rating": teacher.rating,
                   "picture": teacher.picture,
                   "price": teacher.price,
                   "id": teacher_id}

        teachers.append(teacher)

    return teachers


def get_goal_teachers(goal):
    """
    Данная функция извлекает из данных о преподавателях только тех, кто соответствует выбранной цели.
    :param goal: цель для занятия
    :return: list of dict
    """
    teachers_id = []
    teachers_ = TeachersModel.query.all()

    for teacher in teachers_:
        for goal_ in teacher.goals:
            if goal == goal_.name_eng:
                teachers_id.append(teacher.id)

    teachers = __get_teachers__(teachers_id)

    return teachers


def get_some_teachers(quantity=None):
    """
    Данная функция возвращает набор данные о некотором числе преподавателей,
    если число не указано, то данные всех преподавателей.
    Сортировка осуществляется случайным образом.
    :param quantity: количество преподавателей
    :return: list of dict
    """
    teachers_id = []
    teachers_ = TeachersModel.query.all()

    for teacher in teachers_:
        teachers_id.append(teacher.id)

    if quantity is not None:
        random_id = []
        for _ in range(quantity):
            choice_id = choice(teachers_id)
            random_id.append(choice_id)
            teachers_id.remove(choice_id)
        teachers = __get_teachers__(random_id)

    else:
        random_id = []
        for _ in range(len(teachers_id)):
            choice_id = choice(teachers_id)
            random_id.append(choice_id)
            teachers_id.remove(choice_id)
        teachers = __get_teachers__(random_id)

    return teachers
