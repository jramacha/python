#!/usr/local/bin/python3.6


class allfiles:
	
	def __init__(self): 
		self._files = []

	def pop_fl(self):
		if not self.isempty():
			return self._files.pop()
		else:
			print ('No more files')	

	def push_fl(self, name):
		self._files.append(name)	

	def isempty(self):
		return len(self._files) == 0


class median:
	
	def __init__(self, num, avg): 
		self._dic = {} # map to store count and mean

	def get_mean(self):
		total = 0
		ct = 0
		for k,v in self._dic.items():
			total += k * v 
			ct += v
		return total / ct	



def main():
	myfl = generate_fl(0, 10, 100, 100)
	myfl.write_to_fl()

if __name__ == '__main__':
	main()			