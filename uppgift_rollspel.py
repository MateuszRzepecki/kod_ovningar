f = open("stats.txt", "rt")
lines = f.readlines()
for line in lines:
    if "Smidighet:" in line:
        print(line.strip()[-2:])
f.close()
