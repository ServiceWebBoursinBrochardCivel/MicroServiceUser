import mariadb
import os

def db_connection():
    conn = None
<<<<<<< HEAD

    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_database = os.getenv('DB_DATABASE')

    try : conn = mariadb.connect(user= db_user, password= db_password, host= db_host,database= db_database)
=======
>>>>>>> a217173b82d38bead7e4bca2cb06b8b149a402dc
    except mariadb.Error as e:
        print('erreur')
    return conn