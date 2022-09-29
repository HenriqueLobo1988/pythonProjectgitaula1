print('Olá Karina!')
print("quanto é 1+1?")

print('Olá Karina!')
print("quer somar comigo?")


def calculate():
    operation = input('''
Por favor, diga a operação que quer fazer:
+ Para soma
- Para subtração
* Para multiplicação
/ Para Divisão
''')

    number_1 = int(input('Por favor, entre com o primeiro número: '))
    number_2 = int(input('Por favor, entre com o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('vocẽ não digitou nenhuma operação, por favor Ka, digite certo.')

    # Add again() function to calculate() function
    again()


def again():
    calc_again = input('''
Você quer realmente calcular 1+1 de novo Karina?
digite Y para sim ou N para Nao.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até mais Ka, te Amo, bocó!.')
    else:
        again()


calculate()