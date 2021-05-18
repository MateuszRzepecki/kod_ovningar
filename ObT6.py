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
    for line in lines:
        if stat_q in line:
            stat_comp = line[l+1:100]
            # Här används len(stat_q) för att få bort början på linjen med frågan
            print("Your stat:" + str(stat_comp))
            # En loop genom texten, om attributen/färdigheten man söker finns så printas talet
            print("You rolled:" + " " + str(roll))
            # printar ut talet man har fått från slaget
  


          
    txt.close()
ObT6()
