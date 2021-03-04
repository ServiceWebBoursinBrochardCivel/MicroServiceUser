from flask import Blueprint,request,jsonify
import DatabaseFiles.connection as connection

search_api = Blueprint('search_api',__name__)

@search_api.route('/search',methods=['POST'])
def search():
    conn = connection.db_connection()
    cursor= conn.cursor()
    user = None
    if request.method =='POST':
        mail = request.form['mail']
        password = request.form['password']
        sql = """SELECT * FROM user WHERE mail =? and password =?"""
        cursor.execute(sql,(mail,password))
        rows = cursor.fetchall()
        for r in rows :
            user = r
        conn.commit()
        cursor.close()
        conn.close()
        if user is not None:
            return f"Existant"
        return f"Innexistant"



      