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
    roll = random.randint(1, int(dice_sides))
    lines = txt.readlines() 
    for line in lines:
        if question in line:
            roll_result = line[l+1:100]
            print("Your stat:" + str(roll_result))
            # En loop genom texten, om attributen/färdigheten man söker finns så printas talet för den
    print("You rolled:" + " " + str(roll))
    if roll >= int(roll_result):
        print("You did it!")
    if roll < int(roll_result):
        print("You failed.")
    if roll == 1:
        print("Your action was executed perfectly!")
    if roll == dice_sides:
        print("Your action almost failed...")
        
 
    txt.close()
    # stänger textfilen
dice_roll()
