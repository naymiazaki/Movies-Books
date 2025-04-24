import pandas as pd

#netflix_titles.csv
caminho_dados = 'D:\\PARTICULAR\\AULAS\\netflix_titles.csv'

try: 
    #Tentar carregar p dadps dp CSV para um DataFrame
    
    df = pd.read_csv(caminho_dados)
    
    print("Dados carregados com sucesso")
    print("-" * 30)

    #Mostra informações sobre as colunas (Tipos, valores não nulos)

    print ("Informações do DataFrame/Planilha")
    df.info()
    print("-" * 30)

    print("Dimensões (linhas, colunas):", df.shape)

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_dados}' não foi encontrado.")





    