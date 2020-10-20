print("==========================================ONLINE LIBRARY MANAGEMENT================================================")
class Library:
    def __init__(self,list_of_books,Library_name):
        self.lend_data={}
        self.list_of_books=list_of_books
        self.Library_name=Library_name

        for books in self.list_of_books:
            self.lend_data[books]=None
    def display_books(self):
        for index,books in enumerate (self.list_of_books):
            print(f"{index}:{books}")
    def lend_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book]=reader
            else:
                print(f"Sorry this book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrng name")
    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name]=None
    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)
    def return_book(self,book,reader):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry this book is not lend")
        else:
            print("sorry, you entered the wrong name")
def main():
    list_books=['Rich Dad Poor Dad','Alchemist','Subtle Art Of Not Giving A Fuck']
    Library_name='Yashi'

    Yashi=Library(list_books,Library_name)

    print(f"Welcome To {Yashi.Library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' ")
    Exit=False
    while(Exit is not True):
        _input=input("options:")
        print("\n")
        if _input=="q":
            Exit=True
        elif _input=="d":
            Yashi.display_books()
        elif _input=="l":
            name = input("What is your name:")
            book = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            Yashi.lend_book(book,name)
        elif _input=="a":
            book_name=input("What is the name of book:")
            Yashi.add_book(book_name)
        elif _input=="del":
            book=input("book which you want to delete:")
            Yashi.delete_book(book)
        elif _input=="r":
            name=input("What is your name:")
            book=input("name of book which you want to return:")
            Yashi.return_book(book,name)
if __name__ == "__main__":
    main()