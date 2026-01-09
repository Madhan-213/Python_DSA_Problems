class car:
    def __init__(self,brand,mod):
        self.brand=brand
        self.mod=mod
    
    def info(self):
        print("brand name ia ",self.brand,"mod is ",self.mod)

c=car("BMW","X5")
c.info()

class bike:
    def __init__(self,brand,mod):
        self.brand=brand
        self.mod=mod
    
    def info(self):
        print("brand name ia ",self.brand,"mod is ",self.mod)
b=bike("KTM","Duke200")
b.info()