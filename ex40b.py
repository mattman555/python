class Song(object):#make a class named Song

	def __init__(self,lyrics): #initialization procedure with the self object and lyrics
		self.lyrics = lyrics
		
	def sing_me_a_song(self):#procedure to print the lyrics line by line
		for line in self.lyrics:
			print line
			

happy_bday = Song(["Happy birthday to you",   #making a variable to fill the lyrics in the song class
		   "I don't want to get sued",
		   "So I'll stop right there"])
		   
bulls_on_parade = Song(["They rally around tha family",
			"With pockets full of shells"])
			
happy_bday.sing_me_a_song()#call the sing a song procedure from the Song class 

bulls_on_parade.sing_me_a_song()
