class Sphere():
	def __init__(self, pos, size, colour):
		self.pos = pos
		self.r = size
		self.colour = colour

	def getdis(self, center, ray):
		v = center.proj(ray)
		d = self.r ** 2 - center.size() ** 2 + v.size() ** 2
		if d < 0:
			return False
		size = v.size() - d ** 0.5
		v = v * size / v.size()
		return v