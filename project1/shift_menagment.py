import database as database
import shifts
import config

def main():
    database.create_conn()
    while True:
        user_id= input("unesite id radnika: ")
        shift_start= input("pocetak smene [HH:MM]: ")
        shift_end=input("kraj smene [HH:MM]: ")
        shift_date=input("unesite datum smene [YYYY-MM-DD]: ")
        if shifts.create_shifts(user_id, shift_start, shift_end, shift_date):
            print("smena kreirana")
        another=input("\nDa li zelita da kreirate smenu za jos jednog radnika? [da/ne] ").lower()
        while another != config.POSITIVE_ANSWER and another!=config.NEGATIVE_ANSWER:
            print(f"unesite {config.POSITIVE_ANSWER} ili {config.NEGATIVE_ANSWER} ---- {another}")
            another=input("\nDa li zelita da kreirate smenu za jos jednog radnika? [da/ne] ").lower()
        if another==config.NEGATIVE_ANSWER:
            break
    database.fetch_all(database.show("shifts","id", "asc"))
    
if __name__ == "__main__":
    try:
        main()
    finally:
        database.conn.close()