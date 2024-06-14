import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []

        #Appending strings for given number of keyword arguments
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    
    def draw(self, draw_number):
        drawn = []

        if draw_number > len(self.contents):
            drawn = self.contents[:]
            self.contents.clear()
            return drawn
        else:

            for i in range(draw_number):
                removed = self.contents.pop(random.randint(0,len(self.contents)-1))
                drawn.append(removed)
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        expected_copy = copy.deepcopy(expected_balls)
        colors_drawn = hat_copy.draw(num_balls_drawn)

        for color in colors_drawn:
            if(color in expected_copy):
                expected_copy[color] -= 1

        if all(x <= 0 for x in expected_copy.values()):
            count += 1
    
    return count/num_experiments

hat = Hat(black=6, red=4, green=3)
print(hat.draw(15)) 