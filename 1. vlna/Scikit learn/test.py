from sklearn import tree

learn_data = [[0, 0], [24, 3], [18, 5]]
learn_classes = [0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(learn_data, learn_classes)

parameters = [[-1, 0], [24, 25]]
print(parameters)
pole = list(clf.predict(parameters))   # [0, 1]
print(pole)
