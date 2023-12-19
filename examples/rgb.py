from time import sleep

from colorzero import Color

from tree import RGBXmasTree

tree = RGBXmasTree()

colors = [Color('red'), Color('green'), Color('blue')] # add more if you like

try:
    while True:
        for color in colors:
            tree.color = color
            sleep(1)
except KeyboardInterrupt:
    tree.close()
