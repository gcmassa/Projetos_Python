import pandas as pd
import os

# Lista todos os arquivos .csv no diretório atual
files = [i for i in os.listdir() if i.endswith(".csv")]

df = pd.DataFrame()

# Lê e concatena todos os arquivos
for file in files:
    df_temp = pd.read_csv(file)
    df_temp["origem"] = file  # Adiciona o nome do arquivo como nova coluna

    df = pd.concat([df, df_temp], ignore_index=True)

# Salva o DataFrame final em um novo arquivo
df.to_csv("agrupado.csv", sep=";", index=False)
