import string

Z26 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,0]

def transformMatriz(matriz):
    matriz = matriz.replace(' ', '')
    result = []
    if len(matriz)%2 != 0:
        for letter in range(len(matriz)):
            if letter == (len(matriz)-1):
                result.append(matriz[letter])
            result.append(matriz[letter])
    else :
        for letter in range(len(matriz)):
            result.append(matriz[letter])
    return result

def letterValue(letter1, letter2): # função que encontra o indíce da letra
    result = []
    letter1 = letter1.upper()
    letter2 = letter2.upper()
    alfabeto = string.ascii_uppercase
    if (letter1 == 'Z') : 
        value = 0
        result.append(value)
    else: 
        value = alfabeto.index(letter1) + 1
        result.append(value)
    if (letter2 == 'Z') :
        value = 0
        result.append(value)
    else :
        value = alfabeto.index(letter2) + 1 
        result.append(value)
    return result

def valueLetter(letter1, letter2):
    result = []
    alfabeto = string.ascii_uppercase
    if letter1 == 0:
        result.append('Z')
    else:
        result.append(alfabeto[letter1-1])
    if letter2 == 0:
        result.append('Z')
    else: 
        result.append(alfabeto[letter2-1])
    return result
    
def pmodulo(matriz,valor): # DIVISÃO PARA PEGAR O RESTO
    for p in matriz:
        if p[0] < 0: p[0] = p[0]%valor + 26 # CASO FOR UM VALOR NEGATIVO, É SOMANDO AO RESTO 26
        if p[1] < 0: p[1] = p[1]%valor + 26 
        if p[0] < valor : p[0] = p[0]
        else: p[0] = p[0]%valor
        if p[1] < valor : p[1] = p[1]
        else: p[1] = p[1]%valor
    return matriz

def det(matriz): # ENCONTRAR O DETERMINANTE DA MATRIZ CHAVE
    linha1 = matriz[0]
    linha2 = matriz[1]
    determinante = (linha1[0]*linha2[1])-(linha1[1]*linha2[0])
    return determinante

def inv(matriz): # MATRIZ INVERSA DA MATRIZ CHAVE
    aux = matriz[1][1]
    matriz[1][1] = matriz[0][0]
    matriz[0][0] = aux
    matriz[0][1] *= -1
    matriz[1][0] *= -1
    return matriz

def inversaMatriz(matriz,invDet): # MATRIZ C (MATRIZ INVERSA * DETERMINANTE NO Z26)
    for valor in range(len(matriz)):
        matriz[valor][0] *= invDet
        matriz[valor][1] *= invDet
    return matriz

def findInZ26(determinante): # ENCONTRAR ELEMENTO DO Z26 
    posicao = 0
    listaValores = []
    for valor in Z26:
        valor = valor * determinante
        listaValores.append(valor)
    aux = []
    for valor in range(len(listaValores)):
        conteudo = []
        if valor%2 != 0:
            continue
        else:
            conteudo.append(listaValores[valor])
            conteudo.append(listaValores[valor+1])
            aux.append(conteudo)
    listaValores = aux
    listaValores = pmodulo(listaValores,26)
    for i in range(len(listaValores)):
        if listaValores[i][0] == 1:
            posicao = Z26[(i*2)]
        if listaValores[i][1] == 1:
            posicao = Z26[(i*2)]
    return posicao
    
def crypto(String): # FUNÇÃO DE CRIPTOGRAFIA
    matrizChave = [[4,3],[1,2]] # matriz A
    matrizValue = [] # matriz que irá se tornar a matriz P
    frase = String
    String = transformMatriz(String)
    for letter in range(len(String)):
        if letter %2 != 0: continue
        else : 
            matriz2 = letterValue(String[letter],String[letter+1])
            matrizValue.append(matriz2)
    C = []
    for p in matrizValue:
        c = []
        cont = 0
        for linha in matrizChave:
            valor = (linha[0]*p[0])+(linha[1]*p[1])
            if cont == 1 : c.append(valor)
            else: c.append(valor)
            cont += 1
        C.append(c)
    C = pmodulo(C,26)
    matrizCrypto = []
    fraseCriptografada = ''
    for p in C:
        p= valueLetter(p[0],p[1])
        matrizCrypto.append(p)
    contagem = 0
    for valor in range(len(frase)):
        if frase[valor] == ' ':
            fraseCriptografada = fraseCriptografada + ' '
        else :
            if valor%2 == 0:
                fraseCriptografada = fraseCriptografada + matrizCrypto[contagem][0]
                fraseCriptografada = fraseCriptografada + matrizCrypto[contagem][1]
                contagem+=1
    return fraseCriptografada

def descrypt(String): # FUNÇÃO DE DESCRIPTOGRAFIA
    matrizChave = [[4,3],[1,2]] # matriz A
    frase = String
    C = transformMatriz(String)
    matrizC = []
    for letter in range(len(C)):
        if letter %2 != 0: continue
        else : 
            matriz2 = letterValue(C[letter],C[letter+1])
            matrizC.append(matriz2)
    A = inv(matrizChave)
    invDeterminante = findInZ26(det(matrizChave))
    A = inversaMatriz(A,invDeterminante)
    P = []
    for p in matrizC:
        c = []
        cont = 0
        for linha in A:
            valor = (linha[0]*p[0])+(linha[1]*p[1])
            if cont == 1 : c.append(valor)
            else: c.append(valor)
            cont += 1
        P.append(c)
    P = pmodulo(P,26)
    matrizDescrypto = []
    fraseDescriptografada = ''
    for p in P:
        p= valueLetter(p[0],p[1])
        matrizDescrypto.append(p)
    contagem = 0
    for valor in range(len(frase)):
        if frase[valor] == ' ':
            fraseDescriptografada = fraseDescriptografada + ' '
        else :
            if valor%2 == 0:
                fraseDescriptografada = fraseDescriptografada + matrizDescrypto[contagem][0]
                fraseDescriptografada = fraseDescriptografada + matrizDescrypto[contagem][1]
                contagem+=1
    return fraseDescriptografada
