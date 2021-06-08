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

# Definierar funktion
def dice_roll():
    # Här bestäms vilken attribut/färdighet som ska gemföras med tärningens slag
    stat_q = input("Which stat do you want to test?:")
    # len() räknar antalet objekt i en lista, kolla for-loopen
    l = len(stat_q)
    # Läser textfilen
    lines = txt.readlines()
    # for-loop 
    for line in lines:
        # Kollar om input värdet finns i line
        if stat_q in line:
            # Här används l för att få bort början på linjen med frågan
            stat_comp = line[l+1:100]
            # Om attributen/färdigheten man söker finns så printas talet
            print("Your stat:" + str(stat_comp))
            # printar ut talet man har fått från slaget
            print("You rolled:" + " " + str(roll))
    # If satser som syftar på att beskriva olika fall där värdet från kastet och attribut/färdighet gemförs     
    if roll > int(stat_comp):
        print("You did it!")
    if roll < int(stat_comp):
        print("You failed...")
    if int(stat_comp) == 1:
        print("Your action was executed perfectly!")
    if int(stat_comp) == int(dice_max):
        print("Your action almost failed...")

dice_roll()

# stänger textfilen
txt.close()

# Definierar en annan funktion
def ObT6():
    # Tom lista fylls på med värden från ObT6-funktionen
    ObT6_list = [] 
    # For_loop 
    for x in range(3):
        # if sats körs endast om man fick 6 då man har kastat en T6.
        if roll == 6 and int(dice_max) == 6:
            print("bazinga")
ObT6() 
