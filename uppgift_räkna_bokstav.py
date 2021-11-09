target = input('Ange en bokstav:')
text = input('Skriv text:')

def CharacterCounter():
    antal = 0
    for i in text:
        if i == target:
            antal = antal + 1
    print('Bokstaven ' + str(target) + ' finns ' + str(antal) + ' gånger i texten.')
CharacterCounter()
