#  Write a Python program to create a Book class with a constructor that accepts the title, author, and price of a book.
#  Create functions to display the book details, apply a discount on the price, and display the final price.
#  Create an object of the class and demonstrate all the functions.


class Book:
    def __init__(self, title, author, price_of_book):
        self.title = title
        self.author = author
        self.price_of_book = price_of_book
        self.final_price = price_of_book

    def display_details(self):
        print("=============  Book Details  ================")
        print("Title  :", self.title)
        print("Author :", self.author)
        print("Price  :", self.price_of_book)

    def discount(self, percentage):
      if self.price_of_book > 200:
           discount_amount = self.price_of_book * percentage / 100
           self.final_price = self.price_of_book - discount_amount
           print("Discount :", discount_amount)
      else:
           self.final_price = self.price_of_book
           print("No discount available.")

    def display_final_price(self):
        print("Final Price :", self.final_price)



book1 = Book("Python Programming", "Ali", 500)

book1.display_details()

book1.discount(10)

book1.display_final_price()