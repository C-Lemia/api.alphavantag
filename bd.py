import requests
import pandas as pd
import sqlite3
from alpha_vantage.timeseries import TimeSeries

# Defina sua chave de API
API_KEY = 'sua_chave_api_aqui'

# Dicionário de símbolos e suas respectivas bolsas
bolsas = {
    'AAPL': 'NASDAQ',        # Apple
    'GOOGL': 'NASDAQ',       # Alphabet (Google)
    'MSFT': 'NASDAQ',        # Microsoft
    'TSLA': 'NASDAQ',        # Tesla
    'AMZN': 'NASDAQ',        # Amazon
    'FB': 'NASDAQ',          # Meta (Facebook)
    'NFLX': 'NASDAQ',        # Netflix
    'NVDA': 'NASDAQ',        # NVIDIA
    'BA': 'NYSE',            # Boeing
    'DIS': 'NYSE',           # Disney
    'JPM': 'NYSE',           # JPMorgan Chase
    'XOM': 'NYSE',           # ExxonMobil
    'KO': 'NYSE',            # Coca-Cola
    'PFE': 'NYSE',           # Pfizer
    'V': 'NYSE',             # Visa
    'BABA': 'NYSE',          # Alibaba
    'ORCL': 'NYSE',          # Oracle
    'INTC': 'NASDAQ',        # Intel
    'CSCO': 'NASDAQ',        # Cisco
    'IBM': 'NYSE',           # IBM
}

# Função para obter dados de uma ação e nome da bolsa
def obter_dados_bolsa(simbolo):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=simbolo, interval='1min', outputsize='full')

    nome_bolsa = bolsas.get(simbolo, 'Bolsa desconhecida')

    # Adicionar o nome da ação e bolsa como novas colunas ao DataFrame
    data['Ação'] = simbolo
    data['Bolsa'] = nome_bolsa

    return data

# Função para salvar os dados no SQLite
def salvar_no_sqlite(data, db_name='bolsa_valores.db'):
    # Conectar ao banco de dados SQLite (será criado se não existir)
    conn = sqlite3.connect(db_name)
    
    # Salvar o DataFrame no banco de dados
    data.to_sql('dados_bolsa', conn, if_exists='append', index=False)
    
    # Fechar a conexão
    conn.close()
    print(f"Dados salvos com sucesso no banco de dados '{db_name}'.")

# Iterar sobre todas as ações do dicionário e salvar os dados
for simbolo in bolsas:
    try:
        dados_bolsa = obter_dados_bolsa(simbolo)
        salvar_no_sqlite(dados_bolsa)
    except Exception as e:
        print(f"Erro ao obter ou salvar dados para {simbolo}: {e}")
