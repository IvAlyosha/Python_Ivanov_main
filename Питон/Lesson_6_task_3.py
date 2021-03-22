class Worker:

    def __init__(self,name, surname,position):
       self.name = name
       self.surname = surname
       self.position = position
       wage = 10000
       bonus = 10000
       self._income = {
           "wage": wage,
           "bonus": bonus
       }


class Position (Worker):

    def __init__(self,name, surname, position):
        super().__init__(name, surname, position)
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(self._income["wage"]+self._income["bonus"])

a = Position('Alex','Ivnov','cheif service-manager')
a.get_full_name()
a.get_total_income()