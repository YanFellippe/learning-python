nome = str(input("Qual o seu nome? "))
XP = int(input("Quanto de XP? "))

if XP < 1000:
    nivel = "Ferro"
elif 1001 <= XP <= 2000:
    nivel = "Bronze"
elif 2001 <= XP <= 5000:
    nivel = "Prata"
elif 5001 <= XP <= 7000:
    nivel = "Ouro"
elif 7001 <= XP <= 8000:
    nivel = "Platina"
elif 8001 <= XP <= 9000:
    nivel = "Ascendente"
elif 9001 <= XP <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O Herói de nome {nome} está no nível de {nivel}")
