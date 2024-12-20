from flask import Blueprint, redirect, render_template, request, session
lab4=Blueprint('lab4',__name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')

@lab4.route('/lab4/mult-form')
def mult_form():
    return render_template('lab4/mult-form.html')

@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')

@lab4.route('/lab4/degree-form')
def degree_form():
    return render_template('lab4/degree-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1=request.form.get('x1')
    x2=request.form.get('x2')
    if x1=='' or x2=='':
        return render_template('lab4/div.html',error='Оба поля должны быть заполнены!')
    if x2=='0':
        return render_template('lab4/div.html',error='Второе число не должно равняться 0!')
    x1=int(x1)
    x2=int(x2)
    result=x1/x2
    return render_template('lab4/div.html', x1=x1,x2=x2,result=result)

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1=request.form.get('x1')
    x2=request.form.get('x2')
    if x1=='':
        x1=0
    if x2=='': 
        x2=0   
    x1=int(x1)
    x2=int(x2)
    result=x1+x2
    return render_template('lab4/sum.html', x1=x1,x2=x2,result=result)

@lab4.route('/lab4/mult', methods=['POST'])
def mult():
    x1=request.form.get('x1')
    x2=request.form.get('x2')
    if x1=='':
        x1='1'
    if x2=='': 
        x2='1'   
    x1=int(x1)
    x2=int(x2)
    result=x1*x2
    return render_template('lab4/mult.html', x1=x1,x2=x2,result=result)

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1=request.form.get('x1')
    x2=request.form.get('x2')
    if x1=='' or x2=='':
        return render_template('lab4/sub.html',error='Оба поля должны быть заполнены!')
    x1=int(x1)
    x2=int(x2)
    result=x1-x2
    return render_template('lab4/sub.html', x1=x1,x2=x2,result=result)

@lab4.route('/lab4/degree', methods=['POST'])
def degree():
    x1=request.form.get('x1')
    x2=request.form.get('x2')
    if x1=='' or x2=='':
        return render_template('lab4/degree.html',error='Оба поля должны быть заполнены!')
    if x2=='0' or x1=='0':
        return render_template('lab4/degree.html',error='Поле не должно равняться 0!')
    x1=int(x1)
    x2=int(x2)
    result=x1**x2
    return render_template('lab4/degree.html', x1=x1,x2=x2,result=result)

tree_count=0

@lab4.route('/lab4/tree', methods=['POST','GET'])
def tree():
    global tree_count
    if request.method=='GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    operation=request.form.get('operation')
    
    if operation=='cut':
        tree_count-=1
    elif operation=='plant':
        tree_count+=1
    if tree_count<0: 
        tree_count=0
    return redirect('/lab4/tree')

users=[
    {'login': 'alex', 'password': '123', 'name': 'Александр', 'sex': 'М'},
    {'login': 'bob', 'password': '555', 'name': 'Боб', 'sex': 'М'},
    {'login': 'kate', 'password': '694', 'name': 'Катерина', 'sex': 'Ж'},
    {'login': 'jon', 'password': '477', 'name': 'Иван Иванов', 'sex': 'М'},
    {'login': 'kot', 'password': '304', 'name': 'Василий Васильевич', 'sex': 'М'},
]


@lab4.route('/lab4/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
        if 'login' in session:
           authorized=True
           name=session['name']
        else:
            authorized=False
            name=''
        return render_template('lab4/login.html',authorized=authorized,name=name)
    
    login=request.form.get('login')
    password=request.form.get('password')

    if login=='':
        error='Не введён логин'
        return render_template('lab4/login.html',error=error,authorized=False, login=login)
    
    if password=='':
        error='Не введён пароль'
        return render_template('lab4/login.html',error=error,authorized=False, login=login)
    
    for user in users:
        if login==user['login'] and password==user['password']:
            session['login']=login
            session['name'] = user['name'] 
            return redirect('/lab4/login')
        
    error='Неверный логин и/или пароль'
    return render_template('lab4/login.html',error=error,authorized=False,login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
   session.pop('login',None)
   return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET','POST'])
def fridge():
    images = []
    if request.method=='GET':
         return render_template('lab4/fridge.html',temperature=None)
    temperature = request.form.get('temperature')
    if temperature=='':
        return 'Ошибка: не задана температура'
    else:
        temperature = int(temperature)
        if temperature < -12:
            return 'Не удалось установить температуру — слишком низкое значение'
        elif temperature > -1:
            return 'Не удалось установить температуру — слишком высокое значение'
        elif -12 <= temperature <= -9:
            images.extend(['<img src="/static/lab4/снежинка.png" width="20" height="20">' for _ in range(3)])
        elif -8 <= temperature <= -5:
            images.extend(['<img src="/static/lab4/снежинка.png" width="20" height="20">' for _ in range(2)])
        elif -4 <= temperature <= -1:
            images.extend('<img src="/static/lab4/снежинка.png" width="20" height="20">')
    
    images_html = ''.join(images)
    
    return f'Установлена температура: {temperature}°С {images_html}'

prices = {
    "ячмень": 12345,
    "овёс": 8522,
    "пшеница": 8722,
    "рожь": 14111
}

weight=0
@lab4.route('/lab4/order', methods=['GET','POST'])
def order():
    global weight
    total_price = None
    discount = None
    grain = None
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')

        if weight=='':
            return render_template('lab4/order.html', error='Ошибка: вес не указан')
            
        else:
            weight = int(weight)
            if weight <= 0:
                return render_template('lab4/order.html', error='Ошибка: вес должен быть больше 0')
            elif weight > 500:
                return render_template('lab4/order.html', error='Ошибка: такого объёма сейчас нет в наличии')
        
        total_price = prices.get(grain) * weight

        discount = 0
        if weight > 50:
            discount = total_price * 0.10
            total_price -= discount
            
    return render_template('lab4/order.html', grain=grain, weight=weight, total_price=total_price, discount=discount)