listaNumerico=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',',','.']

def validadorNuclear(lista):
    if valor[loopExterno] == listaNumerico[loopInterno]:
        print(f"{valor[loopExterno]} Validado.")
        lista[0]+=1
        return lista.append(loopInterno)

def floatizador():
    print(listaPreV,listaPosV)
    somador=0
    for indexPre in range(listaPreV[0]):
        somador+=listaPreV[indexPre+1]*(10**(listaPreV[0]-1-indexPre))
    for indexPos in range(listaPosV[0]):
        somador+=listaPosV[indexPos+1]/(10**(indexPos+1))
        print(listaPosV[indexPos+1]/(10**(indexPos+1)))
    return somador

def transformadorSTR_FLOAT(valor):
    global loopExterno,loopInterno, listaPreV,listaPosV
    listaPreV=[0]
    listaPosV=[0] 
    posVirgulaON=False
    loopExterno=0
    while loopExterno < len(valor):
        loopInterno=0
        while loopInterno <= (len(listaNumerico)-1):
            if valor[loopExterno]==',' or valor[loopExterno]=='.':
                posVirgulaON=True
                break
            elif posVirgulaON==False:
                validadorNuclear(listaPreV)                
            elif posVirgulaON==True:
                validadorNuclear(listaPosV)
            
            loopInterno+=1
        loopExterno+=1

    return floatizador()

while True:
    valor=input("Escreva o valor que deseja: ")
    if valor=='':
        print("\nPrograma encerrado.")
        break
    else:
       print(transformadorSTR_FLOAT(valor))