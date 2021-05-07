import random
# Importerar modulen random 

def dice_roll():
# Definierar funktion
    txt = open("stats.txt", "rt")
    # Öppnar textfilen
    dice_max = input("How many sides does your dice have?:")
    # Låter användaren välja det maximala antal sidor som tärningen har
    question = input("What stat are you looking for?:")
    # Här bestäms vilken attribut/färdighet som ska gemföras med tärningens slag
    l = len(question)
    roll = random.randint(1, int(dice_max))
    # Variabel som fungerar som tärningen
    lines = txt.readlines()
    # Läser textfilen
    for line in lines:
        if question in line:
            roll_result = line[l+1:100]
            print("Your stat:" + str(roll_result))
            # En loop genom texten, om attributen/färdigheten man söker finns så printas talet
    print("You rolled:" + " " + str(roll))
    # printar ut talet man har fått från slaget
    if roll >= int(roll_result):
        print("You did it!")
    if roll < int(roll_result):
        print("You failed.")
    if roll == 1:
        print("Your action was executed perfectly!")
    if roll == dice_max:
        print("Your action almost failed...")
        
 
    txt.close()
    # stänger textfilen
dice_roll()
