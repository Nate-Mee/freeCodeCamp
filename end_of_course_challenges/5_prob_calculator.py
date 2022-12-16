import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.hat = kwargs
        self.colours = self.hat.keys()
        self.contents = []
        for key in self.hat:
            for value in range(0, self.hat[key]):
                self.contents.append(key)

    def draw(self, num):
        pulled = []
        if num < len(self.contents):
            for n in range(0, num):
                pulled.append(self.contents.pop(random.randint(0, (len(self.contents) - 1))))
        else:
            pulled = self.contents
        return pulled


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_expected_count = 0
    for value in range(0, num_experiments):
        match_expected = 0
        original = copy.deepcopy(hat.contents)
        pulled = []
        if num_balls_drawn < len(original):
            for n in range(0, num_balls_drawn):
                pulled.append(original.pop(random.randint(0, (len(original) - 1))))
        else:
            pulled = hat.contents
        drawn_balls_dict = {}
        for col in set(pulled):
            drawn_balls_dict[col] = pulled.count(col)
        for colour in expected_balls:
            if colour in drawn_balls_dict:
                if expected_balls[colour] <= drawn_balls_dict[colour]:
                    match_expected += 1
        if match_expected == len(expected_balls):
            match_expected_count += 1
    prob = match_expected_count / num_experiments 
    return prob



# new_hat = Hat(yellow=3, blue=2, green=6)
# probability = experiment(hat=new_hat, expected_balls={'yellow':2, 'green':1}, num_balls_drawn=5, num_experiments=100)
# print(probability)

# hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
# probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=1)
# print(probability)

# hat = Hat(blue=3,red=2,green=6)
# probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
# print(probability)