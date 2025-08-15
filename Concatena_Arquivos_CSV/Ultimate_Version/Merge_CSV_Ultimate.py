import os
import pandas as pd
import argparse

# Função para listar arquivos CSV no diretório especificado
def listar_csvs(diretorio, incluir_subpastas=False):
    arquivos_csv = []

    # Se incluir_subpastas for True, percorre todas as subpastas
    if incluir_subpastas:
        for raiz, _, arquivos in os.walk(diretorio):
            arquivos_csv.extend([os.path.join(raiz, f) for f in arquivos if f.endswith(".csv")])
    else:
        # Caso contrário, lista apenas os arquivos do diretório principal
        arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".csv")]

    return arquivos_csv

# Função principal para ler, concatenar e salvar os arquivos CSV
def merge_csvs(arquivos, separador=";", nome_saida="agrupado.csv"):
    df_final = pd.DataFrame()  # DataFrame vazio para acumular os dados
    total_linhas = 0  # Contador de linhas totais

    for arquivo in arquivos:
        try:
            # Lê o arquivo CSV
            df_temp = pd.read_csv(arquivo)

            # Exibe informações sobre o arquivo lido
            print(f"Lendo '{arquivo}': {df_temp.shape[0]} linhas, {df_temp.shape[1]} colunas")

            # Adiciona uma coluna com o nome do arquivo de origem
            df_temp["origem"] = os.path.basename(arquivo)

            # Concatena ao DataFrame final
            df_final = pd.concat([df_final, df_temp], ignore_index=True)

            # Atualiza o contador de linhas
            total_linhas += df_temp.shape[0]

        except Exception as e:
            # Em caso de erro na leitura, exibe mensagem e continua
            print(f"⚠️ Erro ao ler '{arquivo}': {e}")

    # Verifica se o DataFrame final contém dados
    if not df_final.empty:
        # Salva o resultado em um novo arquivo CSV
        df_final.to_csv(nome_saida, sep=separador, index=False)

        # Mensagens de sucesso e resumo
        print(f"\n✅ Arquivo '{nome_saida}' gerado com sucesso.")
        print(f"📊 Total de arquivos processados: {len(arquivos)}")
        print(f"📈 Total de linhas combinadas: {total_linhas}")
    else:
        # Caso nenhum dado tenha sido lido com sucesso
        print("🚫 Nenhum dado válido foi encontrado para gerar o arquivo.")

# Função principal que configura a interface de linha de comando
def main():
    # Cria o parser de argumentos
    parser = argparse.ArgumentParser(description="Merge múltiplos arquivos CSV em um único arquivo.")

    # Argumento para o diretório onde estão os arquivos CSV
    parser.add_argument("-d", "--diretorio", default=".", help="Diretório onde estão os arquivos CSV")

    # Argumento para incluir arquivos em subpastas
    parser.add_argument("-s", "--subpastas", action="store_true", help="Incluir arquivos em subpastas")

    # Argumento para nome do arquivo de saída
    parser.add_argument("-o", "--output", default="agrupado.csv", help="Nome do arquivo de saída")

    # Argumento para definir o separador do CSV
    parser.add_argument("-sep", "--separador", default=";", help="Separador do CSV de saída")

    # Lê os argumentos fornecidos pelo usuário
    args = parser.parse_args()

    # Lista os arquivos CSV com base nos argumentos
    arquivos_csv = listar_csvs(args.diretorio, args.subpastas)

    # Verifica se há arquivos para processar
    if arquivos_csv:
        print(f"\n🔍 {len(arquivos_csv)} arquivos .csv encontrados.")
        merge_csvs(arquivos_csv, separador=args.separador, nome_saida=args.output)
    else:
        # Mensagem caso nenhum arquivo seja encontrado
        print("🚫 Nenhum arquivo .csv encontrado no diretório especificado.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()