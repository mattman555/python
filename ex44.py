class other(object):#Make a class called other that has-a object
	
	def implicit(self):#Procedure that prints when called
		print "Other implicit()"
	
	def altered(self):#Procedure that prints when called
		print "Other altered()"
	

class child(object):#Make a class called other that has-a object
	
	def __init__(self):#intialization procedure that gives the self.other object the propreties of the other class
		self.other = other()
		
	def implicit(self):#Procedure that prints then calls the implicit procedure from the other class then prints something else
		self.other.implicit()
		
	def overide(self):#Procedure that prints when called
		print "Child overide"
	
	def altered(self):#Procedure that prints then calls the altered procedure from the other class then prints something else
		print"Child before"
		self.other.altered()#call the altered procedure from the other class
		print"Child after"

son = child()#make the son object with the propreties of the child class

son.implicit()#class the implicit procedure from child through son
son.overide()#class the overide procedure from child through son
son.altered()#class the altered procedure from child through son

