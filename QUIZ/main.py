print('Bem vindo ao meu GTA QUIZ!! ')
answer_user = input('Bora começar um desafio? (Y/N) ')
print(answer_user)
if answer_user != "Y":
    quit()
score = 0


print('Começando ... ')
print('Quem desenvolveu o jogo GTA? \nA) RockStar Games \nB) Activision \nC) EA Games')
answer_user_1 = input('Resposta: ')

if answer_user_1 == 'A':
    print('Correto!')
    score = score + 1
else:
    print('Resposta Incorreta')

print('Como é o nome do principal personagem do GTA San Andreas? \nA) Billy \nB) Nick \nC) Carl')
answer_user_2 = input('Resposta: ')

if answer_user_2 == 'C':
    print('Correto!')
    score = score + 1
else:
    print('Resposta Incorreta')

print(f"Fim de Jogo... Pontuação: { score } /2" )

