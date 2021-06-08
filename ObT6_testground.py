# Importerar modulen random 
import random
# Skapar en seed för random modulens funktioner
random.seed()

# Öppnar textfilen
txt = open("stats.txt", "rt")
# Låter användaren välja det maximala antal sidor som tärningen har
dice_max = input("How many sides does your dice have?:")
# Variabel som fungerar som tärningen
roll = random.randint(5, int(dice_max))
# Läser textfilen
lines = txt.readlines()

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
    while roll == 6 and int(dice_max) == 6 and i < int(times):
        for x in range(2):
            ObT6_list.append(random.randint(1, 6))
        i = i + 1
        print(ObT6_list)
        print(sum(ObT6_list))



    # For_loop 
    # for x in range(3):
        # if sats körs endast om man fick 6 då man har kastat en T6.
        #if roll == 6 and int(dice_max) == 6:
            #print(str(ObT6_list))
ObT6()