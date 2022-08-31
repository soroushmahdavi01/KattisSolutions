# OUR OUTPUT / OUR 1st INPUT = OUR SECOND INPUT
# X / 38 = 24 

cpuin = input()
cpudex = cpuin.split(' ')

articles = int(cpudex[0])
faktor = int(cpudex [1])

prescore = articles * faktor
faktor = faktor - 1
while (prescore / articles) > faktor :
    prescore = prescore - 1
    

prescore = prescore + 1
    

print(prescore)