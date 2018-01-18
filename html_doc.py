class Tag(object):
	''' Tag klasa abstrakcyjna przedstawiajaca pojedynczy znacznik w pliku html

	Atrybuty:
		tag_start (str): poczatek znacznika
		tag_end (str): koniec znacznika
		content (str): zawartosc pomiedzy poczatkiem i koncem znacznika
	'''

	def __init__(self, name, contents):
		'''Tag init method

		Args:
			name (str): nazwa znacznika 
			content (str): wybrana zawartosc znacznika
		'''
		self.start_tag = '<{}>'.format(name)
		self.end_tag = '</{}>'.format(name)
		self.contents = contents

	def __str__(self):
		''' metoda __str__ zwraca wszystkie atrybuty Tag'a
		'''

		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

	def display(self, file=None):
		''' wyswietla obiekt - siebie
		'''

		print(self, file=file)

class DocType(Tag):

	def __init__(self):
		super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd','')
		self.end_tag = ''

class Head(Tag):

	def __init__(self, title=None):
		super().__init__('head', '')
		if title:
			self._title_tag = Tag('title', title)
			self.contents = str(self._title_tag)

class Body(Tag):
	'''Klasa Body reprezentujaca reprezentujaca cala czesc 'fizyczna' pliku html

	Atrybuty:
	dziedziczone:
		name (str): nazwa 'body'
		content (str): zawartosc czesc body
	nowe:
		body_content([]): tablicza przechowyjaca znaczniki
 	'''

	def __init__(self):
		''' Body init method

		Args:
		name (str) : body
		content(str) : wpowadzana zawartosc
		content_body([]) : dodawane elementy
		'''
		super().__init__('body', '')
		self._body_contents = []

	def add_tag(self, name, contents):
		''' Dodawanie nowego tagu do tablicy , tworzony jest nowy tag

		Args:
			name (str): nazwa tagu
			content (str): zawartosc tagu
		
		'''

		new_tag = Tag(name, contents)
		self._body_contents.append(new_tag)

	def display(self, file=None):
		'''
		dziedziczy metode display() po Tag'u, ponadto do atrybuty content dodawany sa zawartosc wszystkich Tag'ow z tablicy body_content
		'''

		for tag in self._body_contents:
			self.contents += str(tag)

		super().display(file=file)

class HtmlDoc(object):
	'''klasa reprezentujaca caly plik html 

	Atrybuty:
	_doc_type (DocType) : info o pliku html
	_head (Head): czesc head pliku html
	_body (Body): czesc body pliku html

	'''

	def __init__(self, doc_type, head, body):
		'''Method __init__

		'''
		self._doc_type = doc_type
		self._head = head
		self._body = body

	def add_tag(self, name, contents):
		''' do czesc Body() uzywana jest metoda ktora dodaje elementy Tag() do tablicy
		'''
		self._body.add_tag(name, contents)

	def display(self, file=None):
		'''Wykorzystanie metody display() kazdego z agregatu
		'''
		self._doc_type.display(file=file)
		print('<html>', file=file)
		self._head.display(file=file)
		self._body.display(file=file)
		print('</html>', file=file)


if __name__ == '__main__':
	new_body = Body()
	new_body.add_tag('h1', 'Agggregat')
	new_body.add_tag('p', 'saldhsadhsad')
	new_body.add_tag('p', "<dasdsadas <strong> Composition </strong>")
	new_body.add_tag('p', "<dasdsadas <strong> Composition </strong>")

	new_docType = DocType()
	new_header = Head('Aggregat title')
	my_page = HtmlDoc(new_docType, new_header, new_body)

	with open('test3.html', 'w') as test_doc3:
		my_page.display(file=test_doc3)

