import random
# Importerar modulen random 

def dice_roll():
# Definierar funktion
    txt = open("stats.txt", "rt")
    # Öppnar textfilen
    dice_max = input("How many sides does your dice have?:")
    # Låter användaren välja det maximala antal sidor som tärningen har
    stat_q = input("What stat are you looking for?:")
    # Här bestäms vilken attribut/färdighet som ska gemföras med tärningens slag
    l = len(stat_q)
    # 
    roll = random.randint(1, int(dice_max))
    # Variabel som fungerar som tärningen
    lines = txt.readlines()
    # Läser textfilen
    for line in lines:
        if stat_q in line:
            stat_comp = line[l+1:100]
            print("Your stat:" + str(stat_comp))
            # En loop genom texten, om attributen/färdigheten man söker finns så printas talet
            print("You rolled:" + " " + str(roll))
            # printar ut talet man har fått från slaget
    if roll > int(stat_comp):
        print("You did it!")
    if roll < int(stat_comp):
        print("You failed.")
    if int(stat_comp) == 1:
        print("Your action was executed perfectly!")
    if int(stat_comp) == int(dice_max):
        print("Your action almost failed...")
    # If satser som syftar på att beskriva olika fall där värdet från kastet och attribut/färdighet gemförs
        
 
    txt.close()
    # stänger textfilen
dice_roll()
