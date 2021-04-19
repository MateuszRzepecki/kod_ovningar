f = open("stats.txt", "rt")  # öppnar filen och läser ifrån den​
str = "Smidighet:"  # Bestämmer strängen som ska sökas efter​
# line_number = -1​
# smidighet_line = 0​
# Loopar igenom alla strängarna och letar efter str​
for line in f:
    ​
# line_number += 1​
if str in line:  # Checkar om den hittar str och isf printar linjen med str i.​
print(line[11:13])  # ser till så koden bara printar en viss del av line​
