try:
    valor = int(input('Digite um valor: '))

    if valor % 2 == 0:
        print('É um número par!')
    else:
        print('É um número impar!')
except:
    print('Digite apenas números!')