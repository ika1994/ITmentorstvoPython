products=[]
product=''
limit=3
while len(products)<limit :
    product = input(f"Potrebno je da unesete {limit-len(products)} produkta ")
    if not len(product)==0:
        products.append(product)
print(f"Uneseni proizvodi: {products}")