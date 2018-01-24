print "How many Malcrops did you find on planet Exflon?",
Exflon = raw_input()
print "How many Malcrops did you find on planet Mobiles?",
Mobiles = raw_input()
print "How many Malcrops did you find on planet Monsantoes?",
Monsantoes = raw_input()

total = int(Exflon) + int(Mobiles) + int(Monsantoes)
print "You found %s malcrops!" % total
print "The average Malcrops per planet is %.2f." % (total / 3.0)