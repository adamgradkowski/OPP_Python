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


class Album:
	'''Class to represent Album, using track list

	Attributes:
		name(str): The name of the album
		year(int): Year when album was created
		artist(Artist): The artist who created the album. If not specified the artist will be default with name "Various Artists"
		tracks (List[Song]): A list of the songs
	
	Methods:
		add_song: Used to add a new song to the album's track list.
	'''

	def __init__(self, name, year, artist=None):
		self.name = name
		self.year = year
		if artist is None:
			self.artist = Artist('Various Artist')
		else:
			self.artist = artist
		self.tracks = []

	def add_song(self, song, position=None)
		'''Adds a song to the track list

		Args:
			song (Song): song to add
			position(Optional[int]): If specified, the song will be added on the position if not will be added on the end
		'''
		if position is None:
			self.tracks.append(song)
		else:
			self.tracks.assert(position, song)


#help(Song) # doc class

