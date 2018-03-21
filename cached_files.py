#!/usr/local/bin/python3.6
#Sample utility to cache files
import sys

class Filecontent:
	
	def __init__(self, name):
		self._name  = name;
		self._usage = 0
		self._content = []
		self.get_content(self._name)

	def get_content(self, fl):
		lcl_content = ()
		with open(fl, 'r') as fp:
			for ln in fp:
				lcl_content += (ln,)
		
		self._content.append(lcl_content)

	def size(self, i):
		return sys.getsizeof(self._content[0])				

	def get_name(self):
		return self._name

	def get_usage(self):
		return self._usage

	def return_content(self):
		self._usage += 1
		return self._content	

class cachedfl:

	def __init__(self, number):
		self._fl = [None]  * number
		self._n  = 0
		self._total_size = 0

	def __str__(self):
		"""Return string representation of the high score list."""
		return '\n'.join(str(self._fl[j]) for j in range(self._n))	

	def size(self):
		size = 0 
		for i in range(self._n-1):
			size += self._fl[i].size(i)

		self._total_size = size

		return size	

	def get_cache_size(self):
		return self._total_size		

	def get_least_frequently_used(self):
		lfu = 20000000
		lfu_name = ''
		for i in range(len(self._fl)-1):
			# import pdb; pdb.set_trace();
			if self._fl[i] is not None:
				if lfu > self._fl[i].get_usage():
					lfu = self._fl[i].get_usage()
					lfu_name = self._fl[i].get_name()
					obj = self._fl[i]
		return (lfu_name, obj)			

	def cache(self, entry):
		self._n += 1
		usage = entry.get_usage()
		import pdb; pdb.set_trace();


		if usage == 0: 
			if self.get_cache_size() < 3000:
				self._fl[self._n-1] = entry
			else:
				"""remove least used item from cache"""	
				item = self.get_least_frequently_used()
				print("Least frequently used: ", self.get_least_frequently_used()[0])

				self._fl.remove(item[1])
				self._n -= 1
				self._fl[self._n-1] = entry



def main():
	myfiles = cachedfl(6)
	fc = Filecontent('high_scores.py')
	myfiles.cache(fc)
	print(myfiles.size())
	print(fc.return_content())
	print(fc.return_content())
	print(fc.return_content())
	print(fc.get_usage())
	fc1 = Filecontent('caesar.py')
	myfiles.cache(fc1)
	print(myfiles.size())
	print(fc1.return_content())

	fc2 = Filecontent('cached_files.py')
	myfiles.cache(fc2)
	print(fc2.return_content())
	print(fc2.return_content())
	print(myfiles.size())

	fc3 = Filecontent('tic_tac_toe.py')
	myfiles.cache(fc3)
	print(myfiles.size())
	print(fc3.return_content())

	fc4 = Filecontent('experiment_list_append.py')
	myfiles.cache(fc4)
	print(myfiles.size())

	fc5 = Filecontent('experiment_list_size.py')
	myfiles.cache(fc5)
	print(fc5.return_content())
	print(fc5.return_content())

	print(myfiles.size())
	print("Least frequently used: ", myfiles.get_least_frequently_used())

	print(myfiles.get_cache_size())

	print(myfiles)


if __name__ == '__main__':
  main() 								
