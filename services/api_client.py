import requests

resposta = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL').json()
print(resposta)

#valor de compra e venda
valorCompra = resposta['USDBRL']['bid']
valorVenda = resposta['USDBRL']['ask']

print(f"Valor de compra: {valorCompra}")
print(f"Valor de venda: {valorVenda}")
