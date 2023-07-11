
from datetime import datetime

''' Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл,
уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, 
выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.

Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.

Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой).
Реализацию пользовательского интерфейса студент может делать как ему удобнее,
можно делать как параметры запуска программы (команда, данные),
можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.
'''
def show():                                                                     # Печать всей базы
    with open(FILE_PATH,'r',encoding='utf-8') as base:
        print(base.read())

def add():                                                                      # Добавление новой записи в файл
    with open(FILE_PATH, 'r') as file:                                          # Считает количество строк в файле и нумерует их 
        id=str(len(file.readlines())+1)
    name=input("Введите название заметки: ")
    now=datetime.now()                                                          # текущее время
    date=now.strftime("%d.%m.%Y %H:%M")                                         # Запись текущего времени в строку
    notes=input("Напишите заметку: ")

    with open(FILE_PATH,'a',encoding='utf-8') as base:
        base.write(id+';'+name+';'+date+';'+notes+'\n')




FILE_PATH = r"control_work_01\base.txt"                                             # Начальная база

while True:
    print()                                                                 # Печать списка допустимых команд
    print('[1] Показать весь список заметок')
    print('[2] Добавить')
    print('[3] Поиск')
    print('[4] Редактировать')
    print('[5] Удалить')
    print('[6] Выход')
    print()
    Command = int(input("Введите номер команды: "))

    if Command ==1:                                                                 # Выполнение команды
        show()
    elif Command==2:
        add()
    elif Command==3:
        search()
    elif Command==4:
        edit()
    elif Command==5:
        delete()
    else: break