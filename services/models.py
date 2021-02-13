from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

teachers_goals_association = db.Table("teacher_goals",
                                      db.Column("teacher_id", db.Integer, db.ForeignKey("teachers.id")),
                                      db.Column("goal_id", db.Integer, db.ForeignKey("goals.id"))
                                      )


class TeachersModel(db.Model):
    """
    Класс реализует модель данных для списка преподавателей
    """
    __tablename__ = "teachers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    free_time = db.Column(JSON)
    student = db.relationship("BookingModel")
    goals = db.relationship("GoalsModel",
                            secondary=teachers_goals_association,
                            back_populates="teachers")


class GoalsModel(db.Model):
    """
    Класс реализует модель для списка целей изучения языка
    """
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    name_eng = db.Column(db.String, nullable=False)
    name_ru = db.Column(db.String, nullable=False)
    emoji = db.Column(db.String, nullable=False)
    teachers = db.relationship("TeachersModel",
                               secondary=teachers_goals_association,
                               back_populates="goals")


class BookingModel(db.Model):
    """
    Класс реализует модель данных для хранения заявок на бронирование занятия с преподавателем
    """
    __tablename__ = "booking"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    day = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))


class RequestModel(db.Model):
    """
    Класс реализует модель данных для хранения заявок на подбор преподавателя
    """
    __tablename__ = "request"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    time_duration = db.Column(db.String, nullable=False)
    goal = db.Column(db.String, nullable=False)
