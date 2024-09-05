def calculate_delivery(city):
    if city=="beograd":
        return 500
    elif city=="zagreb":
        return 600
    elif city=="subotica":
        return 1200
    elif city=="kragujevac":
        return 600

city=input("unesite grad\n").lower()
price=calculate_delivery(city)
print(f"Dostava do {city} je {price}")
