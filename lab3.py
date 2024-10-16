from flask import Blueprint, redirect, render_template, request, make_response
lab3=Blueprint('lab3',__name__)

@lab3.route('/lab3/')
def lab():
    name=request.cookies.get('name')
    age=request.cookies.get('age')
    name_color=request.cookies.get('name_color')
    return render_template("lab3/lab3.html", name=name,name_color=name_color,age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp=make_response(redirect('/lab3/'))
    resp.set_cookie('name','Alex', max_age=5)
    resp.set_cookie('age','20')
    resp.set_cookie('name_color','magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp=make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user=request.args.get('user')
    
    if user=='':
        errors['user']='Заполните поле!'
    
    age=request.args.get('age')
    if age=='':
        errors['age']='Заполните поле!'

    sex=request.args.get('sex')
    return render_template('lab3/form1.html', user=user,age=age,sex=sex, errors=errors )


@lab3.route('/lab3/order')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price=0
    drink=request.args.get('drink')
    if drink=='cofee':
        price=120
    elif drink=='black-tea':
        price=80
    else:
        price=70

    if request.args.get('milk')=='on':
        price+=30
    if request.args.get('sugar')=='on':
        price+=10
        
    return render_template('lab3/pay.html',price=price)


@lab3.route('/lab3/success')
def success():
    price=request.args.get('price')
    return render_template('lab3/success.html',price=price)

@lab3.route('/lab3/settings')
def settings():
    color=request.args.get('color')
    background_color=request.args.get('background_color')
    font_size=request.args.get('font_size')
    text_align=request.args.get('text_align')
    if (color or background_color or font_size or text_align):
        resp=make_response(redirect('/lab3/settings'))
        resp.set_cookie('color',color)
        resp.set_cookie('background_color',background_color)
        resp.set_cookie('font_size',font_size)
        resp.set_cookie('text_align',text_align)
        return resp
    
    color=request.cookies.get('color')
    background_color=request.cookies.get('background_color')
    font_size=request.cookies.get('font_size')
    text_align=request.cookies.get('text_align')
    resp=make_response(render_template('lab3/settings.html',color=color,background_color=background_color,text_align=text_align,font_size=font_size))
    return resp

@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    resp.delete_cookie('color')
    resp.delete_cookie('background_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('text_align')
    return resp

@lab3.route('/lab3/bilet')
def bilet():
    errors={} 
    price=0
    ticket_type=""
    passenger=request.args.get('passenger')
    polka=request.args.get('polka')
    linen=request.args.get('linen')
    baggage=request.args.get('baggage')
    age=request.args.get('age')
    from_=request.args.get('from_')
    where_=request.args.get('where_')
    date=request.args.get('date')
    belay=request.args.get('belay')
   
    if passenger=="":
        errors['passenger']='Заполните поле!'
    
    if age=="" or age is None:
        errors['age']='Заполните поле!'
    else:
        age = int(age)
        if age < 1 or age > 120:
            errors['age']='Возраст должен быть от 1 до 120 лет'

    if from_=='':
        errors['from_']='Заполните поле!'

    if where_=='':
        errors['where_']='Заполните поле!'
    if not errors:
        if date=='':
            errors['date']='Заполните поле!'

        if age>18:
            price=1000
            ticket_type='Взрослый билет' 
        else:
            price=700
            ticket_type='Десткий билет' 
        if polka =='down' or polka=='lower-side':
            price+=100
        if linen=='yes':
            price+=75
        if baggage=='baggage_yes':
            price+=250   
        if belay=='belay_yes':
            price+=150  

    return render_template('lab3/bilet.html',passenger=passenger,errors=errors,polka=polka,
                           linen=linen,baggage=baggage,age=age,from_=from_,
                           where_=where_,date=date,belay=belay,price=price,ticket_type=ticket_type)
