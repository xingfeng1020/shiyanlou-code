for n in range(1,101):
	if n%10==7 or n%7==0 or int(n/10)%10==7:# n//10==7
		continue
	print(n)

	