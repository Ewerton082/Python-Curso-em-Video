# Achar onde apareceu a primeira e ultima vez tal letra

letra = str(input("Qual Letra você quer achar? ").strip().lower())

frase = str(input(f"Em qual frase quer procurar esta letra? ").lower().strip())

print(f"""
A letra \033[92m{letra}\033[m Apareceu \033[92m{frase.count(letra)}\033[m
A Primeira Vez que apareceu foi na posição \033[92m{frase.find(letra) +1}\033[m
A Ultima Vez que apareceu foi na posição \033[92m{frase.rfind(letra) +1}\033[m
""")
