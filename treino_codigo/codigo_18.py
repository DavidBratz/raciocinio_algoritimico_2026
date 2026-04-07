print("SEJA BEM VINDO AO CALCULADOR DE TEMPO DE DOWNLOAD")

tamanho = float(input("INFORME O TAMANHO DO ARQUIVO EM MB: "))
velocidade = float(input("INFORME A VELOCIDADE DO LINK DE INTERNET EM MBPS: "))

tamanho_megabits = tamanho * 8  

tempo_segundos = tamanho_megabits / velocidade
tempo_minutos = tempo_segundos / 60

print(f"O TEMPO APROXIMADO DE DONWLOAD DO ARQUIVO É DE {tempo_minutos:.2f} MINUTOS.")
