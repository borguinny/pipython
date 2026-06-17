arquivo_clientes = open(file="clientes.csv", mode="r", encoding="utf-8")

registros = arquivo_clientes.readlines()

arquivo_clientes.close()

nome_pesquisado = input("Nome: ")


for registro in registros:
    nome, data_nascimento, telefone, endereco, bairro, genero = registro.strip().split(",")

    if nome_pesquisado.lower() in nome.lower():
        print()
        print(f"{nome}")
        print(f"Data Nascimento:{data_nascimento}")
        print(f"Fone:{telefone}")
        print(f"End:{endereco} - Bairro: {bairro}")
        print(f"Gênero:{genero}")