entry = input('Enter a string: ')
result1 = ''
result2 = ''
for i in range(len(entry)):
    if entry[i] != entry[i].capitalize() and entry[i] != ' ':
        result1 += entry[i]
    elif entry[i] == entry[i].capitalize() and entry[i] != ' ':
        result2 += entry[i]
print(result1 + result2)