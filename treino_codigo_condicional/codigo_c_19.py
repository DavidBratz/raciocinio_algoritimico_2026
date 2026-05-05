numero = int(input("Informe um número entre 0 e 1000:"))

if numero < 0 or numero >= 1000:
    print("Esse número é inválido")
else:
    centena = numero // 100
resto = numero % 100

dezena = resto // 10
unidade = resto % 10
partes = []
if centena > 0:
    if centena == 1:
        partes.append("1 centena")
    else:
        partes.append(f"{centena} centenas")

if dezena > 0:
    if dezena == 1:
        partes.append("1 dezena")
    else:
        partes.append(f"{dezena} dezenas")

if unidade > 0:
    if unidade == 1:
        partes.append("1 unidade")
    else:
        partes.append(f"{unidade} unidades")
if len(partes) == 1:
    print(partes[0])
elif len(partes) == 2:
    print(f"{partes[0]} e {partes[1]}")
else:
    print(f"{partes[0]}, {partes[1]} e {partes[2]}")

#-------- Testes ------------------------------------
#-------- 326 (3 centenas, 2 dezenas e 6 unidades) --
#-------- 300 (3 centenas) --------------------------
#-------- 100 (1 centena) ---------------------------
#-------- 320 (3 centenas e 2 dezenas) --------------
#-------- 310 (3 centenas e 1 dezena) ---------------
#-------- 305 (3 centenas e 5 unidades) -------------
#-------- 301 (3 centenas e 1 unidade) --------------
#-------- 101 (1 centena e 1 unidade) ---------------
#-------- 311 (3 centenas, 1 dezena e 1 unidade) ----
#-------- 111 (1 centena, 1 dezena e 1 unidade) -----
#-------- 25 (2 dezenas e 5 unidades) ---------------
#-------- 20 (2 dezenas) ----------------------------
#-------- 10 (1 dezena) -----------------------------
#-------- 21 (2 dezenas e 1 unidade) ----------------
#-------- 11 (1 dezena e 1 unidade) -----------------
#-------- 1 (1 unidade) -----------------------------
#-------- 7 (7 unidades) ----------------------------
#-------- 16 (1 dezena e 6 unidades) ----------------
