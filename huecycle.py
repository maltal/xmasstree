from colorzero import Color, Hue
from tree import RGBXmasTree

tree = RGBXmasTree()

tree.color = Color('red')

try:
    while True:
        tree.color += Hue(deg=1)
except KeyboardInterrupt:
    tree.off
    tree.close()
