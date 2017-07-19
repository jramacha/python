#!/usr/local/bin/python3.6


mfmp = 10 
balance = 4497
annualInterestRate = 0.04

while True:
	bal = balance
	for i in range(1,13):
		if bal < 0:
			# print('Lowest Payment: ', mfmp)
			break
		mir  = round(annualInterestRate / 12, 2)
		mub  = round((bal - mfmp), 2)
		bal = mub + round((mir * mub),2)	
		# print ('balance: ', bal)

		
	if bal <= 0:
		# import pdb; pdb.set_trace();
		
		print('Lowest Payment: ', mfmp)
		# print('balance: ', bal)
		break
	if bal > 0:
		mfmp += 10			


# def main():
# 	# minimum_payment()
# 	payingoff()



# if __name__ == '__main__':
# 	main()