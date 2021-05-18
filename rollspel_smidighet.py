f = open("stats.txt", "rt")
lines = f.readlines()
for line in lines:
    if "Agility:" in line:
        print(line.strip()[-2:])
f.close()
