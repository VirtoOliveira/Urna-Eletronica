Roberto = 0
Elias = 0
Maria = 0
Simone = 0
Votos = 0
Nulos = 0
Brancos = 0

#Iniciando a votação

print("Digite 99, para encerrar a votação")

while True :
    Candidaton = int(input("Insira o numero de seu Candidato: ") )
    
    if Candidaton == 99:
        print("O usuario encerrou a votação")
        break

    elif Candidaton == 33:
        print("Candidato  Roberto foi selecionado")
        Roberto += 1
        Votos += 1
    elif Candidaton == 44:
        print("Candidato  Elias foi selecionado")
        Elias += 1
        Votos += 1
    elif Candidaton == 55:
        print("Candidata Maria foi selecionada")
        Maria += 1
        Votos += 1
    elif Candidaton == 66:
        print("Candidata Simone foi selecionado")
        Simone += 1
        Votos += 1
    elif Candidaton == 00:
        print("A opção de Voto branco foi selecionada")
        Votos += 1
        Brancos +=1
    else:
        print ("Voto NULO")
        Nulos +=1
        Votos +=1

if Votos > 0 :
    print("\n --- RESULTADO FINAL ---")
    print ("Nenhum voto computado")
Resultados = [("Brancos",Brancos),("Nulos",Nulos),("Roberto",Roberto),("Elias",Elias),("Maria",Maria),("Simone",Simone)]
Resultados.sort(key=lambda x: x[1],reverse=True)

for nome, votos in Resultados:
    if votos > 0:
        print(f"{nome}: {votos} votos ({(votos/Votos)*100:.2f}%)")

votos_validos = Roberto + Elias + Maria + Simone

if votos_validos > 0:
    vencedor, votos_vencedor = Resultados [0]
    
    if(votos_vencedor / votos_validos ) > 0.5:
        
        print(f"\n {vencedor} venceu no 1º turno com {(votos_vencedor/ votos_validos)*100:.2f}% dos votos válidos!")
    else:
        print("\n Nenhum candidato venceu no 1º turno. Vamos ao 2º turno")
        segundo_turno = [Resultados[0], Resultados [1]]

#Em caso de empate, começamos o 2º turno. Apenas com o 1º e 2º colocado da votação, excluindo votos brancos e nulos

        print (f"\n Candidatos do 2º turno serão: {segundo_turno [0][0]} e {segundo_turno [1][0]}")
        votos_segundo = {segundo_turno [0][0]: 0, segundo_turno [1][0]: 0}
        while True:
            print("\Digite 99 para encerrar a votação do 2º turno")
            voto = int(input(f"Vote em {segundo_turno[0][0]} (1) ou {segundo_turno [1][0]} (2): "))
            
            if voto == 99:
                print ("Votação encerrada")
                break
            elif voto == 1:
                votos_segundo[segundo_turno [0][0]] +=1
            elif voto == 1:
                votos_segundo[segundo_turno [1][0]] +=1
            else:
                print("Voto inválido")

        print("\n --- RESULTADO 2º TURNO---")
        for nome,v in votos_segundo.items():
            print(f"{nome}: {v} votos")

        vencedor = max(votos_segundo, key = votos_segundo.get)
        print (f"\n {vencedor} venceu o 2º turno!")
else:
    print("Nenhum voto foi computado")


    

