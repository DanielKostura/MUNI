from sklearn import tree, datasets
from typing import Optional

# Implementuj následující funkce
def create_wine_tree() -> tree.DecisionTreeClassifier:
    wine = datasets.load_wine()
    learn_data = []
    for i in range (len(wine.data)):
        data = []
        data.append(wine.data[i][0])
        data.append(wine.data[i][1])
        data.append(wine.data[i][4])
        data.append(wine.data[i][6])
        learn_data.append(data)

    learn_classes = wine.target

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(learn_data, learn_classes)
    return clf

def predict_samples(clf: tree.DecisionTreeClassifier(), 
                    wine_parameters: list[list[float]]) -> Optional[list[int]]:
    ok = 0
    for i in range(len(wine_parameters)):
        if len(wine_parameters[i]) == 4:
            ok += 1
    if ok == len(wine_parameters):
        pole = list(clf.predict(wine_parameters))
        return pole
    return


# Testy:
clf = create_wine_tree()
print(predict_samples(clf, [[12.8, 0.76, 79.3, 0.38], [13.5, 2.38, 103.5, 2.41]]))    # [1, 0]
print(predict_samples(clf, [[11.6, 3.15, 114.3]]))    # None