# Importerar modulen random 
import random
# Skapar en seed för random modulens funktioner
random.seed()

# Öppnar textfilen
txt = open("stats.txt", "rt")
# Låter användaren välja det maximala antal sidor som tärningen har
dice_max = input("How many sides does your dice have?:")
# Variabel som fungerar som tärningen
roll = random.randint(1, int(dice_max))
# Läser textfilen
lines = txt.readlines()

# Definierar en annan funktion
def ObT6():
    if roll == 6 and int(dice_max) == 6:
        for x in range(3):
            return("bazinga")
ObT6() 