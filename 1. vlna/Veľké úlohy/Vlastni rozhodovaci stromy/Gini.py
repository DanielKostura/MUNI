COST = 0
HAS_AT_HOME = 1
MONEY = 2

data = [
([20.47, 13.74], False),
([15.75, 8.74], False),
([6.23, 5.09], False),
([11.7, 9.98], False),
([5.23, 3.47], False),
([4.5, 7.57], False),


([12.5, 1.56], True),
([23.26, 7.78], True),
([3.9, 7.21], True),
([7.77, 5.48], True),
([7.06, 2.28], True),
([1.13, 2.39], True)

#([35.86, True, 2], True)
]

def get_gini(treshhold, data): # vypocita gini atributu
    odpoved_ano_ano = 0
    odpoved_ano_nie = 0
    odpoved_nie_ano = 0
    odpoved_nie_nie = 0

    for i in range(len(data)):
        if data[i][0] < treshhold:
            if data[i][1] == True:
                odpoved_ano_ano += 1
            elif data[i][1] == False:
                odpoved_ano_nie += 1

        else:
            if data[i][1] == True:
                odpoved_nie_ano += 1
            elif data[i][1] == False:
                odpoved_nie_nie += 1

    odpoved_ano = odpoved_ano_ano + odpoved_ano_nie
    odpoved_nie = odpoved_nie_nie + odpoved_nie_ano
    odpovede = odpoved_ano + odpoved_nie

    if odpoved_ano != 0 and odpoved_nie != 0:
        gini_true = 1 - (odpoved_ano_ano/odpoved_ano)**2 - (odpoved_ano_nie/odpoved_ano)**2
        gini_false = 1 - (odpoved_nie_ano/odpoved_nie)**2 - (odpoved_nie_nie/odpoved_nie)**2
    
        gini = (odpoved_ano/odpovede) * gini_true + (odpoved_nie/odpovede) * gini_false

        return gini  
    return 1000

def search_atribut(atribut):
    current_data = []
    for i in range(len(data)): # vytvori jednoduchy zoznam
        couple = []
        couple.append(data[i][0][atribut])
        couple.append(data[i][1])
        current_data.append(couple)
    current_data.sort()

    gini = 1000

    for i in range(len(data)-1): # pocitanie jednotlivých gini v atribute
        mid = (current_data[i][0] + current_data[i+1][0]) / 2
        current_gini = get_gini(mid, current_data)
        if current_gini < gini: # hladanie najvacsieho gini v atribute
            gini = current_gini
            treshhold = mid

    return gini, treshhold


gini = 1000
for i in range(len(data[0][0])):
    current_gini, current_treshhold = search_atribut(i)
    if current_gini < gini: # hladanie najvacsieho gini s pomedzi atributov
        gini = current_gini
        treshhold = current_treshhold
        atribut = i

print(gini)
print(treshhold)
print(atribut)