import requests
from bs4 import BeautifulSoup

# получаем код HTML-страницы
url = 'http://opencart.qatestlab.net/'
response = requests.get(url)
html = response.text
# обрабатываем HTML-страницу с помощью BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')
# извлекаем нужные элементы страницы, например, заголовок
title = soup.title.string
print(title)
inputs = soup.find_all()
input_list = []
for input_tag in inputs:
    input_list.append(input_tag)

import joblib
# загрузка модели
clf = joblib.load('model.pkl')

# функция классификации тегов на странице
def classify_tags(html, clf, input_list):
    # тестируем классификатор
    for item in input_list:
        bn = item
        bn=str(item)
        test_objects = [bn] # теги на странице, которые нужно классифицировать
        X_test = vectorizer.transform(test_objects)
        predicted_classes = clf.predict(X_test)
        for i, obj in enumerate(test_objects):
            print(f"Tag '{obj}' is '{predicted_classes[i]}'")

classify_tags(html, clf, input_list)
