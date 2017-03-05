#creating a list for saving the palindromes
p = []
n = 0
sum = []
prodarray = []
multiply = 0

#checking for all the pallindromes in the given range
def Palindrome_Checker():
	for i in range(10, 1000):
		n = i
		rev = 0
		while(i > 0):
			dig = i%10
			rev = rev * 10 + dig
			i = i / 10
		if n == rev:
			p.append(n)

Palindrome_Checker()  #calling the palindrome function

l = len(p)
for i in range(0,99):
	for j in range (i+1, l):
		for k in range (j+1, l):
			for m in range (k+1, l):
				sum = p[i]+p[j]+p[k]+p[m]
                #checking if the sum is a pallindrome
				n = sum
				rev = 0
				while(sum > 0):
					dig = sum%10
					rev = rev * 10 +dig
					sum = sum / 10
					if n == rev:        #only if the sum is palindrome, multiply
						mul = p[i]*p[j]*p[k]*p[m]
						a = p[i]
						b = p[j]
						c = p[k]
						d = p[m]
						if mul > multiply:
							multiply = mul
print multiply
print a
print b
print c
print d