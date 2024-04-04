from core import generatePassword

pw =generatePassword.PasswordGeneratorSevice
min_length = generatePassword.MIN_LENGTH


def catchlength() -> int:
    r = input('change length? [y/n]')
    if r != "y":
        return min_length
    l = int(input("add lenght: "))
    return l

def catchinputs():
    l = catchlength()

    if input('add Uppercase? [y/n]') != 'y':
        upp = False
    else: upp = True
    
    if input('add Lowercase? [y/n]') != 'y':
        low = False
    else: low = True
    
    if input('add Number? [y/n]') != 'y':
        num = False
    else: num = True
    
    if input('add Symbols? [y/n]') != 'y':
        sym = False
    else: sym = True

    if (upp or low or num or sym) == False:
        print("No character")
        return catchinputs()
    
    return pw.generate(l, upp, low, num, sym)


while True:
    try:
        print(catchinputs())
        end_input = input('end? [y/n]')
        if end_input == 'y':
            break
        elif end_input != 'n':
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")
    except ValueError as e:
        print(e)

"""
bueno...
"""