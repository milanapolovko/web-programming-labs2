from flask import Flask, url_for, redirect, render_template
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
                <h2>Список роутов</h2>
                <p><a href="/index">Индекс</a></p>
                <p><a href="/lab1/web">Web-сервер</a></p>
                <p><a href="/lab1/author">Автор</a></p>
                <p><a href="/lab1/oak">Дуб</a></p>
                <p><a href="/lab1/counter">Счетчик</a></p>
                <p><a href="/lab1/info">Info</a></p>
                <p><a href="/lab1/created">Что-то создано</a></p>
                <p><a href="/lab1/400">Ошибка 400</a></p>
                <p><a href="/lab1/401">Ошибка 401</a></p>
                <p><a href="/lab1/402">Ошибка 402</a></p>
                <p><a href="/lab1/403">Ошибка 403</a></p>
                <p><a href="/lab1/405">Ошибка 405</a></p>
                <p><a href="/lab1/418">Ошибка 418</a></p>
                <p><a href="/lab1/reset">Очистка счетчика</a></p>
                <p><a href="/lab1/error">Ошибка 500</a></p>
                <p><a href="/lab1/text">Господин из Сан-Франциско</a></p>
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
            'Content-Type': 'text/plain; charset=utf-8'
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
def unauthorized():
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

@app.route('/lab1/error')
def trigger_error():
    result=1/0
    return str(result)
    
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

