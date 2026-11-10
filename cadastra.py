#Cadastrar Usuário:

import json


user = {
    "Nome": "Marcelo",
    "CPF": 14865814414,
    "Ativo": True,
    "Saldo": 0
}

with open("user.json", "w", encoding="utf-8") as arquivo:
    json.dump(user, arquivo, ensure_ascii=False, indent=4)
