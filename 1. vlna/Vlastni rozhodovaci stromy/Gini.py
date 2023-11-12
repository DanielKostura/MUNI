COST = 0
HAS_AT_HOME = 1
MONEY = 2

data = [
    ([0.75, False, 0], False),
    ([0.75, False, 2], True),
    ([0.75, True, 0], False),
    ([0.99, False, 1], True),
    ([1.99, True, 1], False),
    ([2.99, False, 0], False),
    ([2.99, True, 2], True),
    ([3.50, False, 2], True),
    ([10.99, False, 2], True),
    ([10.99, True, 2], True)
    ]

def get_gini(treshhold, data):
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
    for i in range(len(data)):
        couple = []
        couple.append(data[i][0][atribut])
        couple.append(data[i][1])
        current_data.append(couple)
    current_data.sort()

    gini = 1000

    for i in range(len(data)-1):
        mid = (current_data[i][0] + current_data[i+1][0]) / 2
        current_gini = get_gini(mid, current_data)
        if current_gini < gini:
            gini = current_gini
            treshhold = mid

    return gini, treshhold


gini = 1000
for i in range(len(data[0][0])):
    current_gini, current_treshhold = search_atribut(i)
    if current_gini < gini:
        gini = current_gini
        treshhold = current_treshhold
        atribut = i

print(gini)
print(treshhold)
print(atribut)