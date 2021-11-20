target = input('Ange en bokstav:')
text = input('Skriv text:')
amount = 0

for i in text:
    if i == target:
        amount = amount + 1
print('Bokstaven ' + str(target) + ' finns ' + str(amount) + ' gånger i texten.')



