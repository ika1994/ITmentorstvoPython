import pymysql
import pymysql.cursors
import config

conn = None
def create_conn()->object:
    global conn
    if conn is None:
        try:
            conn = pymysql.connect(host=config.HOST,user=config.USER,password=config.PASSWORD, database=config.DATABASE,cursorclass=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(f"Greska u konekciji: {e}")
            return None
    return conn
    
def show(table:str, column:str, order:str, limit:int = None)->list|bool:
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
        
def where(table:str, column:str, value:str)->list|bool:
    with conn.cursor() as cursor:
        query=f"SELECT * FROM {table} WHERE {column} = %s LIMIT 1"
        if(cursor.execute(query, value)):
            return cursor.fetchall()
    return False

def insert(table:str, columns:list[str], values:list[str])->bool:
    with conn.cursor() as cursor:
        columns_str=", ".join(columns)
        values_str=", ".join(["%s"]*len(values))
        query=f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"
        cursor.execute(query, values)
        conn.commit()
        return True
    return False

def update(table:str, columns:list[str], values:list[str], where_col:str, where_val:str)->bool:
    with conn.cursor() as cursor:
        update_query=", ".join([f"{col} = %s" for col in columns])
        query=f"UPDATE {table} SET {update_query} WHERE {where_col} = %s"
        cursor.execute(query,values + [where_val])
        conn.commit()
        return True
    return False

def delete(table:str, id:int)->bool:
    with conn.cursor() as cursor:
        query = f"DELETE FROM {table} WHERE id = %s"
        if(cursor.execute(query, id)):
            conn.commit()
            return True
        return False

def fetch_all(results:list[str]):
    for row in results:
        print(row)