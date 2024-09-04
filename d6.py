students=[
    {"name":"Toma","score":100, "active":True},
    {"name":"Milos","score":20, "active":True},
    {"name":"Alija", "score":82, "active":False}
    ]
for student in students:
    if student["active"]:
        print(student)