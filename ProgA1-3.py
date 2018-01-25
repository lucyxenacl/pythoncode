#Programmed by Marisa Nickerson for Bioinformatics

print "Please Enter DNA sequence"
DNA = raw_input()
compliment = DNA.replace('A', 't')
compliment = compliment.replace('T', 'a')
compliment = compliment.replace('G', 'c')
compliment = compliment.replace('C', 'g')
UpperCompliment = compliment.upper()
print "This is the compliment to the sequence %s" % UpperCompliment