def search_function():
    # Definierar funktionen
    txt = open("stats.txt", "rt")
# Öppnar text-filen
    question = input("Vad söker du efter?:")
# Skapar en input som frågar användaren om det de söker
    lines = txt.readlines()
    for line in lines:
        if question in line:
            print(line.strip())
            txt.close()
            break
# Loopen letar efter användarens input i textfilen och om den hittas så printas den
search_function()
# Startar funktionen
