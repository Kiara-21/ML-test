from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# создаем обучающую выборку
with open('objects.txt') as f:
    objects = [line.rstrip() for line in f] # список всех объектов
with open('classes.txt') as f:
    classes = [line.rstrip() for line in f]# соответствующие им классы
# подготавливаем данные для обучения
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(objects)
Y = classes
# обучаем классификатор
clf = svm.SVC()
clf.fit(X, Y)
# тестируем классификатор
test_objects = ['<script></script>'] # теги на странице, которые нужно классифицировать
X_test = vectorizer.transform(test_objects)
predicted_classes = clf.predict(X_test)
# выводим результаты
for i, obj in enumerate(test_objects):
    print(f"Tag '{obj}' is '{predicted_classes[i]}'")

import joblib
# сохранение модели
joblib.dump(clf, 'model.pkl')