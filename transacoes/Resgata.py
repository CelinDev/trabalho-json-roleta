#Retirar dinheiro
import json

def resgata(user):
    with open("user.json", "r", encoding="utf-8") as arquivo:
        user = json.load(arquivo)

    if user["Ativo"] == True:
        saque = float(input("Qual quantia deseja sacar? "))
        user["Saldo"] = float(user["Saldo"])
        if saque > float(user["Saldo"]):
            print("Você não tem saldo suficiente para sacar essa quantia.")
        else:
            print("Você retirou R$", saque, "!!")
            user["Saldo"] = float(user["Saldo"]) - saque

    with open("user.json", "w", encoding="utf-8") as arquivo:
        json.dump(user, arquivo, ensure_ascii=False, indent=4)

    print("Valor disponivel para saque: ", user["Saldo"])