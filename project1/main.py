import pymysql
import re
import bcrypt
import pymysql.cursors


#
# DEBUG
# 
# regex
# bcrypt
# user registration

HOST="localhost"
USER="root"
PASSWORD=""
DATABASE="project1"

#REGEX#
# dodati druge uslove regex
email_pattert=r""
name_pattern=r""
password_pattern=r""



#create connection with sql
def create_conn():
    return pymysql.connect(host=HOST,user=USER,password=PASSWORD, database=DATABASE,cursorclass=pymysql.cursors.DictCursor)


def check_user_exist(conn, email):
    with conn.cursor() as cursor:
        query="SELECT * FROM users WHERE email=%s"
        cursor.execute(query,email)
        return cursor.fetchone()
    
def login(conn, email):
    while True:
        password = input("Unesite lozinku da biste se ulogovali\n")
        user = verify_password(conn, email, password)
        if user:
            print(f"Uspešno ste se ulogovali: {user["first_name"]}")
            return True
        else:
            print("Greška: neispravna lozinka")

def verify_password(conn, email, password):
    with conn.cursor() as cursor:
        query = "SELECT * FROM users WHERE password=%s AND email=%s"
        cursor.execute(query, (password, email))
        return cursor.fetchone()

def hash_password(password):
    hashed_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def check_password(user_password, hashed_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def register_user(conn, email, password, name, last_name):
    with conn.cursor() as cursor:password
        query = "INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (email, password, first_name, last_name))
        conn.commit()

def verify_name(name):
    False

def verify_email(email):
    None

def main():
    conn=create_conn()

    email=""
    user_password=""
    action=""
    first_name=""
    last_name=""

    while email=="":
        email=input("Unesite email adresu\n")
        user=check_user_exist(conn,email)
    if user:
        login(conn, email)
    if not user:
        while action=="":
            action=input("---REGISTRACIJA---\nDa li zelite da se registrujete [DA/NE]\n").lower()
            if action=='da':
                while first_name=="":
                    first_name=input("Unesite ime\n")
                    verify_name(first_name)
                while last_name=="":
                    last_name=input("unesite prezime \n")
                while user_password=="" or len(user_password)<8 :
                    user_password=input("unesite ispravan pass\n")
                #upis u bazu
            elif action=='ne':
                print("cao")
                exit()
            else:
                action=""



if __name__ == "__main__":
    main()