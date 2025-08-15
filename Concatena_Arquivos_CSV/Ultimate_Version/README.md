
---

## 🛠️ Melhorias incluidas

- ✅ Escolha de diretório via argumento ou padrão atual
- ✅ Verificação de existência de arquivos `.csv`
- ✅ Tratamento de erros com mensagens claras
- ✅ Relatório de progresso com contagem de linhas/colunas
- ✅ Confirmação final com total de arquivos e linhas
- ✅ Suporte a subpastas (opcional)
- ✅ Interface de linha de comando com `argparse`

---

## 🧪 Código Final: `Merge_CSV_Ultimate.py`

```python
import os
import pandas as pd
import argparse

def listar_csvs(diretorio, incluir_subpastas=False):
    arquivos_csv = []
    if incluir_subpastas:
        for raiz, _, arquivos in os.walk(diretorio):
            arquivos_csv.extend([os.path.join(raiz, f) for f in arquivos if f.endswith(".csv")])
    else:
        arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".csv")]
    return arquivos_csv

def merge_csvs(arquivos, separador=";", nome_saida="agrupado.csv"):
    df_final = pd.DataFrame()
    total_linhas = 0

    for arquivo in arquivos:
        try:
            df_temp = pd.read_csv(arquivo)
            print(f"Lendo '{arquivo}': {df_temp.shape[0]} linhas, {df_temp.shape[1]} colunas")
            df_temp["origem"] = os.path.basename(arquivo)
            df_final = pd.concat([df_final, df_temp], ignore_index=True)
            total_linhas += df_temp.shape[0]
        except Exception as e:
            print(f"⚠️ Erro ao ler '{arquivo}': {e}")

    if not df_final.empty:
        df_final.to_csv(nome_saida, sep=separador, index=False)
        print(f"\n✅ Arquivo '{nome_saida}' gerado com sucesso.")
        print(f"📊 Total de arquivos processados: {len(arquivos)}")
        print(f"📈 Total de linhas combinadas: {total_linhas}")
    else:
        print("🚫 Nenhum dado válido foi encontrado para gerar o arquivo.")

def main():
    parser = argparse.ArgumentParser(description="Merge múltiplos arquivos CSV em um único arquivo.")
    parser.add_argument("-d", "--diretorio", default=".", help="Diretório onde estão os arquivos CSV")
    parser.add_argument("-s", "--subpastas", action="store_true", help="Incluir arquivos em subpastas")
    parser.add_argument("-o", "--output", default="agrupado.csv", help="Nome do arquivo de saída")
    parser.add_argument("-sep", "--separador", default=";", help="Separador do CSV de saída")

    args = parser.parse_args()

    arquivos_csv = listar_csvs(args.diretorio, args.subpastas)

    if arquivos_csv:
        print(f"\n🔍 {len(arquivos_csv)} arquivos .csv encontrados.")
        merge_csvs(arquivos_csv, separador=args.separador, nome_saida=args.output)
    else:
        print("🚫 Nenhum arquivo .csv encontrado no diretório especificado.")

if __name__ == "__main__":
    main()
```

---

## 🧭 Como usar

No terminal ou prompt de comando:

```bash
python merge_csv_ultimate.py
```

Ou com argumentos personalizados:

```bash
python merge_csv_ultimate.py -d ./meus_csvs -s -o resultado.csv -sep ","
```

---
