class laptop():
    chargertype='typeC' #class variable
    def __init__(self) -> None:
        self.price=0 #instance varaibles
        self.brand=''
    def setprice(self,p):
        self.price=p
    def displayprice(self):#instance method
        print(self.price)
    #@classmethod #--DECORATORS
    def changecharger(cls):#classmethod
        cls.chargertype='typeB'
    @staticmethod
    def info():#static method
        print('hello!!')

dell=laptop()
dell.displayprice()
dell.setprice(1000)
dell.displayprice()
print(laptop.chargertype)
#laptop.changecharger()
laptop.changecharger(laptop)
print(laptop.chargertype)
#laptop.info() 
dell.info()