n = int(input("Digite o valor do n(MAIOR QUE 0 E QUE SEJA UM NÚMERO INTEIRO OU SEJA SEM VÍRGULAS):"))


for i in range(1, n + 1):
    espaços = (n - i)
    controle = (i * 2)
    print(" " * espaços + "X" * controle)
