import BioinformaticsB
genomic_dna = open("genomic_dna.txt").read()

exon_locations = open("exons.txt")

coding_sequence = ""

for line in exon_locations:
    start = int(line[0:line.find(',')])
    stop = int(line[line.find(',')+1:])
    
    exon = BioinformaticsB.extractExon(genomic_dna, start, stop)
    
    coding_sequence = coding_sequence + exon
    
output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
