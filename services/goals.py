from services.models import GoalsModel


class Goals:
    """
    Класс, реализующий логику работы с данными о целях
    """

    def find_goals(self):
        """
        Функция, которая извлекает данные о всех целях
        :return: list
        """
        goals = GoalsModel.query.all()

        return goals

    def names_goals(self):
        """
        Функция, которая извлекает русские названия целей и прикрепляет к них  эмодзи
        :return: dict
        """
        names = {}
        goals = self.find_goals()
        for goal in goals:
            name = goal.emoji + " " + goal.name_ru
            temp_data = names.fromkeys([goal.name_eng], name)
            names.update(temp_data)

        return names

    def get_emoji(self, goal):
        """
        Функция, которая возвращает эмодзи для цели
        :param goal: str, английское название цели
        :return: str
         """
        goals = self.find_goals()
        for goal_ in goals:
            if goal_.name_eng == goal:
                return goal_.emoji

    def get_ru_name(self, goal):
        """
        Функция, которая возвращает русское название для цели
        :param goal: str, английское название цели
        :return: str
         """
        goals = self.find_goals()
        for goal_ in goals:
            if goal_.name_eng == goal:
                return goal_.name_ru.lower()
