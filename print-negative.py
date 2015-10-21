with open("negative.txt", "r") as f:
	negative = f.read().strip().splitlines()
	f.close()
	for line in negative:
		print ('c(' + '\'' + line + '\'' + ',' + '\'negative\'' + ')' +',')
