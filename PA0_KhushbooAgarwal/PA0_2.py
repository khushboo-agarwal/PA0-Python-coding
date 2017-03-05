from random import *
lb = 1
ub = input("Enter the upper bound for (1,X):  ")
print("Select an integer between (1,X) in your mind ")
user_input = ''
b = 0
tries = 0
while((user_input.upper())!='W'):
	b = int((lb+ub)/2)
	print b
	tries = tries +1
	user_input = raw_input("is this lower or higher than your guessed value  ")
	if((user_input.upper())=='L'):
		lb=b
	if((user_input.upper())=='H'):
		ub=b
if((user_input.upper()) == 'W'):
	print("Correct")
	print tries