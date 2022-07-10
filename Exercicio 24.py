# Analizando se a primeira palavra do texto é santos

texto = str(input("Em Qual cidade vc nasceu: ").strip().lower())
texto_sep = texto.split()

print(f'A Primeira palavra da sua cidade é \033[94m|\033[0msanto\033[94m|\033[0m: {texto_sep[0] == "santo"}')
