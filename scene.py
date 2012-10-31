from PIL import Image
from vectors import *
from time import time

class Camera():
    def __init__(self, dimensions, position=(0,0,0), inc = 1):
        self.w, self.h = dimensions
        self.inc = inc
        self.start = time()
    def draw(self, objects, lights):
        print "rendering a %d x %d image" % (self.w, self.h)
        def convtime(diff):
            seconds = diff % 60
            minutes = diff / 60
            hours = minutes / 60
            minutes %= 60
            return "%d hrs, %d min, %d sec" % (hours, minutes, seconds)

        img = Image.new("RGB", (self.h, self.w))

        getp = lambda x, m: (2 * float(x) / m) - 1
        percent = 0
        for y in xrange(self.h):
            for x in xrange(self.w):
                complete = float(y * self.h + x) / (self.w * self.h)
                if complete == float(percent + 1) / 100:
                    percent += self.inc
                    print str(percent) + "%"
                    timediff = time() - self.start
                    print convtime(timediff), "elapsed",
                    print convtime((timediff / float(percent) * 100) - timediff), "remaining\n"
                ray = Vector((getp(x, self.w), getp(y, self.h), 1))
                color = ray.color(objects, lights)
                if color == False:
                    vx = (x / 10) % 2
                    vy = (y / 10) % 2
                    if vx + vy == 1:
                        img.putpixel((x, y), (102,)*3)
                    else:
                        img.putpixel((x, y), (153,)*3)
                        
                    #img.putpixel((x, y), (0,)*3)
                else:
                    img.putpixel((x, y), color)
        img.show()
        img.save("out.png")

class Light():
    def __init__(self, pos, bright=1):
        self.pos = pos
        self.brightness = bright

if __name__ == "__main__":
        import main
