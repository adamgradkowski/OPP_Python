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

	def get_title(self):
		return self.title

	name = property(get_title)


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

	def add_song(self, song, position=None):
		'''Adds a song to the track list

		Args:
			song (Song): the title to add
			position(Optional[int]): If specified, the song will be added on the position if not will be added on the end
		'''
		song_found = find_object(song, self.tracks)
		if song_found is None:
			song_found = Song(song,self.artist)
			if position is None:
				self.tracks.append(song_found)
			else:
				self.tracks.issert(position, song_found)


class Artist:
	'''
	Adam: uzupelnij dokumentacje
	'''
	def __init__(self, name):
		self.name = name
		self.albums = []

	def add_album(self, album):
		'''Adam: uzupelnij dokumentacje
		'''
		self.albums.append(album)

	def add_song(self, name, year, title):
		"""Add a new song to the collection of albums
		
		New album will be created in the collection if it doesnt exist already

		Args:
			name (srt): Name album
			year (int): Year album
			title (str): title of song
		"""
		album_found = find_object(name, self.albums)
		if album_found is None:
			print(name + " not found")
			album_found = Album(name, year, self)
			self.add_album(album_found)
		else:
			print("found album " + name)
		album_found.add_song(title)



def find_object(field, object_list):
	'''Check 'object_list' to see if object 'name' equal to field exist, return it if so'''
	for item in object_list:
		if item.name == field:
			return item
	return None

def load_data():
	
	artist_list = []

	with open("albums.txt", "r") as albums:
		for line in albums:
			#data row should consit of (artist, album, year, song)
			artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
			year_field = int(year_field)
			#print(artist_field, album_field, year_field, song_field)

			new_artist = find_object(artist_field,artist_list)
			if new_artist is None:
				new_artist = Artist(artist_field)
				artist_list.append(new_artist)

			new_artist.add_song(album_field, year_field, song_field)


		

	return artist_list #Adam: szukaj innego rowiazania tego load'a


def create_check_file(artist_list):
	"""Create a check file to compare with original file"""
	with open("checkfile.txt", 'w') as checkfile:
		for new_artist in artist_list:
			for new_album in new_artist.albums:
				for new_song in new_album.tracks:
					print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)
if __name__ == '__main__':
	artists = load_data()
	create_check_file(artists)
	'''for a in artists:
		print("*" * 80)
		print(a.name)
		for i in a.albums:
			print(i.name)
			for song in i.tracks:
				print(song.title)
		print("*" * 80)
	'''
#help(Song) # doc class

