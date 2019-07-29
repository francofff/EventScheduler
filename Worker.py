class worker(object):
	def __init__(self, name, availablity):
		self.name = name
		self.aval2am = availablity[0]
		self.aval2pm = availablity[1]
		self.aval3am = availablity[2]
		self.aval3pm = availablity[3]
		self.aval4am = availablity[4]
		self.aval4pm = availablity[5]
