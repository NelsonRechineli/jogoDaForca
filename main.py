from palavraForca import palavra    #palavra pra ser adivinhada
letras_usuario = []                #letras que o usuario já chutou
chances = 10                        #chances que damos pro usuario

ganhou = False                      #ainda nao ganhou, depois vamos encerrar o jogo

while True:                          #todo jogo é um loop 

    for letra in palavra:        #pra cada letra que tenho dentro da minha palavra escolhida 
        if letra.lower() in letras_usuario:    #se a letra tentada tiver dentro das letras que o usuario tentou, printe a letra acertada. transforma em letra minuscula
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")  #recebo a letra tentada pelo usuario
    letras_usuario.append(tentativa.lower())  #pegar essa letra e adicionar na minha lista letras_usuario. append adiciona. minusculo e maiusculo faz diferença

    if tentativa.lower() not in palavra.lower():  #se o usuario errar diminui a chance dele
        chances -= 1  #equivalente a chances = chances - 1

    ganhou = True    #encerra o jogo

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False  #parte pra proxima rodada
          
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")  #encerra o jogo

else:
    print(f"Você perdeu! A palavra era: {palavra}")  #encerra o jogo