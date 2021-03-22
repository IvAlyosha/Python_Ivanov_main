class Clothes:
    def __init__(self,clothes):
        self.clothes = clothes.upper()
        self._fabric = None
    @property
    def calculation_fabric(self):
        return self._fabric
    @calculation_fabric.setter
    def calculation_fabric(self,value):
        if self.clothes == 'COAT' or 'ПАЛЬТО':
            self._fabric = (value/6.5 + 0.5)
        elif self.clothes == 'SUIT' or 'КОСТЮМ':
            self._fabric = (value*2+0.3)
suit = Clothes('Пальто')
suit.calculation_fabric = 12
print(suit.calculation_fabric)
coat = Clothes('Coat')
coat.calculation_fabric = 40
print(coat.calculation_fabric)