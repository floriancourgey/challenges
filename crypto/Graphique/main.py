s = "FDPJ RBXRHJJ JBNJJZ NDZRXXB"
mot = ""
mot2 = ""

for c in s:
	if c == " ":
		mot = mot + " "
		mot2 = mot2 + " "
		continue
	c_ascii = ord(c) - ord('A')
	resultat = (c_ascii-1)/2
	resultat2 = (c_ascii+26-1)/2
	lettre = chr(resultat + ord('A'))
	lettre2 = chr(resultat2 + ord('A'))
	mot = mot + lettre
	mot2 = mot2 + lettre2
	print(c+" ascii_"+str(c_ascii)+" resultat_"+str(resultat)+"  "+lettre+" ou "+lettre2)

print(mot)
print(mot2)
print("POUR VALIDER ENTREZ GOZILLA")
