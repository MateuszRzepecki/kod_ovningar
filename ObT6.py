import random
# Importerar random modulen

def ObT6():
    # Definierar funktion
    txt = open("stats.txt", "rt")
    # Öppnar textfilen
    dice_max = input("How many sides does your dice have?:")
    # Låter användaren välja det maximala antal sidor som tärningen har
    stat_q = input("Which stat do you want to test?:")
    # Här bestäms vilken attribut/färdighet som ska gemföras med tärningens slag
    l = len(stat_q)
    # len() räknar antalet objekt i en lista, se line 20
    roll = random.randint(1, int(dice_max))
    # Variabel som fungerar som tärningen
    lines = txt.readlines()
    # Läser textfilen



          
    txt.close()
ObT6()
