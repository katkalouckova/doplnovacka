with open("song.txt") as f:
	text = f.read()
f.closed

print(text)

text = text.replace("\n", "# ")

seznam = []
seznam = text.split(" ")
vysledek = []
interpunkce = ".,;?!-\""

print(seznam)

for i in range(len(seznam)):

	slovo = seznam[i]
	upravene_slovo = ""

	if ((i + 1) % 5 == 0):
		for pismeno in slovo:
			if pismeno not in interpunkce:
				upravene_slovo += "*"
			else:
				upravene_slovo += pismeno
		vysledek.append(upravene_slovo)

	else:
		vysledek.append(slovo)

s = " ".join(vysledek)
s = s.replace("#", "\n")

print(s)
