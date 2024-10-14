from flask import Flask, url_for
from lab1 import lab1
from lab2 import lab2

app=Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)

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


  

