def diceroll_function():
# Definierar funktionen
    import random
    # Importerar random modulen så att den kan användas
    for x in range(1000):
        print(random.randint(1, 6))
        # Loop som körs 1000 gånger, printar ett slumpmässigt nummer mellan 1 till 6  
diceroll_function()
# Kör funktionen