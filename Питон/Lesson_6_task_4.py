class Car:

    def __init__(self,speed,color,name,is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_poliсe = is_police

    def go(self):
        print('Машина движется')

    def stop(self):
        print('Машина остановилась')

    def turn(self,turn):
        print(f"Машина повернула на {turn}")

    def show_speed(self):
        return self.speed

class TownCar(Car):

    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')
        else: return self.speed

class SportCar(Car):

    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')
        else: return self.speed

class PoliceCar(Car):

    def __init__(self,speed,color,name,is_police):
        super().__init__(speed,color,name,is_police)

police = PoliceCar(70, "blue", "Audi", True)
police.turn("left")
print(police.show_speed())

winner = SportCar(140, "red", "Ferrari", False)
winner.turn("right")
print(winner.show_speed())

garbage = WorkCar(90, "black", "Yaz", False)
garbage.turn("right")
print(garbage.show_speed())

town = TownCar(60, "black", "honda", False)
town.turn("right")
print(town.show_speed())
