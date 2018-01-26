#Programmed by Marisa Nickerson for Bioinformatics
#DNA coding seqeuence to show introns and exons
#uppercase shows bases that code in the DNA, lowercase shows the noncoding bases.
print "please enter DNA sequence"
DNA = raw_input()
coding = DNA[0:64].upper()
intron = DNA[64:92].lower()
exon = DNA[91:].upper()
sequence = coding+intron+exon
print "The exon and intron DNA sequence is %s" % sequence 