# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 13:33:53 2021

@author: Henry
"""


            
class Human():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight =weight
            
    def bmi(self):
        bmi = self.weight/ (self.height * self.height)
        return bmi
            
class Robot(Human):
    def __init__(self, name, height, weight):
        super().__init__(name, height, weight)    
        self.power = 100
        self.language = "English"
        self.color(0, 0, 255)
    def speak(self):
        if self.language == "English":
            print("hello")
        if self.language == "Chiness" :
            print("哈囉")


class Car():
    def __init__(self, speed, position, color):
        self.speed = speed
        self.position = position
        self.color = color
        
    def run(self):
        self.position = self.position + self.speed
    def getPosition(self):
        return self.position


class electricCar(Car):
    def __init__(self, speed, position, color):
        super().__init__(speed, position, color) 
        self.power = 100

    def run(self):
        if self.power > 0:
            self.power = self.power - 1
            self.position = self.position + self.speed

car1 = Car(30, 0, (255, 255, 255))
for i in range(200):
    car1.run()
print("car1's position is :" + str(car1.getPosition()))
    
car2 = electricCar(50, 0, (0, 0, 255))
for i in range(200):
 car2.run()
 
print("car2's power is :" + str(car2.power))


















"""
Henry = Human("Henry", 1.41, 31)
bmi = Henry.bmi()
print("Henry bmi is : " + str(bmi))
            
Jack = Human("Jack", 1.35, 26)
Jack = Jack.bmi()
print("Jack bmi is : " + str(bmi))       
"""










   