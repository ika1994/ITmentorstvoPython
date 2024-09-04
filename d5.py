age=""
while not age.isdigit() or int(age) <18:
    age=input("Koliko godina imate?")
print(f"Imete {age} godina")