shops={
    "maxi":{
        "hleb":150,
        "novine":30
    },
    "roda":{
        "hleb":100,
        "novine":30
    },
    "aman":{
        "hleb":30,
        "novine":30
    },
    "idea":{
        "novine":20
    }
}
avg=0.0
sum=0
i=0
max=0
max_price_shop=""
for shop, items in shops.items():
    if "hleb" in items:
        if max<items["hleb"]:
            max=items["hleb"]
            max_price_shop=shop
        sum+=items["hleb"]
        i+=1
avg=sum/i
print(f"srednja vrednost hleba je {avg} i najskuplji hleb je u prodavnici {max_price_shop}")