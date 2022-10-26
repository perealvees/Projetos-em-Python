import random

print("Seja muito bem vindo ao GUESS NUMBER!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: O valor digitado não é numérico. Tente novamente!")
    quit()

random_number = random.randint(0, choice_number)
n_choices = 0

while True:
    answer_user = input("Chute um número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: O valor digitado não é numérico. Digite um número!")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("Parabéns. Acertou!")
        break
    elif answer_user > random_number:
        print("Esta longe, o número randomico é maior que isso..")
    else:
        print("Chutou longe, o número randomico é menor que isso..")

print("N° de tentativas: " + str(n_choices))

