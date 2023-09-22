#1 Bibliotecas
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

#2 Código da ação
codigo_acao = "PETR4.SA"

#3 Salvar chave de API da Alpha Vantage
api_key = 'WIC9UMQ2PL2XN5M3'

#4 Usar uma instância da classe TimeSeries
ts = TimeSeries(key=api_key, output_format='pandas')

#5 Puxando os dados históricos da ação
dados, meta_dados = ts.get_daily(symbol=codigo_acao, outputsize='full')

#6 Extrair o fechamento
fechamento = dados['4. close']

#7 Criar dataframe
df = pd.DataFrame({
    'Data': fechamento.index,
    'Preço de Fechamento': fechamento.values
})

#8 Calcular as informações
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento.iloc[-1], 2)

#9 Imprimir os valores
print(f"Código da Ação: {codigo_acao}")
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")
print(f"Atual: {atual}")

#10 Salvar em Excel
nome_arquivo = f"{codigo_acao}_dados.xlsx"
df.to_excel(nome_arquivo, index=False)
print(f"Dados salvos em {nome_arquivo}")
