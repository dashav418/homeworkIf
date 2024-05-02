
x = -3
print('Hello! ')
if x < 0:
    print('Less zero!')
print('Goodbye! ')
a, b = 35, 9
if a > b:
    print('a > b')
if a > b and a > 0:
    print('success')
if (a > b) and (a > 0 or b < 1000):
    print('success')
if 5 < b and b < 10:
    print('success')
if '34' > '134':
    print('success')
if '134' > '13':
    print('success')
if [2, 4] > [2, 1]:
    print('success')
if '6' > 5:   #оставить или сделать '5'?
    print('success')
if [5, 6] > 5:  #заработает в случае [5, 6] > [5, 5]
    print('success')
if '6' != 5:
    print('success')
