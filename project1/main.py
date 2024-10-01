import pymysql
import re
import bcrypt
import pymysql.cursors

### NE radi register user


HOST="localhost"
USER="root"
PASSWORD=""
DATABASE="project1"

POSITIVE_ANSWER="da"
NEGATIVE_ANSWER="ne"

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
        user = return_user_data(conn, email)
        if check_password(password,user['password'].encode('utf-8')):
            return True
        else:
            return False

def return_user_data(conn, email):
    with conn.cursor() as cursor:
        query = "SELECT * FROM users WHERE email=%s"
        cursor.execute(query, email)
        return cursor.fetchone()

def hash_password(password):
   return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
   
def check_password(user_password, hashed_password):
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def register_user(conn, email, password, first_name, last_name):
    with conn.cursor() as cursor:
        query = "INSERT INTO users (email, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (email, password.decode('utf-8'), first_name, last_name))

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

def find(conn,table,column,order,limit=None):
    with conn.cursor() as cursor:
        query=f"SELECT * FROM {table} ORDER BY {column} {order}"
        if limit:
            query+=f" LIMIT {limit}"
        if(cursor.execute(query)):
            if limit==1:
                return cursor.fetchone()
            else:
                return cursor.fetchall()
    return False
        
def where(conn, table, column, value):
    with conn.cursor() as cursor:
        query=f"SELECT * FROM {table} WHERE {column} = {value} LIMIT 1"
        if(cursor.execute(query)):
            return cursor.fetchall()
        return False

##FETCH Funkcija
def fetch_all(results):
    for row in results:
        print(row)

#def insert_password():
#    user_password=""
#   while user_password=="" or len(user_password)<8 :
#        user_password=input("unesite lozinku\n")
#    return hash_password(user_password)

def main():
    conn=create_conn()
    option= None
    email=""
    user_password=""
    action=""
    first_name=""
    last_name=""
    
    #register_user(conn,"e@w.w","$2a$12$qGq5rBbQbXsk6oaI.HNRZOotrSXyCx.yziANqTS2nw95A2mxWGb9i","im","prez") 
       
    while email=="":
        email=input("Unesite email adresu\n")
        if not verify_email(email):
            email=""
        else:
            user=check_user_exist(conn,email)
    if user:
        #greska: ukoliko se ne unese pass pita dva puta login zbog duplog pozivanja funkcije
        while not(login(conn, email)):
            print("greska lozinka")
            #
            login(conn, email)
            #
        while option not in options:
            option=input(f"Da li zelite sve da prikazete ili samo jednog korisnika {options}")
        if(option.lower() == options[0]):
            if(results:=find(conn,"users","id","desc")):
                print(results)
            else:
                print("Greska find all")
        elif options[1]==option.lower():
            if(results:=find(conn,"users","id","asc",1)):
                print(results)
            else:
                print("greska find first")
        elif options[2]==option.lower():
            if(results:=find(conn,"users","id","desc",1)):
                print(results)
            else:
                print("greska find last")
    if not user:
        while action=="":
            action=input("---REGISTRACIJA---\nDa li zelite da se registrujete [DA/NE]\n").lower()
            if action==POSITIVE_ANSWER:
                first_name=check_name(first_name, messages["first_name"]['question'])
                last_name=check_name(last_name,messages["last_name"]["question"])
                while user_password=="" or len(user_password)<8 :
                    user_password=input("unesite lozinku\n")
                user_password = hash_password(user_password)
                
                register_user(conn,email,user_password,first_name, last_name)
                #register_user(conn,email,insert_password(),first_name, last_name)
                
            elif action==NEGATIVE_ANSWER:
                print("cao")
                exit()
            else:
                action=""

if __name__ == "__main__":
    main()