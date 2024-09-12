import json
import os

def load_file(file_name):
    with open(file_name,"r")as file:
        products=json.load(file)
    return products

def save_file(file_name, data):
    with open(file_name,"w") as file:
        json.dump(data, file, indent=4)

def delete_file(file_name):
    os.remove(file_name)

def empty_file(file_name):
    save_file(file_name,'')