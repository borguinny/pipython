arquivo_clientes = open(file="clientes.csv", mode="r", encoding="utf-8")

registros = arquivo_clientes.readlines()

arquivo_clientes.close()

homens = 0
mulheres = 0

for registro in registros:
    nome, data_nascimento, telefone, endereco, bairro, genero = registro.strip().split(",")
    
    print(f"{nome}")
    print(f"Data Nascimento:{data_nascimento}")
    print(f"Fone:{telefone}")
    print(f"End:{endereco} - Bairro: {bairro}")
    print(f"Gênero:{genero}")
    print("-----------------------------------")

print(f"Total de Clientes: {len(registros)}")
