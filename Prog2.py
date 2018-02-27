import bioinformatics

print bioinformatics.PctOfProtein("msrslllrfllfllllpplp", ["L"])
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) 
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) 