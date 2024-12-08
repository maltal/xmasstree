import random

from tree import RGBXmasTree

tree = RGBXmasTree()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random_color()

except KeyboardInterrupt:
    tree.close()
