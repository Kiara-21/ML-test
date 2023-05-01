import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.styles import Font, Color, PatternFill, Alignment

# получаем код HTML-страницы
url = 'http://opencart.qatestlab.net/'
response = requests.get(url)
html_res = response.text
# обрабатываем HTML-страницу с помощью BeautifulSoup
soup = BeautifulSoup(html_res, 'html.parser')
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
class_list = []
def classify_tags(html_res, clf, input_list, class_list):
    # тестируем классификатор
    count = 0
    for item in input_list:
        bn = item
        bn=str(item)
        test_objects = [bn] # теги на странице, которые нужно классифицировать
        X_test = vectorizer.transform(test_objects)
        predicted_classes = clf.predict(X_test)
        for i, obj in enumerate(test_objects):
          #  print(f"Tag '{obj}' is '{predicted_classes[i]}'")
            class_list.append(predicted_classes[i])
            if predicted_classes[i] == '"Зображення"':
                count += 1
        test_objects.clear()
    print(f"Найдено {count} тегов из группы 'Зображення'")
classify_tags(html_res, clf, input_list, class_list)
print(class_list)
class_list = list(set(class_list))
print(class_list)

def write_to_excel(checklist, class_list, url):
    wb = openpyxl.Workbook()
    sheet = wb.active

    sheet.column_dimensions['B'].width = 50
    sheet.row_dimensions[1].height = 40
    cell_B1 = sheet["B1"]
    cell_B1.font = Font(size=12, color='FF0000')
    cell_B1.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    cell_B1.alignment = Alignment(horizontal='center', vertical='center')
    
    cell_range = sheet['C1:F1']
    for row in cell_range:
        for cell in row:
            cell.font = Font(size=12, color='FF0000')
            cell.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
            cell.alignment = Alignment(horizontal='center', vertical='center')
    
    sheet.column_dimensions['C'].width = 25
    sheet.column_dimensions['D'].width = 25
    sheet.column_dimensions['E'].width = 25
    sheet.column_dimensions['F'].width = 25

    sheet.column_dimensions['G'].width = 30
    sheet.column_dimensions['H'].width = 30
    cell_G1 = sheet["G1"]
    cell_G1.font = Font(size=12, color='FF0000')
    cell_G1.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    cell_G1.alignment = Alignment(horizontal='center', vertical='center')
    cell_H1 = sheet["H1"]
    cell_H1.font = Font(size=12, color='FF0000')
    cell_H1.fill = PatternFill(start_color='FFFF00', end_color='FFFF00', fill_type='solid')
    cell_H1.alignment = Alignment(horizontal='center', vertical='center')

    b1_text = "Сайт: " + url
    b1_text = str(b1_text)
    sheet["B1"] = b1_text
    sheet["C1"] = "Firefox 112.0.2"
    sheet["D1"] = "Google Chrome 100.0.4896.75"
    sheet["E1"] = "Opera 75.0.3969.171"
    sheet["F1"] = "Safari 14.1.2"
    sheet["G1"] = "Посилання на баг-репорт"
    sheet["H1"] = "Примітка"
  
    if "Меню навігації" in class_list:
        sheet["A2"] = 1
        sheet["B2"] = "Перевірка стилю"
        sheet["B3"] = "Зображення категорій"
        sheet["B4"] = "Клікабельність посилань"
        sheet["B4"] = "Активні елементи"
    else:
       print("Элемент Меню навігації не содержится в списке")

write_to_excel("checklist.xlsx", class_list, url)
