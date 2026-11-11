import csv
from csv import DictReader


class Item:
    pay_r=0.8
    all=[]
    def __init__(self,name: str,price: float,quantity: int=0):
        #run validations

        assert price>=0, f"prince {price} cant b less than 0"
        assert quantity>=0, f"quantity {quantity} cant be less than 0"
        # instantiate
        self.name=name
        self.price=price
        self.quantity=quantity

        #actions
        Item.all.append(self)
    def apply_dic(self):

        self.price=self.price*self.pay_r
        return self.price
    def calc_tot(self):
        return self.price*self.quantity
    @classmethod
    def instance_from_csv(cls):
        with open('items.csv','r') as f:
            reader=csv.DictReader(f)
            items=list(reader)
            for item in items:
                print(item)
    def __repr__(self) -> str:
        return f"Item('{self.name}',{self.price},{self.quantity}"

item1=Item('phone',1000,3)
item2=Item('Laptop',100,4)
item3=Item('book',200,2)
item4=Item('kite',100,4)
item5=Item("car",4000,1)
Item.instance_from_csv()
#print(Item.all)