import random
# Importerar random modulen så att den kan användas


def T20_function():
    # Definierar funktionen
    result = []
    # Skapar en tom variabel som är en lista
    for x in range(1000):
        result.append(random.randint(1, 20))
    nr1 = str(result.count(1))
    nr2 = str(result.count(2))
    nr3 = str(result.count(3))
    nr4 = str(result.count(4))
    nr5 = str(result.count(5))
    nr6 = str(result.count(6))
    nr7 = str(result.count(7))
    nr8 = str(result.count(8))
    nr9 = str(result.count(9))
    nr10 = str(result.count(10))
    nr11 = str(result.count(11))
    nr12 = str(result.count(12))
    nr13 = str(result.count(13))
    nr14 = str(result.count(14))
    nr15 = str(result.count(15))
    nr16 = str(result.count(16))
    nr17 = str(result.count(17))
    nr18 = str(result.count(18))
    nr19 = str(result.count(19))
    nr20 = str(result.count(10))
    print("Ett:" + nr1 + " " + "Två:" + nr2 + " " + "Tre:" + nr3 +
          " " + "Fyra:" + nr4 + " " + "Fem:" + nr5 + " " + "Sex:" + nr6 + " " + "Sju:" + nr7 + " " + "Åtta:" + nr8 + " " + "Nio:" + nr9 + " " + "Tio:" + nr10 + " " + "Elva:" + nr11 + " " + "Tolv:" + nr12 + " " + "Tretton:" + nr13 + " " + "Fjorton:" + nr14 + " " +
          "Femton:" + nr15 + " " + "Sexton:" + nr16 + " " + "Sjutton:" + nr17 + " " + "Arton:" + nr18 + " " + "Nitton:" + nr19 + " " + "Tjugo:" + nr20)
    # Loop, printar ett slumpmässigt nummer mellan 1 till 20 och repeteras 1000 gånger
    # listan visar antalet gånger som x nummer uppstår
T20_function()
# Kör funktionen
