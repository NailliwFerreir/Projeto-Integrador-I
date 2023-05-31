def validateQuality(mp10, mp25, o3, co, no2, so2):
    boa = [['Boa'], ['Sem riscos à saúde.']]
    moderada = [['Moderada'], [
        'Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas) podem apresentar sintomas como tosse seca e cansaço.A população, em geral, não é afetada.']]
    ruim = [['Ruim'], [
        'Toda a população pode apresentar sintomas como tosse seca,cansaço, ardos nos olhos, nariz e garganta. Pessoas de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas)podem apresentar efeitos mais sérios na saúde.']]
    muitoRuim = [['Muito ruim'], [
        'Toda a população pode apresentar agravamento dos sintomas como tosse seca, cansaço, ardor nos olhos, nariz e garganta e ainda falta de ar e respiração ofegante. Efeitos ainda mais graves à saúde de grupos sensíveis (crianças, idosos e pessoas com doenças respiratórias e cardíacas).']]
    pessima = [['Pessima'], ['Toda a população pode apresentar sérios riscos de manifestações de doenças respiratórias e cardiovasculares. Aumento de mortes prematuras em pessoas de grupos sensíveis.']]
    if (mp10 > 250 or mp25 > 125 or o3 > 200 or co > 15 or no2 > 1130 or so2 > 800):
        return pessima
    elif (mp10 > 150 or mp25 > 75 or o3 > 160 or co > 13 or no2 > 320 or so2 > 365):
        return muitoRuim
    elif (mp10 > 100 or mp25 > 50 or o3 > 130 or co > 11 or no2 > 240 or so2 > 40):
        return ruim
    elif (mp10 > 50 or mp25 > 25 or o3 > 100 or co > 9 or no2 > 200 or so2 > 20):
        return moderada
    else:
        return boa

# REMOVIDO O ACENTO DE PÉSSIMA PARA CRIPTOGRAFAR