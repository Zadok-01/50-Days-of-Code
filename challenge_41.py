# Challenge 41


from dataclasses import dataclass


@dataclass
class Car:
    model:        str
    colour:       str
    year:         int
    transmission: str
    electric:     bool
    
    def __str__(self):
        return f'Car_Model = {self.model}\nColor = {self.colour}\nYear = {self.year}\nTransmission = {self.transmission}\nElectric = {self.electric}'
    
    def print_cars(self):
        # pointless method, but requested
        print(self.__str__())


bmw1 = Car('X6', 'silver', 2018, 'auto', False)
tesla1 = Car('S', 'beige', 2017, 'auto', True)
ford1 = Car('Focus', 'white', 2020, 'auto', False)

print(ford1)
print()
ford1.print_cars()


'''
Challenge #41:

Day 41: Car Classes

Class of Cars

Create three classes of three car brands – Ford, BMW, and Tesla. The 
attributes of the car's objects will be, model, color, year, transmission, 
and whether the car is electric or not.

You will create one object for each car brand:
bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False
tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False

You will create a method, called print_cars that will be able to print out 
objects. For example, if you call the method on the ford1 object, your 
function should print out car info like so: 

car_model = focus
Color = White
Year = 2020
Transmission = Auto
Electric = False
'''

