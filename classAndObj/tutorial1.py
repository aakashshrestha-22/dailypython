class Item:
    def __init__(self, name:str, price:float, quantity=0 ):
        self.name = name
        self.price= price
        self.quantity= quantity
    def calculate_total_price(self):
        return self.price * self.quantity
    
item1 = Item("Aakash", 22, 1)


item2 = Item("Sky",300, 3)  
print(item1.calculate_total_price())
print(item2.calculate_total_price())

