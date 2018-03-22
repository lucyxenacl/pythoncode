f = open('FASTA.txt' , 'w')
f.write('>ABC123' + '\n')
f.write('ATCGTACGATCGATCGATCGCTAGACGTATCG' + '\n')
f.write('>DEF456' + '\n')
f.write('ACTGATCGACGATCGATCGATCACGACT' + '\n')
f.write('>HIJ789' + '\n')
f.write('ACTGACACTGTACTGTACATGTG')

f.close()