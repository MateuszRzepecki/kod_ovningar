# Importerar modulen random 
import random
# Importerar statistics modulen
import statistics
# Skapar en seed för random modulens funktioner
random.seed()

# Variabel som fungerar som tärningen
roll = random.randint(1, 6)

# Definierar en annan funktion
def ObT6():
    # här bestäms antalet gånger ObT6 kommer köras som högst
    times = input("How many times do you wish ObT6 to be executed at most?:")
    # lista, den här fylls på med värden från ObT6-funktionen 
    ObT6_list = []
    # variabel för en while-loop
    i = 0
    start_roll = random.randint(1, 6)
    # While-loop som körs om man får 6 på första kastet, körs endast det antalet gånger som användaren valt
    while start_roll == 6 and i < int(times):
        # For-loop som kastar två tärningar
        for x in range(2):
            roll = random.randint(1, 6) 
            if roll == 6:
                i = i - 1       
            ObT6_list.append(roll)             
        i = i + 1
        for y in range(len(ObT6_list)):     
            if 6 in ObT6_list:   
                ObT6_list.remove(6)      
        print(ObT6_list)
        print("Mean value: " + str(statistics.mean(ObT6_list)))
    print("Final result: " + str(sum(ObT6_list)))
    if start_roll != 6:
        print("First roll wasn't 6, restart to try again.")
ObT6()
