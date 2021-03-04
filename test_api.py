from ApiFiles.userApi import user_api
from ApiFiles.SearchApi import search_api
import DatabaseFiles.connection as connection

def single_user(id):
    conn = connection.db_connection()
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

    if request.method == 'PUT' :
        sql = """UPDATE user
                SET pseudo = ?,
                    mail=?,
                    password=?
                WHERE id=? """
        pseudo= request.form["pseudo"]
        mail = request.form["mail"]
        password = request.form["password"]
        updated_user = {
            'id':id,
            'pseudo' : pseudo,
            'mail' : mail,
            'password' : password
        }
        cursor.execute(sql,(pseudo,mail,password,int(id)))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify(updated_user)

    if request.method == 'DELETE':
        sql = """ DELETE FROM user WHERE id=? """
        cursor.execute(sql,(int(id),))
        conn.commit()
        cursor.close()
        conn.close()
        return "User with the id {} has been deleted".format(id),200

def test_supp():
    request.method = 'DELETE'
    assert single_user(2) == "User with the id 2 has been deleted"