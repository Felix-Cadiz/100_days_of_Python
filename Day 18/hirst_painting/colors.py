# Module to use random colors throughout the project.

import random

class Colors: 
    def __init__(self):
        pass

    def random_colors(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color_pallet = (r, g, b)
        return color_pallet