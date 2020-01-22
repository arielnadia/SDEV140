# Car Class Module

# This module creates a class named Car that contains attributes
# for the year model, make, and speed, and also contains methods
# for acceleration, braking and current speed.

class Car:
    def __init__(Self, Year_Model, Make):
        Self.__Year_Model = Year_Model
        Self.__Make = Make
        Self.__Speed = 0

    def set_year_model(Self, Year_Model):
        Self.__Year_Model = Year_Model

    def set_make(Self, Make):
        Self.__Make = Make

    def set_speed(Self, Speed):
        Self.__Speed = Speed
   
    def accelerate(Self, Speed):
        Self.__Speed += 5

    def brake(Self, Speed):
        Self.__Speed -= 5

    def get_year_model(Self):
        return Self.__Year_Model

    def get_make(Self):
        return Self.__Make

    def get_speed(Self):
        return Self.__Speed

    
