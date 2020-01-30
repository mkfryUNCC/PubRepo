



def readMultilineFASTA(file):

	fh = open(file)

	name = None
	seq = ""


	for line in fh:
		if line.startswith(">"):
			if name:
				
				yield (name,seq)
				name = None
				seq = ""

			name = line.rstrip().lstrip(">")

		else:
			seq += line.rstrip()
			

	yield name,seq



def main():
    filepath = intput("enterPath")
	d = {}
	for name, seq in readMultilineFASTA(filepath):
	   	d[name] = seq
	print(len(d.keys()))



if __name__ == '__main__':
    main()
