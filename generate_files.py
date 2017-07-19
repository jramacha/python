#!/usr/local/bin/python3.6


"""
generate large number of files with numbers
pass mean and std
"""

import random

class generate_fl:
	
	def __init__(self, size, mean, std, count = 10): 
		self._size = size ##size in gb for large files
		self._mean = mean 
		self._std_dev = std
		self._ct  = count

	
	def write_to_fl(self):

		if self._size == 1:
			rg = 100000000 ## for large files
			print('generating large files')	
		else:
			rg = 100 ## small files	
			print('generating small files')	

		for i in range(self._ct):
			name = 'files/nums_'+str(i)+'.txt'
			with open(name, 'a') as fl:
				for i in range(rg):
					num = str(random.gauss(self._mean, self._std_dev))
					fl.write(num+'\n')


def main():
	myfl = generate_fl(0, 10, 100, 100)
	myfl.write_to_fl()

if __name__ == '__main__':
	main()					