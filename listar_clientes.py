# Abrir arquivo
arquivo_clientes = open(file="clientes.csv", mode="r", encoding="utf-8")

# Carregar dados para memória
registros = arquivo_clientes.readlines()

# Fechar arquivo
arquivo_clientes.close()

# Fazer o parsing de cada uma das linhas
registro = registros[50] # o primeiro registro

valores = registro.strip().split(",")

print(valores)




# "Quebrar cada linha nas vírgulas"





