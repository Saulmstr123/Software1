'''
create a simple class
attibutes-variables
methods-functions working usually with attributes
'''


class CashRegister:
    def __init__(self):
        #Attributes
        self.items=0
        self.price=0

    #Methods
    def uptade_register(self, price):
        self.items=self.items+1
        self.price=self.price+price

    def display_register(self):
        return print('The number of items',self.items,'\n Totla price ',self.price)
    def clear_register(self):
        self.items=0
        self.price=0



register1=CashRegister()
register1.uptade_register(1.95)
register1.uptade_register(.65)
register1.uptade_register(99.99)
register1.uptade_register(25000)

print('Clear the register 1')

register1.clear_register()
register1.uptade_register(2.09)
register1.display_register()

print('register2')
register2=CashRegister()
register2.uptade_register(500)

register2.display_register()
print(register2.price)