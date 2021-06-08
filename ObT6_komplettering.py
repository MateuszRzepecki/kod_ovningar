# Importerar modulen random 
import random
# Importerar statistics modulen
import statistics
# Skapar en seed för random modulens funktioner
random.seed()

# Definierar en annan funktion
def ObT6():
    # här bestäms antalet gånger ObT6 kommer köras som högst
    times = input("How many times do you wish ObT6 to be executed at most?:")
    # lista, den här fylls på med värden från ObT6-funktionen 
    ObT6_list = []
    # variabel till en while-loop
    i = 0
    # Första tärningen får sin egen variabel (annars fungerar inte min kod som den ska)
    start_roll = random.randint(1, 6)
    # While-loop som körs om man får 6 på första kastet, körs endast det antalet gånger som användaren valt
    while start_roll == 6 and i < int(times):
        # For-loop som kastar två tärningar
        for x in range(2):
            # lägg märke till att här används roll istället för start_roll
            roll = random.randint(1, 6) 
            # Ibland när man kastar om en tärning med två andra så får man en eller två sexor igen,
            # då får programmet fuska lite och kasta mer gånger än användaren tillåter
            if roll == 6:
                i = i - 1       
            # Lägger värden för roll i listan
            ObT6_list.append(roll)  
        # Ökar i-värdet för att minska antalet ytterliggare gånger som while-loopen körs           
        i = i + 1
        # For-loopen letar efter alla 6:or som finns i listan och tar bort dem så att resultatet stämmer
        for y in range(len(ObT6_list)):     
            if 6 in ObT6_list:   
                ObT6_list.remove(6) 
        # Skriver ut listan så att man kan se hur koden arbetar     
        print(ObT6_list)
        # Skriver ut snittvärde för talen i listan
        print("Mean value: " + str(statistics.mean(ObT6_list)))
    # Skriver ut värdet man får då alla värden från listan adderas ihop
    print("Final result: " + str(sum(ObT6_list)))
    # If-sats som meddelar när första tärningen inte blir 6
    if start_roll != 6:
        print("First roll wasn't 6, restart to try again.")
# Anropar funktionen
ObT6()
