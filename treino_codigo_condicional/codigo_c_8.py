prod1 = float(input("INFORME O VALOR DO PRIMEIRO PRODUTO EM R$:"))
prod2 = float(input("INFORME O VALOR DO SEGUNDO PRODUTO EM R$:"))
prod3 = float(input("INFORME O VALOR DO TERCEIRO PRODUTO EM R$:"))

if prod1 == prod2 and prod2 == prod3:
    print(f"VOCÊ DEVE COMPRAR QUALQUER UM DOS TRÊS PRODUTOS POIS OS VALORES DELES SÃO OS MESMOS R$ {prod1}")
elif prod1 == prod2 and prod1 < prod3:
    print(f"VOCÊ DEVE COMPRAR O PRIMEIRO PRODUTO R$ {prod1} OU O SEGUNDO PRODUTO R$ {prod2} POIS ELES SÃO MAIS BARATOS QUE O TERCEIRO PRODUTO R$ {prod3}")
elif prod1 == prod3 and prod1 < prod2:
    print(f"VOCÊ DEVE COMPRAR O PRIMEIRO PRODUTO R$ {prod1} OU O TERCEIRO PRODUTO R$ {prod3} POIS ELES SÃO MAIS BARATOS QUE O SEGUNDO PRODUTO R$ {prod2}")
elif prod2 == prod3 and prod2 < prod1:
    print(f"VOCÊ DEVE COMPRAR O SEGUNDO PRODUTO R$ {prod2} OU O TERCEIRO PRODUTO R$ {prod3} POIS ELES SÃO MAIS BARATOS QUE O PRIMEIRO PRODUTO R$ {prod1}")        
elif prod1 <= prod2 and prod1 <= prod3:
    print(f"VOCÊ DEVE COMPRAR O PRIMEIRO PRODUTO PORQUE ELE É MAIS BARATO R$ {prod1}, DO QUE OS DEMAIS PRODUTOS LISTADOS R$ {prod2} E R$ {prod3}")
elif prod2 <= prod1 and prod2 <= prod3:
    print(f"VOCÊ DEVE COMPRAR O SEGUNDO PRODUTO PORQUE ELE É MAIS BARATO R$ {prod2}, DO QUE OS DEMAIS PRODUTOS LISTADOS R$ {prod1} E R$ {prod3}")
else:
    print(f"VOCÊ DEVE COMPRAR O TERCEIRO PRODUTO PORQUE ELE É MAIS BARATO R$ {prod3}, DO QUE OS DEMAIS PRODUTOS LISTADOS R$ {prod1} E R$ {prod2}")
