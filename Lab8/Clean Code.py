class FineCalculator:
    def __init__(self, late_days):
        self.late_days = late_days

    def calculate_fine(self):
        return self.late_days * 10


class ReturnService:
    def return_book(self):
        print("Book returned successfully")


class ReceiptPrinter:
    def print_receipt(self, fine):
        print("Fine:", fine)


# Usage
fine_calc = FineCalculator(5)
fine = fine_calc.calculate_fine()

return_service = ReturnService()
return_service.return_book()

printer = ReceiptPrinter()
printer.print_receipt(fine)