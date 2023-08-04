# unit converter test

def print_menu():
    print ('1. Fahrenheit to Celsius')
    print ('2. Fahrenheit to Kelvin ')
    print ('3. Celsius to Fahrenheit')
    print ('4. Celsius to Kelvin')
    print ('5. Kelvin to Fahrenheit')
    print ('6. Kelvin to Celsius')

def F_to_C():
    Fahrenheit = float(input('Fahrenheit: '))
    Celsius = (Fahrenheit-32) / 1.8
    print('lämpötila celsiuksena on: {0}'. format(Celsius))

def F_to_K():
    Fahrenheit = float(input('Fahrenheit: '))
    Kelvin = (Fahrenheit+459.67) / 1.8
    print('lämpötila Kelvineissä on: {0}'. format(Kelvin))

def C_to_F():
    Celsius = float(input('Celsius: '))
    Fahrenheit = Celsius * 1.8 + 32
    print('lämpötila Fahrenheittina on: {0}'. format(Fahrenheit))

def C_to_K():
    Celsius = float(input('Celsius: '))
    Kelvin = Celsius + 273.15
    print('lämpötila Kelvineissä on: {0}'. format(Kelvin))

def K_to_F():
    Kelvin = float(input('Kelvin: '))
    Fahrenheit = Kelvin *1.8 - 459.67
    print('lämpötila Fahrenheittina on: {0}'. format(Fahrenheit))

def K_to_C():
    Kelvin = float(input('Kelvin: '))
    Celsius = Kelvin - 273.15
    print('lämpötila Celsiuksena on: {0}'. format(Celsius)) 

while True:
    print_menu()

    choice = input ('Minkä muunnoksen haluat tehdä?: ')

    if choice == '1':
        F_to_C()

    if choice == '2':
        F_to_K()

    if choice == '3':
        C_to_F()

    if choice == '4':
        C_to_K()

    if choice == '5':
        K_to_F()

    if choice == '6':
        K_to_C()
