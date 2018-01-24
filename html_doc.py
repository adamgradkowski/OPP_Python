class Tag(object):
	''' Tag klasa abstrakcyjna przedstawiajaca pojedynczy znacznik w pliku html

	Atrybuty:
		tag_start (str): poczatek znacznika
		tag_end (str): koniec znacznika
		content (str): zawartosc pomiedzy poczatkiem i koncem znacznika
	'''

	def __init__(self, name, contents = '', id_tag = None, class_tag = None):
		'''Tag init method

		Args:
			name (str): nazwa znacznika 
			content (str): wybrana zawartosc znacznika
		'''
		if id_tag and class_tag:
			self.start_tag = '<{} id="{}" class="{}">'.format(name, id_tag, class_tag)
		elif class_tag:
			self.start_tag = '<{} class="{}">'.format(name, class_tag)
		elif id_tag:
			 self.start_tag = '<{} id="{}">'.format(name, id_tag)
		else:
			self.start_tag = '<{}>'.format(name)

		self.id = id_tag
		self.clas = class_tag
		self.end_tag = '</{}>'.format(name)
		self.contents = contents
		self.elem_content = []
		self.tag_style = {}

	def add_elem(self, elem):

		self.elem_content.append(elem)

	def add_style(self, name, value):
		self.tag_style.update({name:value})

	

 
	
	def __str__(self):
		''' metoda __str__ zwraca wszystkie atrybuty Tag'a
		'''

		return "{0.start_tag}{0.contents}{0.end_tag}".format(self)
	
	def display(self, file=None):
		''' wyswietla obiekt - siebie
		'''
		
		if self.elem_content:
			for elem in self.elem_content: #h2 #h5
				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.start_tag
				self.contents += '\n'
				self.contents += '\t\t'
				self.contents += elem.contents
				if elem.elem_content:
					for ele in elem.elem_content: #h3
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.start_tag
						self.contents += '\n'
						self.contents += '\t\t\t'
						self.contents += ele.contents
						if ele.elem_content:
							for el in ele.elem_content: #h4
								self.contents += '\n'
								self.contents += '\t\t\t'
								self.contents += el.start_tag
								self.contents += '\n'
								self.contents += '\t\t\t\t'
								self.contents += el.contents
								self.contents += '\n'
								self.contents += '\t\t\t'
								self.contents += el.end_tag
						self.contents += '\n'
						self.contents += '\t\t'
						self.contents += ele.end_tag

				self.contents += '\n'
				self.contents += '\t'
				self.contents += elem.end_tag

		self.contents += '\n'
		#self.contents += self.end_tag
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

	def add_style(self, name):
		style = '<link rel="stylesheet" href=' + name + '">'
		self.contents += style
		print(style)

class Style(object):

	def __init__(self, name):
		self.name = name
		self.elements = []
		self.content = ''

	#def __str__(self):
	#	return "{0.name}".format(self)

	def add_elem(self, name):
		self.elements.append(name)

	def display(self, file=None):
		print(self.content)
		for element in self.elements:
			if type(element) is Tag:
				print(element)
				if element.id is not None and element.clas is not None:
					self.content = self.content + '#' + element.id + '.' + element.clas + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values +';' + '\n'
					self.content += '}'
				elif element.clas is not None:
					self.content = self.content + '.' + element.clas + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values +';' + '\n'
					self.content += '}'
				elif element.id is not None:
					self.content = self.content + '#' + element.id + ' {' + '\n'
					for keys,values in element.tag_style.items():
						self.content = self.content + keys + ' : ' + values  +';' + '\n'
					self.content += '}'
			self.content += '\n'
					#print('#'+element.id + '{' + '\n' + str(element.tag_style) + '}')
		#print(content)
			#el = str(element) + ' {\n}\n'
			#self.content += el 

		print(self.content)
		print(self.content, file=file)





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
	body = Body()
	new_docType = DocType()
	new_header = Head('Aggregat title')
	my_page = HtmlDoc(new_docType, new_header, body)

	div1 = Tag('div','div')
	h1 = Tag('h1','glowny naglowek')
	div11 = Tag('div','div')
	p1 = Tag('p', 'Tekst')
	p2 = Tag('p', 'Tekst')
	div11.add_elem(p1)
	div11.add_elem(p2)
	div1.add_elem(h1)
	div1.add_elem(div11)

	div2 = Tag('div','div')
	h2 = Tag('h2','glowny naglowek')
	div22 = Tag('div','div')
	p3 = Tag('p', 'Tekst')
	p4 = Tag('p', 'Tekst')
	div22.add_elem(p3)
	div22.add_elem(p4)
	div2.add_elem(h2)
	div2.add_elem(div22)

	div3 = Tag('div','div')
	h3 = Tag('h3','glowny naglowek')
	div33 = Tag('div','div')
	p5 = Tag('p', 'Tekst')
	p6 = Tag('p', 'Tekst')
	div33.add_elem(p5)
	div33.add_elem(p6)
	div3.add_elem(h3)
	div3.add_elem(div33)


	body.add_tag(div1)
	body.add_tag(div2)
	body.add_tag(div3)
	body.display()

	with open('index.html', 'w') as test_doc3:
		my_page.display(file=test_doc3)
	'''
	div = Tag('div', 'zawartosc', id_tag='id_tag', class_tag='class_tag')
	div.add_style('font','normal')
	div.add_style('background','unnormal')
	#div.display()

	div2 = Tag('div', 'nowosc', id_tag='id_tag2')
	div2.add_style('font','black')
	div2.add_style('background','green')
	
	body = Body()
	new_docType = DocType()
	new_header = Head('Aggregat title')
	#new_header.add_style('mystyle.css')
	my_page = HtmlDoc(new_docType, new_header, body)
	#my_page.display()
	style = Style('mystyle.css')
	style.add_elem(div)
	style.add_elem(div2)
	#style.add_elem('h1')
	#style.display()

	with open('mystyle.css', 'w') as style_:
		style.display(file=style_)
	