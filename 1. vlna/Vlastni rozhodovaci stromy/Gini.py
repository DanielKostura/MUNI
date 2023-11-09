COST = 0
HAS_AT_HOME = 1
MONEY = 2

data = [
    ([1.99, True, 1], False),
    ([2.99, True, 2], True),
    ([0.75, True, 0], False),
    ([0.99, False, 1], True),
    ([3.50, False, 2], True),
    ([2.99, False, 0], False),
    ([10.99, False, 2], True),
    ([0.75, False, 0], False),
    ([10.99, True, 2], True),
    ([0.75, False, 2], True)
    ]

# Tuto funkci implementuj.
def gini(cislo, x):
    odpoved_ano_ano = 0
    odpoved_ano_nie = 0
    odpoved_nie_ano = 0
    odpoved_nie_nie = 0

    for i in range(len(data)):
        if data[i][0][cislo] < x:
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

    
    gini_true = 1 - (odpoved_ano_ano/odpoved_ano)**2 - (odpoved_ano_nie/odpoved_ano)**2
    gini_false = 1 - (odpoved_nie_ano/odpoved_nie)**2 - (odpoved_nie_nie/odpoved_nie)**2
    
    gini = (odpoved_ano/odpovede) * gini_true + (odpoved_nie/odpovede) * gini_false

    return gini


print(gini(0, 3.3)) #vyhral cisla
print(gini(2, 1)) 
print(gini(2, 2)) 