@app.route('/lab1/text')
def text():
    path=url_for("static", filename="gospodin-iz-san-frantsisko.jpg")
    path2=url_for("static", filename="3357eb3351df22d8.jpg")
    return '''
<!doctype html>
<html>
    <style>
        .one{
            width: 20%;
            float:right;
            margin: 5px 30px 3px 20px;
        }
        .two{
            width: 40%;
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        p{
            text-indent: 30px;
            text-align: justify;
            line-height: 1.5;
            margin: 0 30px;
            font-size:18px;
        }
    </style>
    <body>
        <img src="''' + path + '''" class="one">
        <p>Господин из Сан-Франциско – имени его ни в Неаполе, ни на Капри никто не запомнил – ехал в Старый Свет на целых два года, с женой и дочерью, единственно ради развлечения.</p>
        <p>Он был твердо уверен, что имеет полное право на отдых, на удовольствие, на путешествие долгое и комфортабельное, и мало ли еще на что. Для такой уверенности у него был тот резон, 
        что, во-первых, он был богат, а во-вторых, только что приступал к жизни, несмотря на свои пятьдесят восемь лет. До этой поры он не жил, а лишь существовал, правда очень недурно, но 
        все же возлагая все надежды на будущее. Он работал не покладая рук, – китайцы, которых он выписывал к себе на работы целыми тысячами, хорошо знали, что это значит! – и, наконец, 
        увидел, что сделано уже много, что он почти сравнялся с теми, кого некогда взял себе за образец, и решил передохнуть. Люди, к которым принадлежал он, имели обычай начинать наслаждения 
        жизнью с поездки в Европу, в Индию, в Египет. Положил и он поступить так же. Конечно, он хотел вознаградить за годы труда прежде всего себя; однако рад был и за жену с дочерью. 
        Жена его никогда не отличалась особой впечатлительностью, но ведь все пожилые американки страстные путешественницы. А что до дочери, девушки на возрасте и слегка болезненной, то
        для нее путешествие было прямо необходимо – не говоря уже о пользе для здоровья, разве не бывает в путешествиях счастливых встреч? Тут иной раз сидишь за столом или рассматриваешь 
        фрески рядом с миллиардером.</p>
        <p>Маршрут был выработан господином из Сан-Франциско обширный. В декабре и январе он надеялся наслаждаться солнцем Южной Италии, памятниками древности, тарантеллой, серенадами 
        бродячих певцов и тем, что люди в его годы чувствуют особенно тонко, – любовью молоденьких неаполитанок, пусть даже и не совсем бескорыстной, карнавал он думал провести в Ницце, 
        в Монте-Карло, куда в эту пору стекается самое отборное общество, – то самое, от которого зависят все блага цивилизации: и фасон смокингов, и прочность тронов, и объявление войн, 
        и благосостояние отелей, – где одни с азартом предаются автомобильным и парусным гонкам, другие рулетке, третьи тому, что принято называть флиртом, а четвертые – стрельбе в голубей, 
        которые очень красиво взвиваются из садков над изумрудным газоном, на фоне моря цвета незабудок, и тотчас же стукаются белыми комочками о землю; начало марта он хотел посвятить Флоренции, 
        к страстям господним приехать в Рим, чтобы слушать там Miserere; входили в его планы и Венеция, и Париж, и бой быков в Севилье, и купанье на английских островах, и Афины, и Константинополь,
        и Палестина, и Египет, и даже Япония, – разумеется, уже на обратном пути… И все пошло сперва отлично.</p>
        <img src="''' + path2 + '''" class="two">
        <p>Был конец ноября, до самого Гибралтара пришлось плыть то в ледяной мгле, то среди бури с мокрым снегом; но плыли вполне благополучно. Пассажиров было много, пароход — знаменитая
        «Атлантида» — был похож на громадный отель со всеми удобствами, — с ночным баром, с восточными банями, с собственной газетой, — и жизнь на нем протекала весьма размеренно: вставали рано, 
        при трубных звуках, резко раздававшихся по коридорам еще в тот сумрачный час, когда так медленно и неприветливо светало над серо-зеленой водяной пустыней, тяжело волновавшейся в тумане; 
        накинув фланелевые пижамы, пили кофе, шоколад, какао; затем садились в ванны, делали гимнастику, возбуждая аппетит и хорошее самочувствие, совершали дневные туалеты и шли к первому 
        завтраку; до одиннадцати часов полагалось бодро гулять по палубам, дыша холодной свежестью океана, или играть в шеффльборд и другие игры для нового возбуждения аппетита, 
        а в одиннадцать — подкрепляться бутербродами с бульоном; подкрепившись, с удовольствием читали газету и спокойно ждали второго завтрака, еще более питательного и разнообразного, 
        чем первый; следующие два часа посвящались отдыху; все палубы были заставлены тогда длинными камышовыми креслами, на которых путешественники лежали, укрывшись пледами, глядя на облачное 
        небо и на пенистые бугры, мелькавшие за бортом, или сладко задремывая; в пятом часу их, освеженных и повеселевших, поили крепким душистым чаем с печеньями; в семь повещали трубными 
        сигналами о том, что составляло главнейшую цель всего этого существования, венец его... И тут господин из Сан-Франциско спешил в свою богатую кабину — одеваться.</p>
    </body>
</html>
''', 200, {
            'X-Server':'Welcome to my page!',
            'X-Content-Length':'277',
            'Content-Language': 'en-CA , de-DE'
        }

@app.route('/lab2/a/')
def a():
    return 'со слешем'

@app.route('/lab2/a')
def a2():
    return 'без слеша'

flower_list=['роза', 'тюльпан', 'незабудка', 'ромашка']


@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len (flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    flower_list.append(name)
    return f'''
    <!doctype html>
    <html>
        <body>
        <h1>Добавлен новый цветок</h1>
        <p>Название нового цветка: {name} </p>
        <p>Всего цветов: {len(flower_list)} </p>
        <p>Полный список: {flower_list} </p>
        </body>
     </html>   
    ''' 
@app.route('/lab2/example')
def example():
    name='Половко Милана'
    number_lab='Лабораторная работа 2'
    number_course='3 курс'
    group='ФБИ-21'
    fruits=[
        {'name':'яблоки', 'price':100},
        {'name':'груши', 'price':120},
        {'name':'апельсины', 'price':80},
        {'name':'мандарины', 'price':95},
        {'name':'манго', 'price':321},]
    return render_template('example.html', name=name, 
                                number_lab=number_lab,
                                number_course=number_course,
                                group=group, fruits=fruits)  

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase="О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase=phrase)
