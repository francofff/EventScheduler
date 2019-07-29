class Worker(object):
	def __init__(self, name, availability, isSupervisor):
		self.name = name
		self.aval2am = availability[0]
		self.aval2pm = availability[1]
		self.aval3am = availability[2]
		self.aval3pm = availability[3]
		self.aval4am = availability[4]
		self.aval4pm = availability[5]

		self.score = 0
		self.isSupervisor = isSupervisor
