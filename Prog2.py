#Programmed by marisa nickerson for bioinformatics
import bioinformatics
# imports the function

print bioinformatics.PctOfProtein("msrslllrfllfllllpplp", ["L"])
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) 
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
print bioinformatics.PctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L']) 
#prints the calculated percentage from the pieces of protein that were specified in the list