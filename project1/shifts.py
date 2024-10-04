import pymysql
import pymysql.cursors


import database as database


def create_shifts(user_id, start_time, end_time, date):
    if(start_time>end_time):
        return False
    database.insert("shifts", ["employee_id", "start_time", "end_time", "shift_date"],[user_id, start_time,end_time,date])
    return True