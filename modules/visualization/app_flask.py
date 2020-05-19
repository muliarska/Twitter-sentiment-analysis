"""Represents an application"""
from flask import Flask, render_template, request, redirect
from modules.program_process.functional import Functional
from modules.visualization.dashboard import create_dash_app


FLASK_APP = Flask(__name__)
MANAGER = Functional()
INFO = {}
COUNTER = 1


@FLASK_APP.route("/", methods=['GET', 'POST'])
def index():
    """Home page of the application"""
    return render_template('index.html')


@FLASK_APP.route("/choose", methods=['POST'])
def choose():
    """Page to choose for what time user wants
     to get statistics"""
    INFO['username'] = request.form['username']
    MANAGER.set_nickname(INFO['username'])
    return render_template('choose.html')


@FLASK_APP.route("/day", methods=['POST', 'GET'])
def days():
    """Page to choose a day for statistics"""
    days_list = MANAGER.available_days()
    if days_list == []:
        return render_template('exception.html')
    return render_template('days.html', days=days_list)


@FLASK_APP.route("/app_type", methods=['POST'])
def application_type():
    """Page to choose the type of statistics"""
    try:
        day = request.form.get('days')
        INFO['day'] = day
        print(INFO['day'])

    except ValueError:
        INFO['day'] = None

    return render_template('app_type.html')


@FLASK_APP.route("/emotion", methods=['POST', 'GET'])
def emotions():
    """Page to choose an emotion"""
    return render_template('emotions.html')


@FLASK_APP.route("/result", methods=['POST', 'GET'])
def result():
    """Result page with statistics"""
    try:
        emotion = request.form.get('emotions')
        INFO['emotion'] = emotion
        print(INFO['emotion'])
    except ValueError:
        INFO['emotion'] = None

    app_type = "many"
    day = None
    emotion = None
    nick = MANAGER.nickname

    if INFO["day"] is not None:
        day = INFO["day"]
    if INFO["emotion"] is not None:
        app_type = "specific"
        emotion = INFO["emotion"]
    global COUNTER

    try:
        create_dash_app(FLASK_APP, COUNTER, MANAGER, app_type, nick, day, emotion)
        COUNTER += 1
        return redirect('/statistic{}'.format(str(COUNTER - 1)))
    except AttributeError:
        return render_template('exception.html')
