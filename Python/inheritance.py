class parent:
    def __init__(self,name):
        self.name=name

    def show(self):
        print("hello ",self.name)

class child(parent):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print("hello its me",self.name)

p1 = parent("madhu")
c1= child("madhu")

c1.show()
