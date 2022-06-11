import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **balls):
        self.contents = []
        
        if sum(balls.values()) < 1 :
            raise Exception('Hat must have at least one ball!')
            
        for (key, value) in balls.items():
            if value < 0 :
                raise Exception("Negative number are not allowed!")
            if type(value) != int:
                raise Exception("Balls quantity must be an integer!")
                
            for i in range(0, value):
                self.contents.append(key)

    def draw(self, num):
        if type(num) != int:
            raise Exception("Balls quantity must be an integer!")
        if(num > len(self.contents)):
            return self.contents
          
        drawn = random.sample(self.contents, num)
        for item in drawn:
            self.contents.remove(item)

        return drawn
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hatcpy = None
    num_success = 0
    succes = True
    
    i = 0
    while i < num_experiments:
        hatcpy = copy.deepcopy(hat)
        i += 1
        succes = True
        draw = hatcpy.draw(num_balls_drawn)
        
        for (color, value) in expected_balls.items():
            if draw.count(color) >= value :
                succes = succes and True
            else:
                succes = succes and False
            
        if succes :
            num_success += 1
    
    return num_success / num_experiments   
