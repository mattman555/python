import mystuff #Bring in the my stuff programs procdure

myStuff = {'apple': "apples"} #Create dictionary containing the word apple with the name apple

class Mystuff(object): #Make a class with the name Mystuff
	
	def __init__(self): #an initialization procedure with the object self
		self.tangerine = "And now a thousand years between" #make an variable tangerine containing the string
	
	def apple(self): #procedure with the object self
		print "I AM CLASSY APPLES!"
		

thing = Mystuff() #give thing all the propreties of the Mystuff class
thing.apple() #call the apple procedure from the Mystuff class through thing
print thing.tangerine #print the contents of the tangerine variable
print myStuff['apple'] #Print what is under the apple keyword in the myStuff dictionary
mystuff.apple() #run the apple procedure imported from the mystuff module
print mystuff.tangerine #print the tangerine variable from the mystuff module

