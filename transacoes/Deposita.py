import json

def deposita(user):

    with open("user.json", "r", encoding="utf-8") as arquivo:
        user = json.load(arquivo)

    if user["Ativo"] == True:
        deposito = float(input("Qual quantia deseja depositar? "))
        print("Você depositou R$", deposito)
        user["Saldo"] += deposito

    with open("user.json", "w", encoding="utf-8") as arquivo:
        json.dump(user, arquivo, ensure_ascii=False, indent=4)