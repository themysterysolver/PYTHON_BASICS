class dad():
    def __init__(self) -> None:
        print('DAD')
    def money(self):
        print("DAD'S MONEY")
class mom():
    def car(self):
        print("MOM'S CAR")
class son(dad,mom): #Multiple inheritance,hierarchial inheritance
    def __init__(self) -> None:
        super.__init__()
    def phone(self):
        print("SON'S PHONE")
class brother(son): #Single and multilevel inheritance
    def phone(self):
        print("Brother's bike")
class brother1(son):
    def phone(self):
        print("Brother's gun")
arjun=son()
arjun.phone()
arjun.money()
arjun.car()
sam=brother()
sam.money()

