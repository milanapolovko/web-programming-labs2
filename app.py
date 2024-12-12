import os
from os import path
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from db import db

from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8

app=Flask(__name__)

app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)


app.config['SECRET_KEY']= os.environ.get('SECRET_KEY','секретно-секретный секрет')
app.config['DB_TYPE']= os.getenv('DB_TYPE','postgres')

if app.config['DB_TYPE']=='postgres':
    db_name='milana_polovko_orm'
    db_user='milana_polovko_orm'
    db_password='123'
    host_ip='127.0.0.1'
    host_port=5432
    options="-c client_encoding=utf8"

    app.config['SQLALCHEMY_DATABASE_URI']=f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path=path.dirname(path.realpath(__file__))
    db_path=path.join(dir_path,"milana_polovko_orm.db")
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///{db_path}'

db.init_app(app)

@app.route("/")
def title():
    return """<!doctype html>
        <html>
            <head>
                <title>НГТУ,ФБ,Лабораторные работы</title>
            </head> 
            <body>
            <header>
                НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных
            </header>
            <main>
                <ol>
                    <li><a href="/lab1/">Первая лабораторная работа</a></li>
                    <li><a href="/lab2/">Вторая лабораторная работа</a></li>
                    <li><a href="/lab3/">Третья лабораторная работа</a></li>
                    <li><a href="/lab4/">Четвертая лабораторная работа</a></li>
                    <li><a href="/lab5/">Пятая лабораторная работа</a></li>
                    <li><a href="/lab6/">Шестая лабораторная работа</a></li>
                    <li><a href="/lab7/">Седьмая лабораторная работа</a></li>
                    <li><a href="/lab8/">Восьмая лабораторная работа</a></li>
                </ol>
            </main>
            <footer>
                Половко Милана Андреевна, ФБИ-21, 3 курс, 2024
            </footer>
            </body>
        </html>"""

@app.route("/index")
def index():
    return """<!doctype html>
        <html>
            <head>
                <title>НГТУ,ФБ,Лабораторные работы</title>
            </head> 
            <body>
            <header>
                НГТУ, ФБ, WEB-программирование,часть 2. Список лабораторных
            </header>
            <main>
                <ol>
                    <li><a href="/lab1/">Первая лабораторная работа</a></li>
                </ol>
            </main>
            <footer>
                Половко Милана Андреевна, ФБИ-21, 3 курс, 2024
            </footer>
            </body>
        </html>"""


@app.errorhandler(404)
def not_found(err):
    path=url_for("static", filename="404.jpg")
    path2=url_for("static", filename="error.css")
    return '''
<!doctype html>
<html>
    <head>
        <link rel="stylesheet" href="''' + path2 + '''">
    </head>
    <body>
        <img src="''' + path + '''">
        <div>
            <h1>Упс! Страница не найдена.</h1>
            <h2>К сожалению, мы не можем найти запрашиваемую вами страницу</h2>
        </div>
    </body>
</html>
''', 404

    
@app.errorhandler(500)
def server_error(err):
    return '''
<!doctype html>
<html>
    <body> 
        <h1>Внутренняя ошибка сервера<h1>
        <i>Сервер обнаружил внутреннюю ошибку и не смог выполнить ваш запрос. 
        Либо сервер перегружен, либо в приложении есть ошибка.</i>
    </body>
</html>
''', 500


  

