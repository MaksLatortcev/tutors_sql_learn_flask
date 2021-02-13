import os
from flask import Flask, render_template
from flask_migrate import Migrate
from services.teachers import Teachers, get_goal_teachers, get_some_teachers
from services.goals import Goals
from services.forms import BookingForm, RequestForm, SelectForm
from services.models import db


app = Flask(__name__)
app.secret_key = str(os.urandom(10))
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def main():
    teachers = get_some_teachers(quantity=6)
    goals = Goals().names_goals()
    output = render_template("index.html",
                             teachers=teachers,
                             goals=goals)
    return output


@app.route("/all/", methods=["GET", "POST"])
def all_teachers():
    teachers = get_some_teachers()
    form = SelectForm()
    output = render_template("all.html",
                             teachers=teachers,
                             form=form)
    return output


@app.route("/goals/<goal>/")
def goal(goal):
    print(type(goal))
    goal_teachers = get_goal_teachers(goal)
    name_ru = Goals().get_ru_name(goal)
    emoji = Goals().get_emoji(goal)
    output = render_template("goal.html",
                             goal=goal,
                             name_ru=name_ru,
                             goal_teachers=goal_teachers,
                             emoji=emoji)
    return output


@app.route("/profiles/<id_teacher>/")
def profile(id_teacher):
    id_teacher = int(id_teacher)
    teacher = Teachers(id_teacher)
    name = teacher.name
    about = teacher.about
    rating = teacher.rating
    picture = teacher.picture
    price = teacher.price
    goals = teacher.goals
    free_time = teacher.get_free_time()
    week = teacher.week

    output = render_template("profile.html",
                             name=name,
                             about=about,
                             rating=rating,
                             picture=picture,
                             price=price,
                             goals=goals,
                             free_time=free_time,
                             week=week,
                             id=id_teacher)

    return output


@app.route("/request/")
def request():
    form = RequestForm()
    output = render_template("request.html",
                             form=form)
    return output


@app.route("/request_done/", methods=["GET", "POST"])
def request_done():
    form = RequestForm()
    client_name = form.name.data
    client_phone = form.phone.data
    client_goal = form.goal.data
    client_time = form.time.data
    form.save_request_data()
    output = render_template("request_done.html",
                             client_name=client_name,
                             client_phone=client_phone,
                             client_goal=client_goal,
                             client_time=client_time)
    return output


@app.route("/booking/<id_teacher>/<day>/<time>/")
def booking(id_teacher, day, time):
    form = BookingForm()
    id_teacher = int(id_teacher)
    teacher = Teachers(id_teacher)
    name = teacher.name
    week = teacher.week
    picture = teacher.picture
    output = render_template("booking.html",
                             id=id_teacher,
                             day=day,
                             time=time,
                             name=name,
                             week=week,
                             form=form,
                             picture=picture)
    return output


@app.route("/booking_done/", methods=["GET", "POST"])
def booking_done():
    form = BookingForm()
    client_name = form.name.data
    client_phone = form.phone.data
    client_day = form.day.data
    client_time = form.time.data
    form.save_booking_data()
    output = render_template("booking_done.html",
                             client_name=client_name,
                             client_phone=client_phone,
                             client_day=client_day,
                             client_time=client_time)
    return output


@app.errorhandler(500)
def internal_error(error):
    output = render_template("500.html"), 500
    return output


@app.errorhandler(404)
def internal_error(error):
    output = render_template("404.html"), 404
    return output


if __name__ == "__main__":
    app.run()

