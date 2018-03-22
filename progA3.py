import BioinformaticsA
file = open("data.csv", "r")

for line in file:
    genes = line.split(",")
    content = BioinformaticsA.atContent(genes[1])
    if content > 0.65:
        print genes[0], "high"
    elif content > 0.45 or content <= 0.65:
        print genes[0], "Med"
    else:
        print genes[0], "Low"

   




    
    