import random
import json

with open("user.json", "r", encoding="utf-8") as arquivo:
    user = json.load(arquivo)


if user["Saldo"] > 0:
    aposta = int(input("Qual quantia deseja apostar? "))
    if aposta <= user["Saldo"]:
        numero_escolhido = int(input("Escolha um número de 1 a 10: "))
        numero_sorteado = random.randint(1, 10)
        print("O número sorteado foi:", numero_sorteado)

        if numero_escolhido == numero_sorteado:
            ganho = aposta * 2
            user["Saldo"] += ganho
            print("Parabéns! Você ganhou R$", ganho)
        else:
            user["Saldo"] -= aposta
            print("Você perdeu R$", aposta)
            with open("user.json", "w", encoding="utf-8") as arquivo:
                json.dump(user, arquivo, ensure_ascii=False, indent=4)
    else:
        print("Você não tem saldo disponível pra apostar essa quantidade.")            
else:
    print("Saldo insuficiente para essa aposta.")


