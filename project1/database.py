import pymysql
import pymysql.cursors
import config

conn = None
def create_conn():
    global conn
    if conn is None:
        try:
            conn = pymysql.connect(host=config.HOST,user=config.USER,password=config.PASSWORD, database=config.DATABASE,cursorclass=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            print(f"Greska u konekciji: {e}")
            return None
    return conn
    
def show(table,column,order,limit=None):
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
        
def where(table, column, value):
    with conn.cursor() as cursor:
        query=f"SELECT * FROM {table} WHERE {column} = %s LIMIT 1"
        if(cursor.execute(query, value)):
            return cursor.fetchall()
    return False

def insert(table, columns, values):
    with conn.cursor() as cursor:
        columns_str=", ".join(columns)
        values_str=", ".join(["%s"]*len(values))
        query=f"INSERT INTO {table} ({columns_str}) VALUES ({values_str})"
        cursor.execute(query, values)
        conn.commit()
        return True
    return False

def update(table, columns, values, where_col, where_val):
    with conn.cursor() as cursor:
        update_query=", ".join([f"{col} = %s" for col in columns])
        query=f"UPDATE {table} SET {update_query} WHERE {where_col} = %s"
        cursor.execute(query,values + [where_val])
        conn.commit()
        return True
    return False

def delete(table, id):
    with conn.cursor() as cursor:
        query = f"DELETE FROM {table} WHERE id = %s"
        if(cursor.execute(query, id)):
            conn.commit()
            return True
        return False

def fetch_all(results):
    for row in results:
        print(row)