from flask import Blueprint, url_for, redirect, render_template
lab2=Blueprint('lab2',__name__)

@lab2.route("/lab2/a/")
def a():
    return f''' 
    со слешем <br>
    <a href="/">Главное меню</a>
    '''

@lab2.route("/lab2/a")
def a2():
    return f''' 
    без слеша <br>
    <a href="/">Главное меню</a>
    '''

flower_list=['роза', 'тюльпан', 'незабудка', 'ромашка']

@lab2.route("/lab2/flowers/<int:flower_id>")
def flowers(flower_id):
    if flower_id >= len (flower_list):
        return "такого цветка нет", 404
    else:
        return f'''
    <!doctype html>
        <html>
            <body>
                <p>Под индексом {flower_id} записан цветок: {flower_list[flower_id]}</p>
                <p><a href="/lab2/kol_flowers">Список всех цветов</a></p>
                <a href="/">Главное меню</a>
            </body>
        </html>   
    '''  

@lab2.route("/lab2/add_flower/")
def not_name():
    return f'''Вы не задали имя цветка<br>
        <a href="/">Главное меню</a>''', 400


@lab2.route("/lab2/add_flower/<name>")
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
            <a href="/">Главное меню</a>
        </body>
    </html>   
''' 

@lab2.route('/lab2/kol_flowers')
def kol_flower():
    flower_string=', '.join(flower_list)
    if flower_list!=[]:
        return f'''
        <!doctype html>
            <html>
                <body>
                    <p>Все цветы: {flower_string} </p>
                    <p>Всего цветов: {len(flower_list)} </p>
                    <a href="/">Главное меню</a>
                </body>
            </html>   
        ''' 
    else:
        return 'Нет доступных цветов'

@lab2.route('/lab2/delet_flower')
def delet_flower():
    global flower_list
    flower_list=[]
    return f'''
    <!doctype html>
        <html>
            <body>
                <p>Cписок очищен</p>
                <p>Всего цветов: {len(flower_list)} </p>
                <p><a href="{url_for('lab2.kol_flower')}">Показать все цветы</a></p>
                <a href="/">Главное меню</a>
            </body>
        </html>   
    ''' 

@lab2.route("/lab2/example")
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
    return render_template("/lab2/example.html", name=name, 
                                number_lab=number_lab,
                                number_course=number_course,
                                group=group, fruits=fruits)  

@lab2.route("/lab2/")
def lab_2():
    return render_template("/lab2/lab2.html")

@lab2.route("/lab2/filters")
def filters():
    phrase="О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template("/lab2/filter.html", phrase=phrase)

@lab2.route("/lab2/calc/<int:a>/<int:b>")
def calc(a,b):
    return render_template("/lab2/calc.html",a=a,b=b)

@lab2.route("/lab2/calc/")
def calc_1():
    return redirect("/lab2/calc/1/1")

@lab2.route("/lab2/calc/<int:a>")
def calc_2(a):
    return redirect(f"/lab2/calc/{a}/1")

@lab2.route("/lab2/books")
def book():
    books=[
        {'name': 'Бег на вымирание', 'avtor': 'Пожарская Полина', 'genre': 'Юмористические произведения', 'number_of_pages': 22},
        {'name': 'Сова летит на север', 'avtor': 'Суханов Сергей Сергеевич', 'genre': 'Историческая проза', 'number_of_pages': 77},
        {'name': 'Человек с разрушенных холмов', 'avtor': 'Ламур Луис', 'genre': 'Вестерны', 'number_of_pages': 53},
        {'name': 'Тайны морских катастроф', 'avtor': 'Скрягин Лев Николаевич', 'genre': 'Морские приключения', 'number_of_pages': 99},
        {'name': 'История великих путешествий. Том 3. Путешественники XIX века', 'avtor': 'Верн Жюль Габриэль', 'genre': 'Путешествия и география', 'number_of_pages': 110},
        {'name': 'Ядерный будильник', 'avtor': 'Гайдуков Сергей Викторович', 'genre': 'Боевики', 'number_of_pages': 95},
        {'name': 'Ликвидация', 'avtor': 'Бондаренко Вячеслав Васильевич', 'genre': 'Криминальные детективы', 'number_of_pages': 122},
        {'name': 'Весь мир театр', 'avtor': 'Акунин Борис "Чхартишвили Григорий Шалвович"', 'genre': 'Исторические детективы', 'number_of_pages': 84},
        {'name': 'Приключения Незнайки и его друзей', 'avtor': 'Носов Николай Николаевич', 'genre': 'Детская проза', 'number_of_pages': 79},
        {'name': 'Мальчик у моря', 'avtor': 'Дубов Николай Иванович', 'genre': 'Детская проза', 'number_of_pages': 86}]
    return render_template("/lab2/book.html", books=books)  


@lab2.route("/lab2/berries")
def berries():
    berries_list = [
        {"name": "Брусника", "image": url_for("static", filename="/lab2/брусника.jpg"),
         "description": "Кисло-сладкая ягода, ближайшая родственница клюквы и черники." 
            " Это дикорастущее растение произрастает преимущественно в холодном климате и высоко ценится за"
            "свои вкусовые и целебные свойства. Сегодня эту ягоду можно выращивать в обычных условиях,"
            "высаживая сорта, выведенные отечественными и зарубежными селекционерами."
            " Брусника — вечнозелёный кустарник небольшой высоты с кисло-сладкими ягодами."},
        {"name": "Малина", "image": url_for("static", filename="/lab2/малина.jpg"), 
         "description": "Плодовая культура, выращиваемая во многих странах мира с умеренным климатом." 
            "Главное в малине – ее ягоды: душистые, сладкие и очень полезные. Ягода малины является сложным плодом, образованным из" 
            "сросшихся между собой небольших сочных плодов-костянок. Цвет ягод малины может быть розовым, ярко-красным, «малиновым»,"
            "и даже желтым или черным, как у ежевики"},
        {"name": "Арбуз","image": url_for("static", filename="/lab2/арбуз.jpg"),
         "description": "Плод арбуза — сочная многосемянная тыквина с гладкой поверхностью. У разных сортов он имеет различную форму:"
            " круглую, вытянутую, цилиндрическую. Окраска плода может быть белёсой, зелёной, жёлтой с полосками или пятнами, почти чёрной."
            "Мякоть бывает малиновой, оранжевой, красной, розово-оранжевой, розовой, жёлтой, белой."},
        {"name": "Голубика","image": url_for("static", filename="/lab2/голубика.jpg"),
         "description": "Голубика обыкновенная представляет собой многолетник и выглядит как разветвленный кустарник, вырастающий до 40-60 см"
            " (в естественной среде) или 70-100 см (в садовых формах).Плод – сочная ягода, окраска кожицы от светло-голубой до почти чёрной,"
            " часто с восковым налётом, диаметром до 2,5 см. Плоды округлые или сплюснутые, с сохраняющейся чашечкой. Растение эндозоохорное."
            "Вкус плодов кисло-сладкий или сладкий, мякоть плотная, часто неокрашенная. "},
        {"name": "Гранат", "image": url_for("static", filename="/lab2/гранат.jpg"),
         "description": "Род кустарников и небольших деревьев семейства дербенниковых. Плоды граната обычно размером с большой апельсин или грейпфрут"
            ", с толстой кожистой кожурой. Обычно сорта, встречающиеся в наших магазинах, имеют кожуру от темно-красной до красновато-коричневой,"
            " но существуют также гранаты, окрашенные внешне в оранжевый, желтый, розовый и кремовый цвет. "},
        {"name": "Ежевика","image": url_for("static", filename="/lab2/ежевика.jpg"),
         "description": "Ежевика представляют собой стелющийся кустарник или полукустарник, плети которого вырастают в длину до 1,5-2 м."
           "Близкая родственница малины, морошки, костяники и княженики: с точки зрения науки все виды этих растений относятся к одному и "
           "тому же роду - Rubus. Ягоды ежевики кисловато-сладкие, тёмного с сизым оттенком цвета."}]
    return render_template("/lab2/berries.html",berries_list=berries_list)
