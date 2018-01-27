# Programmed by Marisa Nickerson for Bioinformatics
# DNA sequence
print "Please enter DNA sequence"
DNA = raw_input()
DNA = DNA.upper()
A = DNA.count('A')
T = DNA.count('T')
length = len(DNA)
content = int(A + T)/float(length)
print "The AT content is %.2f" % content
