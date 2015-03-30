#!/usr/bin/env python

#1. 
class Triangle(object):
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False
            
my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()



#2.
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." % (self.color,self.model,self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.display_car()

#3.
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        print "This is a %s %s with %s MPG." % (self.color,self.model,self.mpg)
    
    def drive_car(self):
        self.condition = "used"
        #print "This is a %s %s with %s MPG." % (self.color,self.model,self.mpg)
        
class ElectricCar(Car):
    def __init__(self,battery_type):
        self.battery_type = battery_type
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("molten salt")  
print my_car.condition
my_car.drive_car()
print my_car.condition
my_car.battery_type
my_car.model = "Cadillac"
my_car.color = "black"
my_car.mpg = 22
