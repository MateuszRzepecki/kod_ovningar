# Importerar modulen random 
import random
# Skapar en seed för random modulens funktioner
random.seed()

# Låter användaren välja vilken funktion som ska anropas
function_select = input("Type [1] for dice_roll or [2] for ObT6:")
# Låter användaren välja det maximala antal sidor som tärningen har
dice_max = input("How many sides does your dice have?:")
# Variabel som fungerar som tärningen
roll = random.randint(5, int(dice_max))

if str(function_select) == str(1):
    # Definierar funktion
    def dice_roll():
        # Öppnar textfilen
        txt = open("stats.txt", "rt")
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

        # stänger textfilen
        txt.close()
    dice_roll()

if str(function_select) == str(2):
    # Definierar en annan funktion
    def ObT6():
        # här bestäms antalet gånger ObT6 kommer köras som högst
        times = input("How many times do you wish ObT6 to be executed at most?:")
        # variabel för en while-loop
        i = 0
        # startvärdet, den första 6:an
        start_value = 6
        # lista, den här fylls på med värden från ObT6-funktionen och innehåller startvärde
        ObT6_list = [start_value]
        while roll == 6 and i < int(times):
            for x in range(2):
                ObT6_list.append(random.randint(1, 6))
            i = i + 1
            print(ObT6_list)
            print(sum(ObT6_list))
    ObT6()