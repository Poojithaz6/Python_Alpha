class Item:
    pay_r=0.8
    def __init__(self,name: str,price: float,quantity: int=0):
        #run validations

        assert price>=0, f"prince {price} cant b less than 0"
        assert quantity>=0, f"quantity {quantity} cant be less than 0"
        self.name=name
        self.price=price
        self.quantity=quantity

    def calc_tot(self):
        return self.price*self.quantity
item1=Item('phone',1000,3)
print(item1.pay_r)
