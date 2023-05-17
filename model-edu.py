from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

with open('objects.txt') as f:
    objects = [line.rstrip() for line in f]
with open('classes.txt') as f:
    classes = [line.rstrip() for line in f]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(objects)
Y = classes

clf = svm.SVC()
clf.fit(X, Y)

test_objects = ['<nav id="top-links" class="nav toggle-wrap">']
X_test = vectorizer.transform(test_objects)
predicted_classes = clf.predict(X_test)

for i, obj in enumerate(test_objects):
    print(f"Tag '{obj}' is '{predicted_classes[i]}'")

import joblib
joblib.dump(clf, 'model.pkl')
