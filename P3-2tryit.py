genomic_dna = open("genomic_dna.txt").read()
exons_locations = open("exons.txt")

coding_sequence = ""

for line in exons_locations:
    start = int(line[0:line.find(',')])
    stop = int(line[line.find(',')+1:])
   
    exon = genomic_dna[start:stop]
    coding_sequence = coding_sequence + exon
    
output = open("coding_sequence.txt", 'w')
output.write(coding_sequence)
output.close()
