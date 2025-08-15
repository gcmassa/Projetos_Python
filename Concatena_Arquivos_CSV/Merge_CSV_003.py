import os
import pandas as pd

#caminho da pasta com CSV

#caminho = ".\Concatena_Arquivos_CSV"

# Lista os arquivos .csv no diretório atual
#files = [i for i in os.listdir(caminho) if i.endswith(".csv")]
files = [i for i in os.listdir() if i.endswith(".csv")]

if files:
    print("Arquivos encontrados:", files)
    df = pd.DataFrame()

    for file in files:
        try:
            df_temp = pd.read_csv(file)
            print(f"{file}: {df_temp.shape[0]} linhas, {df_temp.shape[1]} colunas")
            df_temp["origem"] = file
            df = pd.concat([df, df_temp], ignore_index=True)
        except Exception as e:
            print(f"Erro ao ler {file}: {e}")

    print("Total de linhas no DataFrame final:", df.shape[0])
    df.to_csv("agrupado.csv", sep=";", index=False)
    print("Arquivo 'agrupado.csv' gerado com sucesso.")
else:
    print("Nenhum arquivo .csv encontrado no diretório atual. Nada foi gerado.")
