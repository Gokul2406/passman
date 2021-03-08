import mariadb
from menu import get_master_password

conn = mariadb.connect(
user="root",
password="gokul",
database="password",
host="localhost",
port=3306
)
print("Connected to db successfully")
cur = conn.cursor()
 
def add_random_key():       
    randomkey_table = cur.execute("SELECT * FROM randomkey;")
    randomkey = cur.fetchall()
    if len(randomkey) == 0:
        random_words = input("Type some random words: ") 
        sql = f"""INSERT INTO randomkey (randomkey) VALUES ("{random_words}")"""
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("Successfully added random words")

    else:
        for r in randomkey:
            print(r)
        

add_master_password()

