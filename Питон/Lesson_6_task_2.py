class Road:
    def __init__(self,width,length):
        self._width = width
        self._length = length
    def mass_asfalt(self,mass, thinkness):
        return self._width*self._length*mass*thinkness

a=Road(100, 200)
print(a.mass_asfalt(25,5))