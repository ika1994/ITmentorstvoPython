products={
    "hleb":{
        "cena":100,
        "kolicina":50
    },
    "pivo":{
        "cena":120,
        "kolicina":200
    }
}

action = None
item =None
while  action not in ["dodaj","obrisi"]:
    action=input("Unesite akciju [Obrisi/Dodaj]").lower()
print(action)

for product in products:
    print(product)
product_to_delete=""

if action=="dodaj":
    item=input("Unesi proizvod ").lower()
    while item in products or item==None or len(item)<2:
        item=input("proizvod vec postoji ").lower()
    price=input("unesite cenu proizvoda")
    while  not price.isdigit():
        price=input("cena mora da bude broj i mora da bude veca od 0 ")
    quantity=input(f"Unesite kolicinu za proizvod {item} ")
    while not quantity.isdigit():
        quantity=input(f"niste uneli kolicinu za proizvod {item}")
    products[item]={"cena":price, "kolicina": quantity}

if action=="obrisi":
    while product_to_delete not  in products:
        product_to_delete=input("koji produkt zelite da obriseta ").lower()
    del(products[product_to_delete])
print(products)