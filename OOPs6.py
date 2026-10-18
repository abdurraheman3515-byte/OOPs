
# Multilevel Inheritance

class Product:
    def __init__(self, pid):
        self.pid = pid


class Category(Product):
    def __init__(self, pid, pname, pcategory, price):
        super().__init__(pid)
        self.pname = pname
        self.pcategory = pcategory
        self.price = price


class Order(Category):
    def __init__(self, pid, pname, pcategory, price, qty, payment_method):
        super().__init__(pid, pname, pcategory, price)
        self.qty = qty
        self.payment_method = payment_method

    def amount(self):
        total = self.price * self.qty

        print("--------- Order Details ---------")
        print("Product ID      :", self.pid)
        print("Product Name    :", self.pname)
        print("Category        :", self.pcategory)
        print("Price           : ₹", self.price)
        print("Quantity        :", self.qty)
        print("Payment Method  :", self.payment_method)
        print("---------------------------------")
        print("Total Amount    : ₹", total)

        return total



O1 = Order(101,"Ear Phone","Electronics",800, 2,"UPI")


O1.amount()
