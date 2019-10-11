import re

with open("items.txt", "r") as infile:
	line = infile.readlines()
	for i in line:
#		print("https://www.albion-online-data.com/api/v2/stats/prices/" + i.split(": ")[1])
		with open("urls.txt", "a") as outfile:
			outfile.write("https://www.albion-online-data.com/api/v2/stats/prices/" + i.split(": ")[1] + "\n")
