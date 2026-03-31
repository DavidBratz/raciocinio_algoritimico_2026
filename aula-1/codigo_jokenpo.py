print ( "1=Pedra , 2=Papel e 3=Tesoura")
david = int(input("Pedra , Papel ou Tesoura ? "))
if david == 1 :
    print ("pedra")
if david == 2 :
    print ("Papel")
if david == 3 :
    print ("Tesoura")
import random
pc = random.randint(1, 3)
if pc == 1 :
    print("PC:Pedra")
if pc == 2 :
    print ("PC:Papel")
if pc == 3 :
    print ("PC:Tesoura")
elif pc == 1 and david == 1 :
    print ("EMPATOU")
elif pc == 2 and david == 2 :
    print ("EMPATOU")
elif pc == 3 and david ==3 :
    print("EMPATOU")
elif pc == 3 and david == 1 :
    print ("VOCE GANHOU")
elif pc == 1 and david == 2 :
    print ("VOCE GANHOU")
elif pc == 2 and david == 3 :
    print ("VOCE GANHOU")
elif pc == 3 and david == 2 :
    print ("PC GANHOU")
elif pc == 2 and david == 1 :
    print ("PC GANHOU")
elif pc == 1 and david == 2 :
    print ("PC GANHOU")
