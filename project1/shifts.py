import pymysql
import pymysql.cursors
from datetime import datetime, timedelta

import database as database


def create_shifts(user_id, start_time, end_time, date):
    if(start_time>end_time):
        return False
    database.insert("shifts", ["employee_id", "start_time", "end_time", "shift_date"],[user_id, start_time,end_time,date])
    return True

# Smenski rad tipa 12-24-12-48
def create_shift_v2(start_date, start_time, shift_type, repeats=4):
    shifts = []
    shift_str=shift_type.split("-")
    shift_numbers= [int(number) for number in shift_str]
    
    current_start = datetime.strptime(f"{start_date} {start_time}", '%Y-%m-%d %H:%M')
    
    for _ in range(repeats):
        work_start_1 = current_start
        work_end_1 = work_start_1 + timedelta(hours=shift_numbers[0])
        shifts.append((work_start_1, work_end_1))

        current_start = work_end_1 + timedelta(hours=shift_numbers[1])
        
        work_start_2 = current_start
        work_end_2 = work_start_2 + timedelta(hours=shift_numbers[2])
        shifts.append((work_start_2, work_end_2))
        
        current_start = work_end_2 + timedelta(hours=shift_numbers[3])

    return shifts