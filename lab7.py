from flask import Blueprint, redirect, render_template, request, session, current_app

lab7=Blueprint('lab7',__name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')

films=[
    {
        "title": "The Substance",
        "title_ru":"Субстанция",
        "year": 2024,
        "description":"Слава голливудской звезды Элизабет Спаркл осталась в прошлом,\
            хоть она всё ещё ведёт популярное фитнес-шоу на телевидении.\
            Когда её передачу собираются перезапустить с новой звездой, \
            Элизабет решает принять уникальный препарат «Субстанция». \
            Так на свет появляется молодая Сью.\
            Однако у совершенства есть своя цена, и расплата не заставит себя долго ждать."
    },
    {
        "title": "Intouchables",
        "title_ru":"1+1 ",
        "year": 2011,
        "description":"Пострадав в результате несчастного случая, \
            богатый аристократ Филипп нанимает в помощники человека, \
            который менее всего подходит для этой работы, – молодого жителя предместья Дрисса, \
            только что освободившегося из тюрьмы. Несмотря на то, что Филипп прикован к инвалидному\
            креслу, Дриссу удается привнести в размеренную жизнь аристократа дух приключений."
    },
    {
        "title": "Shutter Island",
        "title_ru":"Остров проклятых ",
        "year": 2009,
        "description":"Два американских судебных пристава отправляются на один из островов в штате Массачусетс,\
            чтобы расследовать исчезновение пациентки клиники для умалишенных преступников.\
            При проведении расследования им придется столкнуться с паутиной лжи, обрушившимся ураганом \
            и смертельным бунтом обитателей клиники."
    },
      {
        "title": "Moonrise Kingdom",
        "title_ru":"Королевство полной луны",
        "year": 2012,
        "description":"60-е годы XX века. Пара влюблённых подростков, живущих на острове в Новой Англии, \
            убегает из-под присмотра взрослых. Сэм Шакаски — бойскаут, сирота, от которого отказались\
            приемные родители, из-за своего непростого характера ставший изгоем среди других бойскаутов,\
            и Сьюзи Бишоп — замкнутая двенадцатилетняя неуравновешенная девочка, живущая мечтами \
            о волшебных мирах. После обнаружения пропажи местный шериф начинает расследование, \
            а вожатый лагеря бойскаутов организует поисковый отряд."
    },
      {
        "title": "Beoning",
        "title_ru":"Пылающий",
        "year": 2018,
        "description":"Молодой человек Ли Джон-су, ничем особо не занятый, встречает соседскую девушку Хэ-ми,\
            с которой они вместе росли. Та собирается съездить в Африку и просит нового знакомого присмотреть \
            за её кошкой, а возвращается из поездки не одна, а с состоятельным молодым человеком Беном. \
            Однажды парочка приходит к Джон-су, и Бен рассказывает о своем тайном хобби. С этого момента\
            Джон-су лишается покоя, и его начинает одолевать предчувствие страшного."
    },

]

@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):  
    if id >= len(films):
         return {
            'jsonrpc': '2.0',
            'error': {
                'code': 404,
                'message': 'Film not found'
            },}
    return films[id]

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id): 
    if id >= len(films):
         return {
            'jsonrpc': '2.0',
            'error': {
                'code': 404,
                'message': 'Film not found'
            },}
    del films[id]
    return '', 204

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id): 
    film=request.get_json()
    if id >= len(films):
         return {
            'jsonrpc': '2.0',
            'error': {
                'code': 404,
                'message': 'Film not found'
            },}
    if film['description']=='':
        return {'description': 'Заполните описание'},400
    films[id]=film
    return films[id]


@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film(): 
    film=request.get_json()
    if film['description']=='':
        return {'description': 'Заполните описание'},400
    films.append(film)
    return ({'id': len(films) - 1})
        