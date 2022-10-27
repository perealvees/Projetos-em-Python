import random

user_points = 0
computer_points = 0


options = ['r','t','p']

while True:
    user_choice = input('Escolha: \nR(Pedra) \nT(Tesoura) \nP(Papel) \nOu pressione Q para sair.').lower()

    if user_choice == 'q':
        break

    computer_choice = random.randint(0,2)
    # 0 = R, 1 = T, 2 = P
    computer_options = options[computer_choice]

    print("O computador escolheu:" + computer_options)

    if user_choice == computer_options:
        print("EMPATE!")

    elif user_choice == "r" and computer_options == "t":
        print("GANHOU!")

    elif user_choice == "P" and computer_options == "R":
        print("GANHOU!")

    elif user_choice == "T" and computer_options == "P":
        print("GANHOU!")

    else:
        print('VOCÊ PERDEU')
        computer_points = computer_points + 1

    print("Sua pontuação foi: " + str(user_points))
    print("Pontuação do Computador foi" + str (computer_points))

    if  computer_points > user_points:
        print('VITÓRIA')
    elif computer_points == user_points:
        print("EMPATE!")
    else:
        print("DERROTA!")


print('GoodBye!')