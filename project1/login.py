import pymysql
import re
import bcrypt
import pymysql.cursors
import config

import database as database

options =["sve", "first", "last"]

messages={
    "first_name":{
        "question":"Unesite imee",
        "error":"Greska niste uneli ime"
    },
    "last_name":{
        "question":"Unesite prezime",
        "error":"Greska niste uneli ime"
    }
}

name_pattern=r"^[a-zA-Z]+$"
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def check_user_exist(email):
    with database.conn.cursor() as cursor:
        query="SELECT * FROM users WHERE email=%s"
        cursor.execute(query,email)
        return cursor.fetchone()
    
def login(email):
    while True:
        password = input("Unesite lozinku da biste se ulogovali\n")
        user = return_user_data(email)
        if check_password(password,user['password'].encode('utf-8')):
            return True
        else:
            return False

def return_user_data(email):
    with database.conn.cursor() as cursor:
        query = "SELECT * FROM users WHERE email=%s"
        cursor.execute(query, email)
        return cursor.fetchone()

def hash_password(password):
   return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
   
def check_password(user_password, hashed_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def verify_name(name):
    if re.match(name_pattern,name):
        return name.lower().capitalize()
    else:
        return False

def verify_email(email):
    if re.match(email_pattern,email):
        return True
    else:
        return False

def check_name(name,messages):
    while name=="":
        name=input(messages+"\n")
        name=verify_name(name)
        if name==False:
            name=""
    return name   

def insert_password():
    user_password=""
    while user_password=="" or len(user_password)<8 :
        user_password=input("unesite lozinku\n")
    return hash_password(user_password)

def main():
    database.create_conn()
    option= None
    email=""
    action=""
    first_name=""
    last_name=""
           
    while email=="":
        email=input("Unesite email adresu\n")
        if not verify_email(email):
            email=""
        else:
            user=check_user_exist(email)
    if user:
        while not(login(email)):
            print("gresna lozinka")
        while option not in options:
            option=input(f"Da li zelite sve da prikazete ili samo jednog korisnika {options}")
        if(option.lower() == options[0]):
            if(results:=database.show("users","id","desc")):
                print(results)
            else:
                print("Greska find all")
        elif options[1]==option.lower():
            if(results:=database.show("users","id","asc",1)):
                print(results)
            else:
                print("greska find first")
        elif options[2]==option.lower():
            if(results:=database.show("users","id","desc",1)):
                print(results)
            else:
                print("greska find last")
    if not user:
        while action=="":
            action=input("---REGISTRACIJA---\nDa li zelite da se registrujete [DA/NE]\n").lower()
            if action==config.POSITIVE_ANSWER:
                first_name=check_name(first_name, messages["first_name"]['question'])
                last_name=check_name(last_name,messages["last_name"]["question"])
                
                database.insert("users",["email", "password", "first_name", "last_name"], [email, insert_password(),first_name,last_name])
                
            elif action==config.NEGATIVE_ANSWER:
                print("cao")
                break
            else:
                action=""

if __name__ == "__main__":
    main()