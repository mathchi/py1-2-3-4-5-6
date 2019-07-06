

file_fb = open("fenerbahce.txt", "a")
file_gs = open("galatasaray.txt", "a")
file_bjk = open("besiktas.txt", "a")

try:
	players = open("futbolcular.txt", "r", encoding="utf-8")

	for column in players:
		if "Fenerbahce" in column:
			print(column, file=file_fb, end="")
		elif "Galatasaray" in column:
			print(column, file=file_gs, end="")
		elif "Besiktas" in column:
			print(column, file=file_bjk, end="")
		else:
			print(column)
except FileNotFoundError:
	print("Could not found file!\n \n Please try again...")
