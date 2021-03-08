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
 
def add_master_password():       
    randomkey_table = cur.execute("SELECT * FROM randomkey;")
    print("Hello")
    randomkey = cur.fetchall()
    print(randomkey)
    for r in randomkey:
        if r is None:  
            random_words = input("Type some random words: ") 
            sql = f"""INSERT INTO randomkey (randomkey) VALUES ("{random_words}")"""
            cur.execute(sql)
            conn.commit()
            conn.close()
            print("Successfully added random words")

        elif randomkey is not None:
            print("Random key is present")

add_master_password()

