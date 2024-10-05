import os
import importlib

def list_files_in_directory(directory):
    subscripts=[]
    subscripts_exception=['config.py', "database.py", "main.py", "project1.sql", "shifts.py", "__pycache__"]
    
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) not in subscripts_exception:
            if(filename not in subscripts_exception):
                filename=filename.split('.')[0]
                subscripts.append(filename)
    return subscripts     
            


def main():
    while True:
        i=1
        current_directory = os.getcwd()
        files=list_files_in_directory(current_directory)
        print("Izaberite skriptu koju zelite da pokrenete:")
        for i, ss in enumerate(files,start=1):
            ss=ss.split('.')[0].replace("_", " ")
            print(f"{i}. {ss}")
        print(f"{len(files) + 1}. Izlaz")
        
        choice = input("Unesite broj opcije: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("pogresan unos")
            continue  # Restart the loop for a new input
        
        if choice == len(files) + 1:
            print("Izlaz iz programa.")
            break
        valid_choice=False
        for i, ss in enumerate(files, start=1):
            if choice ==i:
                valid_choice=True
                module = importlib.import_module(ss)
                print(module)
                module.main()
                break
        if not valid_choice:
            print("Nepoznata komanda, pokusaj ponovo")

if __name__ == "__main__":
    main()