from data import list_of_products

class Product:
    """ product model """

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def show_product(self):
        return f"{self.name.title()} - {self.price} soums - {self.amount}kg"

    
def product_list(info):
    for key, val in info.items():
        current_product = Product(val['name'], val['price'], val['amount'])
        print(f"{key}. {current_product.show_product()}")
    

def buying():
    product_id = input("\nWhat will you buy? ")
    current_product = Product(list_of_products[product_id]['name'],list_of_products[product_id]['price'],list_of_products[product_id]['amount'])
    print(current_product.show_product())
    
    product_amount = int(input(f"How much {current_product.name} will you buy? "))
    if product_amount > current_product.amount:
        print(f"We don't have this much {current_product.name}. Only {current_product.amount}kg is left.")
        return None
    else:
        return product_amount * current_product.price


def run():
    total_payment = 0

    while True:
        print()
        product_list(list_of_products)
        olingan_product = buying()
        if olingan_product == None:
            davom_etish = input("\nWill you continue(yes/no): ")
            if davom_etish == "no":
                print(f"Your total payment is {total_payment} soums.\nThank you for using our service!")
                break
        else:
            total_payment += olingan_product
            print(f"Your current payment is {total_payment} soums")
            davom_etish = input("\nWill you continue(yes/no): ")
            if davom_etish == "no":
                print(f"Your total payment is {total_payment} soums.\nThank you for using our service!")
                break

run()