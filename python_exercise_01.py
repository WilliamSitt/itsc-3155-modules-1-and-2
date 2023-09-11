entry = input('Enter a string: ')
length = len(entry)
result = ''
for i in range(length):
    result += entry[length - 1]
    length -= 1
print(result)