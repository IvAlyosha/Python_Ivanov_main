class Stationery:
    def __init__(self,titel):
        self.titel = titel
    def draw(self):
        print("Запуск отрисовки...")

class Pen(Stationery):
    def __init__(self,titel):
        super().__init__(titel)
    def draw(self):
        print(f"Запуск отрисоки {self.titel}")

class Pencil(Stationery):
    def __init__(self,titel):
        super().__init__(titel)
    def draw(self):
        print(f"Запуск отрисоки {self.titel}")

class Hadnel(Stationery):
    def __init__(self,titel):
        super().__init__(titel)
    def draw(self):
        print(f"Запуск отрисоки {self.titel}")

pen = Pen("ручка")
pencil = Pencil("карандаш")
handel = Hadnel("маркер")
pen.draw()
pencil.draw()
handel.draw()