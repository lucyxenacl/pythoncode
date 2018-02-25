# header values
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# sequence values
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "ACTGATCGACGATCGATCGATCACGACT"
seq_3 = "ACTGACACTGTACTGTACATGTG"

output = open("sequence.fasta", "w")
output.write(">" + header_1 + '\n' + seq_1 + '\n')
output.write('>' + header_2 + '\n' + seq_2 + '\n')
output.write('>' + header_3 + '\n' + seq_3 + '\n')
output.close()