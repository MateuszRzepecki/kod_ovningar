# Importerar modulen random 
import random
# Importerar statistics modulen
import statistics
# Skapar en seed för random modulens funktioner
random.seed()

# Låter användaren välja vilken funktion som ska anropas
function_select = input("Type [1] for dice_roll or [2] for ObT6:")
# Låter användaren välja det maximala antal sidor som tärningen har
dice_max = input("How many sides does your dice have?:")
# Variabel som fungerar som tärningen
d_roll = random.randint(1, int(dice_max))

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
                print("You rolled:" + " " + str(d_roll))
        # If satser som syftar på att beskriva olika fall där värdet från kastet och attribut/färdighet gemförs     
        if d_roll > int(stat_comp):
            print("You did it!")
        if d_roll < int(stat_comp):
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