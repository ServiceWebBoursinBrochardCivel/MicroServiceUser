from flask import Blueprint,request,jsonify
import DatabaseFiles.connection as connection

search_api = Blueprint('search_api',__name__)

@search_api.route('/search/<string:pseudo>',methods=['GET'])
def search(pseudo):
    conn = connection.db_connection()
    cursor= conn.cursor()
    if request.method=='GET' :
        cursor.execute("SELECT * FROM user where pseudo = ?",(str(pseudo),))
        rows = cursor.fetchall()
        if(len(rows)>0) :
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
        else :
            cursor.close()
            conn.close()
            return "Something wrong",404