import BioinformaticsA
file = open("data.csv", "r")

for line in file:
   genes = line.rstrip('\n').split(",")
   name = genes[0]
   sequence = genes[1]
   nameofgene = genes[2]
   expression = genes[3]
   ATcontent = BioinformaticsA.atContent(sequence)
   if BioinformaticsA.HighAT(ATcontent) == True:
       print "Gene is %s" % name + " High AT content is %.2f" % ATcontent
   elif BioinformaticsA.MedAT(ATcontent) == True:
        print "Gene is %s" % name + " Med AT content is %.2f" % ATcontent
   elif BioinformaticsA.LowAT(ATcontent) == True:
       print "Gene is %s" % name + " Low AT content is %.2f" % ATcontent

   

   




    
    