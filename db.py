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

if __name__ == "__main__":
    connect_db()
