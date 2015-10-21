with open("positive.txt", "r") as f:
	positive = f.read().strip().splitlines()
	f.close()
	for line in positive:
		print ('c(' + '\'' + line + '\'' + ',' + '\'positive\'' + ')' +',')
