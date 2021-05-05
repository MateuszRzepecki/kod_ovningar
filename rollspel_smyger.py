import random
# Importerar en modulen random 

def dice_roll():
# Definierar funktion
    txt = open("stats.txt", "rt")
    # Öppnar textfilen
    dice_sides = input("How many sides does your dice have?:")
    # Låter användaren välja den maxiala antal sidor som tärningen har
    question = input("What stat are you looking for?:")
    # Här bestäms vilken stat som ska gemföras med tärningen
    l = len(question)
    roll_20 = random.randint(1, int(dice_sides)) 
    lines = txt.readlines()
    # Variabler 
    for line in lines:
        if question in line:
            print("Your stat:" + line[l+1:100])
            # En loop genom texten, om attributen/färdigheten man söker finns så printas talet för den
    print("You rolled:" + " " + str(roll_20))
    #if roll_20 >= int(line[l+1:100]):
        #print("You did it!")
    #if roll_20 < :
        #print("You failed.")
    if roll_20 == int(1):
        print("Your action was executed perfectly!")
    if roll_20 == dice_sides:
        print("Your action almost failed...")

        
 
    txt.close()
    # stänger textfilen
dice_roll()
