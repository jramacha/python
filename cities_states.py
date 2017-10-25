#!/usr/local/bin/python3.6

class entries:
	
	def __init__(self, capacity):
		self._n = 0
		self._obj = [None] * capacity

	def add(self, cities):
		self._obj[self._n] = cities
		self._n += 1

	def __str__(self):
		# import pdb;pdb.set_trace();
		"""Return string representation of the high score list."""
		return '\n'.join(str(self._obj[j]) for j in range(self._n))	

class citiesLived:
	
	def __init__(self, city, state, year):
		self.city = city
		self.state = state
		self.year = year

	def __str__(self):
		"""Return string representation of the entry."""
		return '({0}, {1}, {2})'.format(self.year, self.city, self.state) # e.g., '(98, honda, accord)' 

ent = entries(10)

for val in ( ('Baton Rouge',('Louisiana', 2003)),
	('Irving',('Texas', 2005)),
	('Cincinnati',('Ohio', 2006)),
	('Akron',('Ohio', 2006)),
	('Minneapolis',('Minnesota', 2007)),
	('Cleveland',('Ohio', 2007)),
	('New York',('New York', 2011)),
	('Springfield',('New Jersey', 2016)),



	):
	cities = citiesLived(val[0], val[1][0], val[1][1])
	ent.add(cities)
	print('After adding {0}, we have :'.format(cities))
	print(ent)
	print()




		