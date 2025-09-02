Roberto = 0
Elias = 0
Maria = 0
Simone = 0
Votos = 0

while True :
    Candidaton = int(input("Insira o numero de seu Candidato") )
    
    if Candidaton == 99:
        print("O usuario encerrou a votação")
        break

    if Candidaton == 33:
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
    else:
        print ("O candidato não foi encontrado")

if Votos > 0 :
    print("\n --- RESULTADO FINAL ---")
    print(f"Porcentagem de Votos, Roberto = {(Roberto/Votos) * 100:.2f}%")
    print(f"Porcentagem de Votos, Elias = {(Elias/Votos) * 100:.2f}%")
    print(f"Porcentagem de Votos, Maria = {(Maria/Votos) * 100:.2f}%")
    print(f"Porcentagem de Votos, Simone = {(Simone/Votos) * 100:.2f}%")
else:
    print ("Nenhum voto computado")
Resultados = [Roberto,Elias,Maria,Simone]
Resultados.sort(reverse=True)
for i in Resultados:
    print(i)

    

