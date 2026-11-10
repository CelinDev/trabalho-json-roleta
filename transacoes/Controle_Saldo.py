import json
import Deposita
import Resgata

with open("user.json", "r", encoding="utf-8") as arquivo:
    user = json.load(arquivo)

print("Bem-vindo ao menu controle de saldo!")
print("1 - Consultar saldo")
print("2 - Depositar")
print("3 - Sacar")
menu = int(input("Escolha uma opção: "))


match menu:
        case 1: 
            print("Saldo disponível: R$", user["Saldo"])
        case 2:
            Deposita.deposita(user)
        case 3:
            Resgata.resgata(user)