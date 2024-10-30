from flask import Blueprint, url_for, redirect, render_template, request
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
    {'login':'alex','password':'123'},
    {'login':'bob','password':'555'},
    {'login':'kate','password':'694'},
    {'login':'jon','password':'477'},
    {'login':'kot','password':'304'},
]

@lab4.route('/lab4/login', methods=['POST','GET'])
def login():
    if request.method=='GET':
       return render_template('lab4/login.html',authorized=False)
    login=request.form.get('login')
    password=request.form.get('password')

    for user in users:
        if login==user['login'] and password==user['password']:
            return render_template('lab4/login.html',login=login,authorize=True)
        
    error='Неверный логин и/или пароль'
    return render_template('lab4/login.html',error=error,authorized=False)