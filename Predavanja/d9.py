
books=[]

def add_book(name, author):
    books.append({"name":name, "author":author})

add_book("hp1", "JJR")
add_book("hp2", "jjr")
add_book("lort", "idk")


def delete_book(name):
    book_to_delete=check_book(name)
    if book_to_delete is None:
        return "Knjiga ne postoji"
    else:
        books.remove(book_to_delete)
        return "knjiga je obrisana"

def check_book(name):
    for book in books:
        if book["name"]==name:
          return book
        
print(delete_book("lort"))
