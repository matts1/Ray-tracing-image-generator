from scene import *
from shapes import *
from vectors import *
import csv

objects = []
for line in csv.DictReader(open('objects.csv', 'rU')):
    pos = map(float, (line["X"], line["Y"], line["Z"]))
    color = map(float, (line["R"], line["G"], line["B"]))
    obj = eval("%s(%r,%s, %r)" % (line["Type"], pos, line["Size"], color))
    if int(line["On"]):
        objects.append(obj)

lights = []
for line in csv.DictReader(open('lights.csv', 'rU')):
    pos = map(float, (line["X"], line["Y"], line["Z"]))
    light = Light(pos, float(line["Brightness"]))
    if int(line["On"]):
        lights.append(light)

Camera((50, 50), inc=5).draw(objects, lights)
