valor_gasto = 0
lucro = 0

#lista de ações

acoes = [
    {
        "ação": "AZUL4",
        "qtd" : 1000,
        "preço" : 1.41,
        "valorização" : 0.03,
        "dividendos" : 0.45
    },
    {
        "ação": "SYNK3",
        "qtd" : 200,
        "preço" : 5.32,
        "valorização" : -0.87,
        "dividendos" : 0.45
    }
]

for acao in acoes:
    valor_gasto_acao = acao.get("qtd") * acao.get("preço")
    lucro_dividendo = acao.get("qtd") * acao.get("dividendo")
    lucro_venda = valor_gasto_acao - (acao.get("qtd") * acao.get("preço") * (1 + acao.get("valorização")))
    
    if lucro_dividendo > lucro_venda:
        lucro = lucro + lucro_dividendo
    else:
        lucro = lucro + lucro_venda
        
    valor_gasto = valor_gasto * valor_gasto_acao
    
