digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ' ']

def verif(name):
    if len(name) <= 2:
        print('Your name must be at least 2 characters long')
        return False
    if name == 'exit':
        print('Bye!')
        return False
    else:
        print(f'Ton nom est {name}!')
        return True


def cleaner(name):
    for i in digit:
        name = name.replace(str(i), '')
    return name


while True:
    try:
        name = str(input(f'Enter your name: (entre exit to exit)\n'))
    except ValueError:
        print('Invalid input')
        continue
    if verif(cleaner(name)):
        break
