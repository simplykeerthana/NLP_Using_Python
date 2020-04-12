# -*- coding: utf-8 -*-

class Fish:
    def swim(self):
        print("Fish is swimming")
    def eat(self):
        print("fish is eating")
        


fish = Fish()
fish.swim()
fish.eat()


#override constructor 

class Game: 
    def __init__(self,name):
        self.name  = name
    def start(self):
        print(self.name, "has started")
    def stop(self):
        print(self.name, "has stopped")
        
game = Game("Counter strike")
game.start()
game.stop()