from flask import Blueprint, render_template,redirect, request,url_for

lab9=Blueprint('lab9',__name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('/lab9/index.html')
    
    username = request.form.get('username')
    return redirect(f'/lab9/age/{username}')
    
@lab9.route('/lab9/age/<username>', methods=['GET', 'POST'])
def age(username):
    if request.method == 'GET':
        return render_template('lab9/age.html', username=username)
    
    age = request.form.get('age')
    return redirect(f'/lab9/gender/{username}/{age}')

@lab9.route('/lab9/gender/<username>/<age>', methods=['GET', 'POST'])
def gender(username, age):
    if request.method == 'POST':
        gender = request.form.get('gender')
        return redirect(f'/lab9/preference/{username}/{age}/{gender}')
    
    return render_template('lab9/gender.html', username=username, age=age)

@lab9.route('/lab9/preference/<username>/<age>/<gender>', methods=['GET', 'POST'])
def preference(username, age, gender):
    if request.method == 'POST':
        preference = request.form.get('preference')
        return redirect(f'/lab9/final/{username}/{age}/{gender}/{preference}')
    
    return render_template('lab9/preference.html', username=username, age=age, gender=gender)

@lab9.route('/lab9/final/<username>/<age>/<gender>/<preference>')
def final(username, age, gender, preference):
    age = int(age)
    if gender == 'male':
        if age < 18:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы ты быстро вырос, становился умным и смелым, как настоящий герой!"
        else:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы все мечты сбывались, а каждый день приносил радость!"   
    else:
        if age < 18:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы ты быстро выросла, была любознательной и никогда не боялась мечтать!"
        else:
            greeting = f"Поздравляю тебя, {username}, желаю, чтобы все мечты сбывались, а каждый день приносил радость!" 

  
    if preference == 'вкусное':
        if age < 18:
            gift = "Вот тебе подарок — мешочек конфет."
            image = url_for('static', filename='/lab9/мешок_конфет.jpg')  
        else:
            gift = "Вот тебе подарок — коробка шоколадных конфет."
            image = url_for('static', filename='/lab9/коробка_конфет.jpg') 
    else:
        if age < 18:
            gift = "Вот тебе подарок — красивый букет."
            image = url_for('static', filename='/lab9/цветы.jpg')  
        else:
            gift = "Вот тебе подарок — сертификат на покупку."
            image = url_for('static', filename='/lab9/сертификат.jpg') 

    return render_template('lab9/final.html', greeting=greeting, gift=gift, image=image)