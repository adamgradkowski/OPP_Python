class Tag(object):
	''' Tag klasa abstrakcyjna przedstawiajaca pojedynczy znacznik w pliku html

	Atrybuty:
		tag_start (str): poczatek znacznika
		tag_end (str): koniec znacznika
		content (str): zawartosc pomiedzy poczatkiem i koncem znacznika
	'''

	def __init__(self, name, contents = ''):
		'''Tag init method

		Args:
			name (str): nazwa znacznika 
			content (str): wybrana zawartosc znacznika
		'''
		self.start_tag = '<{}>'.format(name)
		self.end_tag = '</{}>'.format(name)
		self.contents = contents
		self.elem_content = []
		self.hierarhy = 0


	def add_elem(self, elem):

		self.elem_content.append(elem)

 
	'''
	def __str__(self):
		 metoda __str__ zwraca wszystkie atrybuty Tag'a
		

		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
	'''
	def display(self, file=None):
		''' wyswietla obiekt - siebie
		'''
		con = self.contents
		self.contents = ''
		print(self.start_tag)
		self.contents += self.start_tag #h1
		self.contents += '\n'
		self.contents += '\t'
		self.contents += con
		if self.elem_content:
			for elem in self.elem_content: #h2 #h5
				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.start_tag
				self.contents += '\n'
				self.contents += '\t\t'
				self.contents += elem.contents
				print(elem.start_tag + elem.end_tag)
				if elem.elem_content:
					for ele in elem.elem_content: #h3
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.start_tag
						self.contents += '\n'
						self.contents += '\t\t\t'
						self.contents += ele.contents
						print(ele.start_tag + ele.end_tag)
						if ele.elem_content:
							self.contents += '\n'
							for el in ele.elem_content: #h4
								self.contents += '\t\t\t'
								self.contents += el.start_tag
								self.contents += '\n'
								self.contents += '\t\t\t\t'
								self.contents += el.contents
								self.contents += '\n'
								self.contents += '\t\t\t'
								self.contents += el.end_tag
								print(el.start_tag + el.end_tag)
						else:
							print("nie ma")
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.end_tag

				else:
					print("nie ma")
				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.end_tag
		else:
			print("nie ma")
		print(self.start_tag)
		self.contents += '\n'
		self.contents += self.end_tag
		print("="*80)
		print(self.contents)
		#print(self, file=file)

	

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

	def add_tag(self, elem):
		''' Dodawanie nowego tagu do tablicy , tworzony jest nowy tag

		Args:
			name (str): nazwa tagu
			content (str): zawartosc tagu
		
		'''
		self.elem_content.append(elem)


	def display(self, file=None):
		'''
		dziedziczy metode display() po Tag'u, ponadto do atrybuty content dodawany sa zawartosc wszystkich Tag'ow z tablicy body_content
		'''

		#for tag in self._body_contents:
		#	self.contents += str(tag)

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

class Div(Tag):

	def __init__(self, cont = None):
		super().__init__('div','')
		self._div_contents = []
		if cont:
			self.contents = cont

	def add_tag(self,name,contents):
		new_tag = Tag(name,contents)
		self._div_contents.append(new_tag)
		for tag in self._div_contents:
			self.contents +=str(tag)

	def display(self, file=None):
		for tag in self._div_contents:
			self.contents += str(tag)
		super().display(file=file)



if __name__ == '__main__':
	'''
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
	'''
	'''
	tag = Tag('p', 'zawartosc')
	tag2 = Tag('h1', 'zawartosc2')
	tag3 = Tag('h2', 'zawartosc3')
	tag2.add_elem(tag3)
	body = Body()
	body.add_tag(tag)
	body.add_tag(tag2)
	body.display()
	'''
	h1 = Tag('h1','h1 naglowek')
	h2 = Tag('h2','h2 naglowek')
	h3 = Tag('h3','h3 naglowek')
	h4 = Tag('h4','h4 naglowek')
	h5 = Tag('h5','h5 naglowek')
	h6 = Tag('h6','h6 naglowek')
	h7 = Tag('h7','h5 naglowek')
	h8 = Tag('h8','h5 naglowek')
	h9 = Tag('h9','h5 naglowek')
	h10 = Tag('h10','h5 naglowek')
	h11 = Tag('h11','h5 naglowek')
	h12 = Tag('h12','h5 naglowek')
	h13 = Tag('h13','h5 naglowek')
	h14 = Tag('h14','h5 naglowek')
	h3.add_elem(h4)
	h2.add_elem(h6)
	h2.add_elem(h3)
	#h2.add_elem(h7)
	h1.add_elem(h2)
	h1.add_elem(h5)

	h1.display()
	

