arquivo_clientes = open(file="clientes.csv", mode="r", encoding="utf-8")

registros = arquivo_clientes.readlines()

arquivo_clientes.close()


contagem_bairros = {}

for registro in registros:     
    nome, data_nascimento, telefone, endereco, bairro, genero = registro.strip().split(",")

    bairro = bairro.strip()
    
    contagem_bairros[bairro] = contagem_bairros.get(bairro, 0) + 1 
 
print("CLIENTES POR BAIRRO")
for bairro, quantidade in contagem_bairros.items():
    print(f"{bairro}: {quantidade} cliente(s)")
    