class Song:
	'''Class to represent a song

	Attritubes:
		title (str): The title of the song
		artist (Artist): An artist object - songs creator
		dutation(int): Duration/Len of the song
	'''

	def __init__(self, title, artist, duration=0):
		'''Song init method

		Args:
			title (str): init
			artist (Artist): init
			duration(Optional int) will default = 0 if not specified
		'''
		self.title = title
		self.artist = artist
		self.duration = duration

