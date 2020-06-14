# A simple mini project to process the ordered
# items in a restaurants

class Tab:

    # Attrubute named menu
    menu = {

        "beer":5,
         "veggie": 12,
         "pizza": 139,
         "burger": 39,
         "Cold_drink":65,
         "desert":76
    }

    # Attrubtes in a class
    table ={

        "Abhishek": 21,
        "Ashish": 34,
        "Aswin": 45
    }

    # self initializing constructor
    def __init__(self):
        self.items = []
        self.total = 0

    # to add item in the cart
    def add(self,item):
        self.items.append(item)
        self.total += self.menu[item]

    # Print the overall bill of cart
    def print_bill(self,tax,service):
        tax = (tax/100) * self.total
        service = (service/100) * self.total
        total = tax + service + self.total

        for item in self.items:
            print(item)
        for item in self.items:
            print(self.menu[item])

        print(total)

