#!/usr/bin/python

def  return_uniq(val):
	uniq=[]
	
	for i in range(0,len(val)):
		if val[i] not in uniq:
			uniq.append(val[i])
	return uniq

			

lst =[2,22,2,3,4]

new = return_uniq(lst)

print new 