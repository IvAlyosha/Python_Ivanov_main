import time
class TrafficLight:

    color_pre = "green"

    def __init__(self,color):
       self.color = color

    def running (self,color):
        if color == 'red' and TrafficLight.color_pre == "green":
            time.sleep(2)
            print("yellow")
            TrafficLight.color_pre = "red"
        elif color == 'yellow' and TrafficLight.color_pre == "red":
            time.sleep(4)
            print("green")
            TrafficLight.color_pre = "yellow"
        elif color == 'green' and TrafficLight.color_pre == "yellow":
            time.sleep(7)
            print("red")
            TrafficLight.color_pre = "green"
        else: print('Неправильный порялок переключения')

a = TrafficLight("")
a.running("red")
a.running("yellow")
a.running("green")
a.running("yellow")