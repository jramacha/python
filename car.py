#!/usr/bin/env python

import time



class Car:
	"""
	simple Car class
	"""

	def __init__(self, make, model, year):
		self._make = make
		self._model = model
		self._year = year


	def get_make(self):
		return self._make


	def get_model(self):
		return self._model

	def get_year(self):
		return self._year


	def drive(self):
		print "Driving.. " + self._make

	def start(self):
		print "Starting.. " + self._make	

	def stop(self):
		print "Stopping.. " + self._make	

def findin_s(lst, item):
	for val in lst:
		if item in lst:
			return True
	return False		

class Flower:
	def __init__(self, name, petals, price):
		self._name = name
		self._petals = petals
		self._price = price

	def set_name(self, name):
		print 'setting name..' + name 
		self._name = name

	def set_name(self, petals):
		self._petals = petals
	
	def set_name(self, price):
		self._price = price
	
	def get_name(self):
		return self._name		

def main():
	i = 0;
	var = 'my_car'+str(i) 
	print var
	# import pdb;pdb.set_trace();
	var = Car('Ferrari', 'Enzo', 2017)
	var.start();
	var.stop();
	i += 1
	print findin_s([15,12,13,10,11,12,2323,1], -11)

	myflower = Flower('Andy',11,12.0)
	print myflower.get_name()

if __name__ == '__main__':
	main()
