from flask import Flask, url_for, redirect
app=Flask(__name__)

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
                    <li><a href="/lab1">Первая лабораторная работа</a></li>
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
                    <li><a href="/lab1">Первая лабораторная работа</a></li>
                </ol>
            </main>
            <footer>
                Половко Милана Андреевна, ФБИ-21, 3 курс, 2024
            </footer>
            </body>
        </html>"""

@app.route("/lab1")
def lab1():
    return """<!doctype html>
        <html>
            <head>
                <title>Лабораторная 1</title>
            </head> 
            <body>
                Flask — фреймворк для создания веб-приложений на языке
                программирования Python, использующий набор инструментов
                Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
                называемых микрофреймворков — минималистичных каркасов
                веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
                <p><a href="/">Главное меню</a></p>
            </body>
        </html>"""

@app.route("/lab1/web")
def web():
    return """<!doctype html>
        <html> 
            <body>
                <h1>web-сервер на flask</h1>
                <a href="/lab1/author">author</a>
            </body>
        </html>""", 200, {
            'X-Server':'sample',
            'Content-Type': 'text/html; charset=utf-8'
        }


@app.route("/lab1/author")
def author():
    name="Половко Милана Андреевна"
    group="ФБИ-21"
    faculty="ФБ"

    return """<!doctype html>
        <html>
            <body>
                <p> Студент: """ + name + """</p>
                <p> Группа: """ + group + """</p>
                <p> Факультет: """ + faculty + """</p>
                <a href="/lab1/web">web</a>
            </body>
        </html>"""

@app.route('/lab1/oak')
def oak():
    path=url_for("static", filename="oak.jpg")
    path2=url_for("static", filename="lab1.css")
    return '''
<!doctype html>
<html> 
    <head>
        <link rel="stylesheet" href="''' + path2 + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + path + '''">
    </body>
</html>
'''

count=0

@app.route('/lab1/counter')
def conter():
    global count
    count+=1
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили: ''' + str(count) + '''
        <p><a href="/lab1/reset">Очистка счетчика</a></p>
    </body>
</html>
'''

@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")

@app.route('/lab1/created')
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i> что-то создано...</i></div>
    </body>
</html>
''', 201

@app.errorhandler(404)
def not_found(err):
    return "нет такой страницы", 404

@app.route('/lab1/400')
def bad_request():
    return '''
<!doctype html>
<html>
    <body>
        <i>неправильный, некорректный запрос</i>
    </body>
</html>
''', 400

@app.route('/lab1/401')
def bad_request():
    return '''
<!doctype html>
<html>
    <body>
        <i>пользователь не авторизован</i>
    </body>
</html>
''', 401

@app.route('/lab1/402')
def payment_required():
    return '''
<!doctype html>
<html>
    <body>
        <i>необходима оплата</i>
    </body>
</html>
''', 402

@app.route('/lab1/403')
def forbidden ():
    return '''
<!doctype html>
<html>
    <body>
        <i>доступ запрещен</i>
    </body>
</html>
''', 403

@app.route('/lab1/405')
def method_not_allowed():
    return '''
<!doctype html>
<html>
    <body>
        <i>метод не поддерживается</i>
    </body>
</html>
''', 405

@app.route('/lab1/418')
def im_a_teapot():
    return '''
<!doctype html>
<html>
    <body>
        <i>я — чайник</i>
    </body>
</html>
''', 418

@app.route('/lab1/reset')
def reset():
    global count
    count=0
    return '''
<!doctype html>
<html>
    <body>
        Счетчик очищен: ''' + str(count) + '''
        <p><a href="/lab1/counter">Вернуться к счетчику</a></p>
    </body>
</html>
'''