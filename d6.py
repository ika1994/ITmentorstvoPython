students=[
    {"name":"Toma","score":100, "active":True},
    {"name":"Milos","score":35, "active":True},
    {"name":"Alija", "score":82, "active":False}
    ]
for student in students:
    if student["active"]:
        if student["score"]>80:
            student["grade"]="A"
        elif 60<student["score"]<80:
            student["grade"]="B"
        elif 40<student["score"]<60:
            student["grade"]="C"
        elif 20<student["score"]<40:
            student["grade"]="D"
        else:
            student["grade"]="F"
        print(student)