import os
import pandas as pd

files = [i for i in os.listdir() if i.endswith(".csv")]
print("Arquivos encontrados:", files)

df = pd.DataFrame()

# Lê e concatena todos os arquivos
for file in files:
    try:
        df_temp = pd.read_csv(file)
        print(f"{file}: {df_temp.shape[0]} linhas, {df_temp.shape[1]} colunas")
        df_temp["origem"] = file # Adiciona o nome do arquivo como nova coluna
        df = pd.concat([df, df_temp], ignore_index=True)
    except Exception as e:
        print(f"Erro ao ler {file}: {e}")

# Salva o DataFrame final em um novo arquivo
# print("Total de linhas no DataFrame final:", df.shape[0])
df.to_csv("agrupado.csv", sep=";", index=False)