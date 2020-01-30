



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
	d = {}
	for name, seq in readMultilineFASTA("/Users/awhaley9/Downloads/Mdomestica_491_v1.1.cds_primaryTranscriptOnly.fa"):
	   	d[name] = seq
	print(len(d.keys()))



if __name__ == '__main__':
    main()
