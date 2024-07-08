class fruit():
    def __init__(self,clr) -> None:
        self.colour=clr
        print (self.colour)
class teacher():
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print ("name:",self.name,'and registraion no:',self.reg)


apple=fruit("red")
bannana=fruit("yellow")

abi=teacher('abirami',5122004)
abi.display()
