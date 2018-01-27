#Programmed by Marisa Nickerson for Bioinformatics

DNA = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ecoR1 = "GAATTC"
cut = DNA.find(ecoR1) + 1
fragment1 = cut
fragment2 = len(DNA)-cut
print "Length of sequence with cut is %s" % fragment1
print "Length is sequence without cut is %s" % fragment2