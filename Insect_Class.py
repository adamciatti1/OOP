import random

class Insect:
    def __init__(self,wings,legs):
        self.wings = wings
        self.legs = legs
        self.distance = 0

    def flight(self):
        self.distance = random.randint(1, 10)

    def get_flight(self):
        return self.distance
