class laptop:
    def __init__(self):
        self.price=1000
        self.processor=""
        self.ram=""
    def display(self):
        print ("processor:",self.processor)
hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=10000000
hp.processor="i7"
hp.ram="16GB"
print(hp.price)
print(dell.price)