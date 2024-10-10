import csv
from collections import defaultdict
import matplotlib.pyplot as plt


cars_data=[]
car_brands=[]
car_models={}
price_by_year={}
grouped_by_year = defaultdict(list)

user_car_brand_input="" 
user_car_model_input=""

with open("car_price_prediction_.csv","r") as file:
    raider=csv.DictReader(file)
    for row in raider:
        cars_data.append(row)
        brand=row['Brand'].lower()
        model=row["Model"].lower()
        if brand not in car_brands:
            car_brands.append(brand)
        if brand not in car_models:
            car_models[brand]=[]
        if model not in car_models[brand]:
            car_models[brand].append(model)
        
        year = row['Year']
        price = float(row['Price'])
        grouped_by_year[(brand, model, year)].append(price)

print(car_brands)
while user_car_brand_input not in car_brands:
    user_car_brand_input=input("BRAND ").lower()

print(car_models[user_car_brand_input])
while user_car_model_input not in car_models[user_car_brand_input]:
    user_car_model_input=input("MODEL ").lower()

for (brand, model, year), prices in grouped_by_year.items():
    avg_price = sum(prices) / len(prices)
    price_by_year[year]=round(avg_price,2)


sorted_price_by_year = dict(sorted(price_by_year.items()))
list_years=[]
list_prices=[]
for year, price in sorted_price_by_year.items():
    list_years.append(year)
    list_prices.append(price)
    
print(f"{list_years[0]}: {list_prices[0]}")    
for i in range(1, len(list_prices)):
    if list_prices[i] > list_prices[i - 1]:
        print(f"{list_years[i]}: rast {list_prices[i]}")
    elif list_prices[i] < list_prices[i - 1]:
        print(f"{list_years[i]}: pad {list_prices[i]}")
    else:
        print(f"{list_years[i]}: nema promene {list_prices[i]}")
    
plt.figure(figsize=(10, 6))
plt.plot(list_years, list_prices, marker='.', color='r', linestyle='-')
plt.title('Cena automobila po godinama')
plt.xlabel('Godina')
plt.ylabel('Cena')
plt.xticks(rotation=45)  
plt.grid(True)            
plt.show()    


#for row in cars_data:
#    if (row['Brand'].lower() == user_car_brand_input and row['Model'].lower() == user_car_model_input):
        #print(row)
