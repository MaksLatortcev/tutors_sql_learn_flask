from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, RadioField, SelectField
from services.models import db, BookingModel, RequestModel


class BookingForm(FlaskForm):
    """
    Класс, реализующий получение данных записи на урок к преподавателю
    """
    # Параметры формы
    day = StringField()
    time = StringField()
    id_teacher = IntegerField()
    name = StringField('Вас зовут')
    phone = IntegerField('Ваш телефон')
    submit = SubmitField('Записаться на пробный урок')

    def save_booking_data(self):
        """
        Функция, которая сохранаяет данные о записи на урок в таблицу booking
        """
        booking_data = BookingModel(name=self.name.data,
                                    phone=self.phone.data,
                                    day=self.day.data,
                                    time=self.time.data,
                                    teacher_id=self.id_teacher.data)

        db.session.add(booking_data)
        db.session.commit()

        return print('Сохранно в таблицу booking')


class RequestForm(FlaskForm):
    """
     Класс, реализующий сохранение данных заявок на подбор преподавателя.
    """
    # Пусть к файлу с данными
    path = None
    # параметры формы
    goal = RadioField('Какая цель занятий?',
                      choices=[('Для путешествий', 'Для путешествий'),
                               ('Для школы', 'Для школы'),
                               ('Для работы', 'Для работы'),
                               ('Для переезда', 'Для переезда')]
                      )
    time = RadioField('Сколько времени есть?',
                      choices=[('1-2 часа в неделю', '1-2 часа в неделю'),
                               ('3-5 часов в неделю', '3-5 часов в неделю'),
                               ('5-7 часов в неделю', '5-7 часов в неделю'),
                               ('7-10 часов внеделю', '7-10 часов внеделю')]
                      )
    name = StringField('Вас зовут')
    phone = IntegerField('Ваш телефон')
    submit = SubmitField('Найдите мне преподавателя')

    def save_request_data(self):
        """
        Функция, которая сохранаяет данные заявки на подбор преподавателя в таблицу request
        """

        request_data = RequestModel(name=self.name.data,
                                    phone=self.phone.data,
                                    time_duration=self.time.data,
                                    goal=self.goal.data)

        db.session.add(request_data)
        db.session.commit()

        return print('Сохранно в таблицу request')


class SelectForm(FlaskForm):
    """
    Класс, реализующий фильтры для страницы со всеми преподавателями - /all/
    """
    filter = SelectField(choices=[('1', 'В случайном порядке'),
                                  ('2', 'Сначала лучшие по рейтингу'),
                                  ('3', 'Сначала дорогие'),
                                  ('4', 'Сначала недорогие')]
                         )
