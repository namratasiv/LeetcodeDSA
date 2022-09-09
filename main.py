class Bird:
    def __init__(self):
        print("INIT calling")
    
    def common(self):
        print("common Bird")
    
    def birdf(self):
        print("birdf")
class Species:
    def __init__(self):
        print("INIT calling Species")
    
    def common(self):
        print("common Species")
    
    def birdS(self):
        print("birdS")
        


class Crow(Species,Bird):
    def __init__(self):
        
        Bird.__init__(self)
        Species.__init__(self)
        print("init crow")
    
    def common(self):
        super().common()
        print("common crow")
    
    def birdc(self):
        print("birdc")
print(Crow.mro())

obj = Crow()
print(repr(obj))
print(str(obj))
obj.common()
obj.birdc()
obj.birdf()
obj.birdS()