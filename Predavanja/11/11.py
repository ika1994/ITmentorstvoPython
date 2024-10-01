import json
from datetime import datetime
max_budget=50000

user=None
with open("json/users.json","r") as file:
    user=json.load(file)

user_budget=user["budget"]+user['credit']
if max_budget<user_budget or user_budget<0:
    print("Greska")
    exit()



expense=0
while expense<=0 or expense>user_budget:
    expense=int(input("Unesite koliko novca zelite da potrosite\n"))
print(user['budget'])

with open("logs/expenses_log.txt","a")as file:
    remaining_budget=user_budget-expense
    log=f"Amount: {expense}\tid: {user['id']}\t Budget: {user["budget"]}\t remaining: {remaining_budget}\tDateTime: {datetime.now()}\n"
    file.write(log)