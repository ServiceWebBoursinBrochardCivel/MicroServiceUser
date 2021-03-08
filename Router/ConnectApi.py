from flask import Blueprint,request,jsonify
from Models.user import User
from TokenHandler.jwtService import JwtService
from DatabaseManager.connection import db_connection

connect_api = Blueprint('connect_api',__name__)

@connect_api.route('/login',methods=['POST'])
def login():
    conn = db_connection()
    cursor= conn.cursor()
    user = None

    if request.method =='POST':
        data = request.get_json()
        mail = data['mail']
        password = data['password']
        sql = """SELECT id, pseudo, mail, password FROM user WHERE mail =? and password =?"""
        cursor.execute(sql,(mail,password))
        row = cursor.fetchone()
        if row is not None :
            user = User(row[0], row[1], row[2], row[3])
            token = JwtService().create(user)
            return token, 200
        cursor.close()
        conn.close()
        return "Can't authenticate", 401

@connect_api.route('/verify', methods=['POST'])
def check():
    if request.method == 'POST' :
        data = request.get_json()
        token = data['token']
        if JwtService().verify(token) :
            return token, 200
        else : 
            return "Unauthorized", 401
