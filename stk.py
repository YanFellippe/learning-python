preco_acao = 5.31
qtd_acao = 100

valor_gasto = qtd_acao * preco_acao
print(f"Valor gasto: => {valor_gasto:.2f}")

preco_acao_futuro = 6.00
valor_esperado = qtd_acao * preco_acao_futuro

print(f"Valor esperado: => {valor_esperado:.2f}")

dividendo_por_acao = 0.45

lucro_com_dividendos = qtd_acao * dividendo_por_acao
lucro_venda = qtd_acao * preco_acao_futuro

if lucro_com_dividendos > lucro_venda:
    print("É melhor receber os dividendos")
    print(f"Pois o lucro dos dividendos será {lucro_com_dividendos}")
    print(f"E o lucro da venda será {lucro_venda:.2f}")
else:
    print("É melhor vender as ações")
    print(f"Pois o lucro dos dividendos será {lucro_com_dividendos}")
    print(f"E o lucro da venda será {lucro_venda:.2f}")