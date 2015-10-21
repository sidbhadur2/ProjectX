with open("l6.txt", "r") as f:
	l5= f.read().strip().splitlines()
	f.close()
	for line in l5:
		#print ('c(' + '\'' + line + '\'' +', '+ '\' \'' + ')' +',')
		print ('\'' + line + '\'' )
