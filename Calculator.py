answer = input('Chose math operations (plus, minus, multiply, divide, to the power ): ').lower()
if answer != 'plus' & 'minus' :
    print('Chose from the list!')
    exit()

a = input('First number: ')
b = input('Second number: ')
if a.isdigit() | b.isdigit():
    a = int(a)
    b = int(b)
    if answer == 'plus':
        result = a + b
    if answer == 'minus':
        result = a - b
    if answer == 'multiply':
        result = a * b
    if answer == 'divide':
        result = a / b
    if answer == 'plus':
        result = a ^ b
    print(result)
else:
    print('Chose a number!')
    exit()
