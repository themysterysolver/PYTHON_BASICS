class company():
    def __init__(self):
        self.__name='google'
        self._owner='xyz'
    def change_company_name(self,newname):
        self.__name=newname
    def display(self):
        print ("the comapany name is ",self.__name,' the owner is ',self._owner)
CEO=company()
CEO.display()
CEO.change_company_name('X')

print(CEO._owner)
CEO._owner='sundarpichai'
print(CEO._owner)
CEO.display()
CEO.__name='instagram'
print(CEO.__name)
print(CEO._company__name)
CEO._company__name= 'YouTube'
CEO.display()

