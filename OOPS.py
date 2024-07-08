class item(): #class declaration..SYNTAX
    pay_rate=0.8 #class atributes
    all=[]
    def __init__(self, name:str, price:float,quantity=0): #one of the magic methods
        assert price>=0 ,f"Price {price} is not greater tahn or equal to zero" #assert+msgs
        assert quantity>=0
        self.name=name
        self.price=price
        self.quantity=quantity
        item.all.append(self) #item.all is a member of class'''
       
 
    #__repr__ representing object magic method
    def __repr__(self):
           return f"item('{self.name}','{self.price}','{self.quantity}')"
    def calculate_tot_price(self):  
        print ( self.price* self.quantity)
        ''' function as method! '''  #self is the object

    def apll_disc(self):
        self.price=self.price*self.pay_rate # class level(item) and instance(self) level '''
#item1=item() #creating a object/INSTANTIATION!
'''item1.name="phone"
item1.price=1000
item1.quantity=4
item1.calculate_tot_price(item1.price,item1.quantity)'''
item1=item("phone",1000,7)
item2=item("laptop",20000,4)
item2.calculate_tot_price()#item2.calculate_tot_price(item2.price,item2.quantity) if given!

item2.mouse="available!"
print(item.__dict__) #magic method
print(item1.__dict__)
print(item2.__dict__)

item1.apll_disc()
print(item1.price)

item2.pay_rate=0.7
item2.apll_disc()
print(item2.price)

print(item.all) #not a convinenet way!!

