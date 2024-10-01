price=int(input("vrednost korpe"))
if price>=1000:
    tax=price*0.1
    print(f"ostvarili ste popust od 10% i iznosi {tax}")
else:
    print("nemate popust")