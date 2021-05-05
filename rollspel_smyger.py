import random
# Importerar en modul 

def T20_roll():
# Definierar funktion
    txt = open("stats.txt", "rt")
    question = input("Compare?:")
    l = len(question)
    result = []
    roll_20 = result.append(random.randint(1, 20)) 
    lines = txt.readlines()
    for line in lines:
        if question in line:
            print(line[l+1:100])
    for x in range(1):
        roll_20
        print("You got:" + " " + str(result))
        #print("You did it!")
        
 
    txt.close()
T20_roll()
