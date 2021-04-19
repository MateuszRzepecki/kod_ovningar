text = input('Skriv text.')
antal = 0
for i in text:
    if i == 'a':
        antal = antal + 1
print('Bokstaven "a" finns' ' ' + str(antal) + ' ' 'gånger i texten.')
