# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Car:
    no_of_tires = 4
    
    def __init__(self, make,model, year, color, moon_roof=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running  = False
    
    def start_engine(self):
        self.engine_running = True
    
    def stop_engine(self):
        self.engine_running = False

    def __del__(self):
        print("{} {}: Destructor Method!".format(self.make, self.model))
        
def main():
    car1 = Car("Ford","Mustang",2010,"Blue")
    car2 = Car("Tesla","Model 3",2020, "Red", True)
    
    print("Printing car1 details:".center(50,"-"))
    print("Make: {}".format(car1.make))
    print("Model: {}".format(car1.model))
    print("Year: {}".format(car1.year))
    print("Color: {}".format(car1.color))
    print("Moon Roof: {}".format(car1.moon_roof)) 
    
    print("Printing car2 details:".center(50,"-"))
    print("Make: {}".format(car2.make))
    print("Model: {}".format(car2.model))
    print("Year: {}".format(car2.year))
    print("Color: {}".format(car2.color))
    print("Moon Roof: {}".format(car2.moon_roof)) 
    
    print("Class Attributes:".center(50,"-"))
    print("car1: {}".format(car1.no_of_tires))
    print("car2: {}".format(car2.no_of_tires))
    print("Car: {}".format(Car.no_of_tires))
    
    del car2
    del car1

if __name__ == '__main__':
    main()