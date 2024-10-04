import os

import login
import shift_menagment


def list_files_in_directory(directory):
    subscripts=[]
    subscripts_exceptions=['config.py', "database.py", "main.py", "project1.sql", "shifts.py", "__pycache__"]
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) not in subscripts_exceptions:
            if(filename not in subscripts_exceptions):
                filename=filename.split('.')[0].replace('_', ' ')
                subscripts.append(filename)
    return subscripts     
            


def main():
    while True:
        i=1
        current_directory = os.getcwd()
        files=list_files_in_directory(current_directory)
        print("Izaberite skriptu koju zelite da pokrenete:")
        for i, ss in enumerate(files,start=1):
            print(f"{i}. {ss}")
        print(f"{len(files) + 1}. Izlaz")
        
        choice = input("Unesite broj opcije: ")
        

        #treba automatizovati da sam broji koliko skripti ima da dinamicki ponudi koliko ima opcija korisnik
        if choice == "1":
            login.main()
        elif choice == "2":
            shift_menagment.main()
        elif choice == "3":
            print("Izlaz iz programa.")
            break
        else:
            print("Nepoznata opcija, pokušajte ponovo.")

if __name__ == "__main__":
    main()