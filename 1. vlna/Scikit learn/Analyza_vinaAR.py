from sklearn import tree
from sklearn import datasets
from typing import Optional

# Tuto funkci implementuj.
def create_wine_tree() -> tree.DecisionTreeClassifier:
    clf = tree.DecisionTreeClassifier()
    
    wine = datasets.load_wine()
    learn_data = [[row[0], row[1], row[4], row[6]] for row in wine.data]
    learn_classes = wine.target

    clf.fit(learn_data, learn_classes)
    return clf

def predict_samples(clf: tree.DecisionTreeClassifier,
                    wine_parameters: list[list[float]]) -> Optional[list[int]]:
    try:
        return list(clf.predict(wine_parameters))
    except ValueError:
        return


# Testy:
clf = create_wine_tree()
print(predict_samples(clf, [[12.8, 0.76, 79.3, 0.38], [13.5, 2.38, 103.5, 2.41]]))    # [1, 0]
print(predict_samples(clf, [[11.6, 3.15, 114.3]]))    # None