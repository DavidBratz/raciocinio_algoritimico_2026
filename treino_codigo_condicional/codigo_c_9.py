num_1 = float(input("INFORME O PRIMEIRO NÚMERO:")) 
num_2 = float(input("INFORME O SEGUNDO NÚMERO:")) 
num_3 = float(input("INFORME O TERCEIRO NÚMERO:")) 

if num_1 >= num_2 and num_1 >= num_3: 
    if num_2 >= num_3: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_1}, {num_2}, {num_3}") 
    else: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_1}, {num_3}, {num_2}") 
elif num_2 >= num_1 and num_2 >= num_3: 
    if num_1 >= num_3: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_2}, {num_1}, {num_3}") 
    else: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_2}, {num_3}, {num_1}") 
else: 
    if num_1 >= num_2: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_3}, {num_1}, {num_2}") 
    else: print(f"A ORDEM CRESCENTE DOS NÚMEROS É: {num_3}, {num_2}, {num_1}")
