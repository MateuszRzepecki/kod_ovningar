import random
# Importerar random modulen så att den kan användas


def T6_function():
    # Definierar funktionen
    result = []
    # Skapar en tom variabel som är en lista
    for x in range(1):
        result.append(random.randint(1, 6))
    nr1 = str(result.count(1))
    nr2 = str(result.count(2))
    nr3 = str(result.count(3))
    nr4 = str(result.count(4))
    nr5 = str(result.count(5))
    nr6 = str(result.count(6))
    print("Ett:" + nr1 + " " + "Två:" + nr2 + " " + "Tre:" + nr3 +
          " " + "Fyra:" + nr4 + " " + "Fem:" + nr5 + " " + "Sex:" + nr6)
    # Loop, printar ett slumpmässigt nummer mellan 1 till 6 och repeteras 1000 gånger
    # listan visar antalet gånger som x nummer uppstår 
T6_function()
# Kör funktionen
