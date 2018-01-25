# Programmed by Marisa Nickerson for Bioinformatics
# DNA sequence
print "Please enter DNA sequence"
DNA = raw_input()
len(DNA)
print "The legnth is %s" % len(DNA)
DNA.count('A')
print "A equals %s" % DNA.count('A')
DNA.count('T')
print "T equals %s" % DNA.count('T')

A = 16
T = 20
print "The AT content is %s" % (int(A)+int(T)/53)