def vytvor_doplnovacku(text, zamena):
	"""
	Kazdy xty(dle parametru zamena) znak v textu nahradi znakem hvezdicky
	a zmeneny text vrati
	:param text:
	:param zamena:
	:return:
	"""

	text = text.replace("\n", "# ")

	seznam = text.split(" ")
	vysledek = []
	interpunkce = ".,;?!-\""

	for i in range(len(seznam)):

		slovo = seznam[i]
		upravene_slovo = ""

		if (i + 1) % 5 == 0:

			for pismeno in slovo:
				if pismeno not in interpunkce:
					upravene_slovo += "*"
				else:
					upravene_slovo += pismeno

			vysledek.append(upravene_slovo)

		else:
			vysledek.append(slovo)

	text = " ".join(vysledek)
	text_se_zamenami = s.replace("*", "\n")

	return text_se_zamenami


with open("song.txt") as f:
	text = f.read()

zmeneny_text = vytvor_doplnovacku(text, zamena)

print(zmeneny_text)
