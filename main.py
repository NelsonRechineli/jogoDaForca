palavra = "python"
letras_usuario = []
chances = 10 

ganhou = False

while True:

    for letra in palavra:    #pra cada letra tentada pra nossa palavra
        if letra.lower() in letras_usuario:    #se a letra tentada tiver dentro das letras que o usuario tentou, printe a letra acertada
            print(letra, end=" ")
        else:
            print("_", end=" ")

    print(f"Você tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ")
    letras_usuario.append(tentativa.lower())  #adiciona a resposta do usuario nas letras que ele tentou . minusculo e maiusculo faz diferença

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True

    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
          
    if chances == 0 or ganhou:
        break

if ganhou:
    print(f"Parabéns, você ganhou. A palavra era: {palavra}")

else:
    print(f"Você perdeu! A palavra era: {palavra}")