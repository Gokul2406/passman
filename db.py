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
    table = cur.execute("SELECT * FROM MasterPassword;")
    if table == None:
        
        random_words = input("Type some random words: ") 
        sql = f"""INSERT INTO randomkey (randomkey) VALUES ("{random_words}")"""
        cur.execute(sql)
        conn.commit()
        conn.close()
        print("Successfully added random words")
        master_password = input("Type the new master password: ")

        print(str.join(random_words, master_password)) 
   
add_master_password()

