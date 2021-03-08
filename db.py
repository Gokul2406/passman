import mariadb
from menu import get_master_password
from secret import random_text_mp

conn = mariadb.connect(
user="root",
password="gokul",
database="password",
host="localhost",
port=3306
)
print("Connected to db successfully")
cur = conn.cursor()
 
def add_masterpassword():       
    masterkey_table = cur.execute("SELECT * FROM MasterPassword;")
    masterpassword = cur.fetchall()
    if len(masterpassword) == 0:
        print("No master password")
        new_masterpassword = input("Type a masterpassword(Make sure to remember it): ")
        hashed_masterpassword = str.join(new_masterpassword, random_text_mp)
        sql = f"""INSERT INTO MasterPassword(masterpassword) VALUES ('{hashed_masterpassword}')"""
        cur.execute(sql)
        conn.commit()
        print("successfully added")
        conn.close()

    else:
        user_masterpassword = input("What is the master password: ")
        hashed_user_masterpassword = str.join(user_masterpassword, random_text_mp)
        for master_tuple in masterpassword:
            for m in master_tuple:
                if m == hashed_user_masterpassword:
                    print("Successfully logged in")
                 

add_masterpassword()

