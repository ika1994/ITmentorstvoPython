products={
    "hleb":{
        "cena":150,
        "kolicina":50
    },
    "pivo":{
        "cena":120,
        "kolicina":200
    }
}
options=["dodaj","obrisi","izlistaj", "stop", "istorijat", "obrisi sve", "najskuplji"]
history=[]
action = None
item =None
while  action not in options:
    action=input(f"Unesite akciju {options}\n ").lower()

    if action=="dodaj":
        item=input("Unesi proizvod \n").lower()
        while item in products or item is None or len(item)<2:
            item=input("proizvod vec postoji \n").lower()
        price=input("unesite cenu proizvoda \n")
        while  not price.isdigit():
            price=input("cena mora da bude broj i mora da bude veca od 0 \n")
        quantity=input(f"Unesite kolicinu za proizvod {item} \n")
        while not quantity.isdigit():
            quantity=input(f"niste uneli kolicinu za proizvod {item} \n")
        products[item]={"cena":price, "kolicina": quantity}
        history.append(f"Dodali ste proizvod {item}, sa cenom {price} i kolicinom {quantity}")

    elif action=="obrisi":
        product_to_delete=""
        print(products)
        while product_to_delete not  in products:
            product_to_delete=input("koji produkt zelite da obriseta\n").lower()
        del(products[product_to_delete])
        history.append(f"Obrisali ste produkt {product_to_delete}")

    elif action=="obrisi sve":
        products.clear()
        history.append("obrisali ste sve")

    elif action=="izlistaj":
        print(products)

    elif action=="stop":
        quit()

    elif action=="istorijat":
        print(history)

    elif action=="najskuplji":
        max_cena=0
        for product in products:
            if int(products[product]["cena"])>max_cena:
                max_cena=products[product]["cena"]
                high_price_product=product
        print(high_price_product)
        print("\n lambda print: ")
        high_price_product = max(products, key=lambda x: products[x]["cena"])
        print(high_price_product)
    action=None