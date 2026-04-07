class LibrarySystem:
    def __init__(self, book_price):
        self.book_price = book_price

    def return_book(self, late_days):
        fine = late_days * 10
        total = self.book_price + fine

        print("Book returned")
        print("Fine:", fine)
        print("Total amount:", total)