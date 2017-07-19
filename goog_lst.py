#!/usr/local/bin/python3.6

def calc_val(lst_lcl, idx, vals):
	if len(lst_lcl) == 1:
		return lst_lcl[0]
	val_lcl = 1
	if len(lst_lcl) % 2 == 1: ##skip by 2 ( product of next 2 items after current)
		for i in range(len(lst_lcl)-2):
			if i % 2 == 0:
				val_lcl = val_lcl * vals[i + idx] [(i+1) + idx] # lookup in vals saved values

		val_lcl *= lst_lcl[len(lst_lcl)-1]	

	else:
		for i in range(len(lst_lcl)-1):
			if i % 2 == 0:
				val_lcl = val_lcl * vals[i + idx] [(i+1) + idx] # lookup in vals saved values

	return val_lcl		


def main():
	# lst = [1,3,6,2,5,6,7,8,1,3,6,2,5,6,7,8]
	# lst = [1,2,3,4,5]
	# lst = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
	lst = [5,5,5,5,5,5,5,5,5,5,1,1]
	new = []
	vals = [[0]*len(lst) for i in range(len(lst))] #2D-array to keep values for lookup

	for i in range(len(lst)):
		for j in range( i+1, len(lst)):
			vals[i][j] = lst[i] * lst[j]

	for i in range(len(lst)):
		# import pdb;pdb.set_trace();
		if i == 0:
			new.append(calc_val(lst[i+1:], i+1, vals)) # values to right of index"""	
		else:	
			new.append(calc_val(lst[0:i], 0, vals)*calc_val(lst[i+1:], i+1, vals)) #values to left of index"""	

	# if new == [120, 60, 40, 30, 24]:
	print(new)		


if __name__ == '__main__':
	main()