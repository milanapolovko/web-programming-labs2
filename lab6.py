from flask import Blueprint, redirect, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
from os import path

lab6=Blueprint('lab6',__name__)

offices=[]
for i in range(1,11):
    offices.append({"number": i, "tenant": "", "price": 1706+i%7})

@lab6.route('/lab6/')
def main():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data=request.json
    id= data['id']

    login=session.get('login')
    if not login:
        return {
            'jsonrpc':'2.0',
            'error':{
                'code': 1,
                'message':'Unauthorized'
            },
            'id': id   
        }
    
    if data['method']=='info':
        cost = sum(office['price'] for office in offices 
                   if office['tenant'] == login)
        return {
            'jsonrpc': '2.0',
            'result': offices,
            'id': id,
            'sum': cost
        }
    if data ['method'] == 'booking':
        office_number = data['params']
        for office in offices:
            if office['number']==office_number:
                if office['tenant'] !='':
                    return{
                        'jsonrpc': '2.0',
                        'error':{
                            'code': 2,
                            'message': 'Already booked'
                        },
                        'id': id
                    }
                office['tenant'] = login
                return{
                    'jsonrpc': '2.0',
                    'result':'success',
                    'id': id
                }
   
    if data['method']=='cancellation':
        office_number=data['params']
        for office in offices:
            if office['number']==office_number:
                if office['tenant'] =='':
                    return{
                        'jsonrpc': '2.0',
                        'error':{
                            'code': 3,
                            'message': 'not booked'
                        },
                        'id': id
                    }
                if office['tenant'] != login:
                    return{
                        'jsonrpc': '2.0',
                        'error':{
                            'code': 4,
                            'message': 'not booked'
                        },
                        'id': id
                    }
            
                office['tenant'] =''
                return{
                    'jsonrpc': '2.0',
                    'result':'success',
                    'id': id
                }

    return{
        'jsonrpc': '2.0',
        'error':{
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }