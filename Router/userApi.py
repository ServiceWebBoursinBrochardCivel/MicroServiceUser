from flask import Blueprint,request,jsonify
from DatabaseManager.connection import db_connection

user_api = Blueprint('user_api',__name__)



@user_api.route('/users', methods=['GET','POST'])
def users() :
    conn = db_connection()
    cursor = conn.cursor()
    if request.method=='GET':
        cursor.execute("SELECT * FROM user")
        users = [
            dict(id=row[0],pseudo = row[1], mail=row[2], password=row[3])
            for row in cursor.fetchall()
        ]
        if users is not None :
            cursor.close()
            conn.close()
            return jsonify(users)
    if request.method=='POST':
        data = request.get_json()
        pseudo = data['pseudo']
        mail = data['mail']
        password = data['password']
        sql = """INSERT INTO user (pseudo,mail,password) VALUES (?,?,?); """
        cursor.execute(sql,(pseudo,mail,password))
        conn.commit()
        cursor.close()
        conn.close()
        return f"User with the id {cursor.lastrowid} created successful"

@user_api.route('/user/<int:id>',methods=['GET','DELETE'])
def single_user(id):
    conn = db_connection()
    cursor = conn.cursor()
    user = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM user WHERE id =?",(int(id),))
        rows = cursor.fetchall()
        for r in rows :
            user = r
        if user is not None :
            cursor.close()
            conn.close()
            return jsonify(user),200
        else :
            cursor.close()
            conn.close()
            return "Something wrong",404


    if request.method == 'DELETE':
        sql = """ DELETE FROM user WHERE id=? """
        cursor.execute(sql,(int(id),))
        conn.commit()
        cursor.close()
        conn.close()
        return "User with the id {} has been deleted".format(id),200