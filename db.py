import mariadb

def connect_db():
    try:
        conn = mariadb.connect(
        user="root",
        password="gokul",
        database="password",
        host="localhost",
        port=3306
        )
        print("Connected to db successfully")
    except Exception as e:
        print(e)

connect_db()

