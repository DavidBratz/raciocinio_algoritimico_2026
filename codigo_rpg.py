import random
tank_vida = 2000

tank_resistencia_fisica = 20
tank_resistencia_fogo = 20
tank_resistencia_raio = 5

tank_dano_fogo = 100
tank_dano_raio = 100
tank_dano_fisico = 100

atacante_vida = 1500

atacante_resistencia_fisico = 10
atacante_resistencia_fogo = 10
atacante_resistencia_raio = 10

atacante_dano_fisico = 100
atacante_dano_fogo = 150
atacante_dano_raio = 160

while tank_vida > 0 and atacante_vida > 0:
    escolha_do_ataque = int(input(" 1 PARA FÍSICO \n 2 PARA FOGO  \n 3 PARA RAIO \n DIGITE : "))
    escolha_do_ataque_tank = int(random.randint(1,3))
    if escolha_do_ataque == 1:
        tank_vida = tank_vida - (atacante_dano_fisico - tank_resistencia_fisica)
        if escolha_do_ataque_tank == 1:
            atacante_vida = atacante_vida - (tank_dano_fisico - atacante_resistencia_fisico)
            print(f"\nTANK ATACOU FISICAMENTE , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 2:
            atacante_vida = atacante_vida - (tank_dano_fogo - atacante_resistencia_fogo)
            print(f"\nTANK ATACOU COM FOGO , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 3:
            atacante_vida = atacante_vida - (tank_dano_raio - atacante_resistencia_raio)
            print(f"\nTANK ATACOU COM RAIO , MINHA VIDA :{atacante_vida}")
    elif escolha_do_ataque == 2:
        tank_vida = tank_vida - (atacante_dano_fogo - tank_resistencia_fogo)
        if escolha_do_ataque_tank == 1:
            atacante_vida = atacante_vida - (tank_dano_fisico - atacante_resistencia_fisico)
            print(f"\nTANK ATACOU FISICAMENTE , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 2:
            atacante_vida = atacante_vida - (tank_dano_fogo - atacante_resistencia_fogo)
            print(f"\nTANK ATACOU COM FOGO , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 3:
            atacante_vida = atacante_vida - (tank_dano_raio - atacante_resistencia_raio)
            print(f"\nTANK ATACOU COM RAIO , MINHA VIDA :{atacante_vida}")
    elif escolha_do_ataque == 3:
        tank_vida = tank_vida - (atacante_dano_raio - tank_resistencia_raio)
        if escolha_do_ataque_tank == 1:
            atacante_vida = atacante_vida - (tank_dano_fisico - atacante_resistencia_fisico)
            print(f"\nTANK ATACOU FISICAMENTE , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 2:
            atacante_vida = atacante_vida - (tank_dano_fogo - atacante_resistencia_fogo)
            print(f"\nTANK ATACOU COM FOGO , MINHA VIDA :{atacante_vida}")
        if escolha_do_ataque_tank == 3:
            atacante_vida = atacante_vida - (tank_dano_raio - atacante_resistencia_raio)
            print(f"\nTANK ATACOU COM RAIO , MINHA VIDA :{atacante_vida}")
    else:
        print("ESCOLHA INVÁLIDA")
    print("VIDA DO TANK:", tank_vida)
    continue
if tank_vida <= 0:
    print("VOCE GANHOU")
if atacante_vida <= 0:
    print("VOCÊ MORREU")