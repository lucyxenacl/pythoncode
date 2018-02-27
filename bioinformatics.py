def PctOfProtein(Protein, codes):
    Protein=Protein.upper()
    c=0 
    for aa in codes:
        aa=aa.upper()
        c = c+Protein.count(aa)
    return(c/float(len(Protein))*100)