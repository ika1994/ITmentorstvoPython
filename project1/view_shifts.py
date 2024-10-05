import database


######## TEST ######


def shifts_per_person(user_id, start_date, end_date):
    with database.conn.cursor() as cursor:
        query="SELECT * FROM shifts WHERE employee_id = %s AND shift_date BETWEEN %s AND %s ORDER BY shift_date ASC"
        cursor.execute(query, (user_id, start_date, end_date))
        return cursor.fetchall()
    return False


def main():
    database.create_conn()
    print(database.show("users","id", "asc"))
    employee_id=input("unesite id radnika: ")
    start_date=input("unesite od kog datuma zelite da vidite smene za radnika [YYYY-MM-DD]: ")
    end_date=input("unesite do kog datuma zelite da vidite smene: ")
    spp=shifts_per_person(employee_id, start_date, end_date)
    if not spp:
        print("Nije uneta ni jedna smena za radnika\n")
    elif spp == False:
        print("opsta greska\n")
    else:
        print(spp)