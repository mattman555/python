class other(object):
	
	def implicit(self):
		print "Other implicit()"
	
	def altered(self):
		print "Other altered()"
	

class child(object):
	
	def __init__(self):
		self.other = other()
		
	def implicit(self):
		self.other.implicit()
		
	def overide(self):
		print "Child overide"
	
	def altered(self):
		print"Child before"
		self.other.altered()
		print"Child after"

son = child()

son.implicit()
son.overide()
son.altered()
		
