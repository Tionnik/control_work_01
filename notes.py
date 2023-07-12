
from datetime import datetime
import os

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
def id(line):                                                                   # Извлечение id из строки
   mass = line.split(";")
   return int (mass[0])

def show():                                                                     # Печать всей базы
    with open(FILE_PATH,'r',encoding='utf-8') as base:
        print(base.read())

def add():                                                                      # Добавление новой записи в файл
    now=datetime.now()                                                          # текущее время
    new_id=now.strftime("%Y%m%d%H%M%S")                                             # 
    date=now.strftime("%d.%m.%Y %H:%M")                                         # Запись текущего времени в строку
    name=input("Введите название заметки: ")
    notes=input("Напишите заметку: ")

    with open(FILE_PATH,'a',encoding='utf-8') as base:
        base.write(new_id+';'+date+';'+name+';'+notes+'\n')

def edit():                                                                   # Замена выбранной строки
    index=int(input("Введите id строки для замены: "))
    with open(FILE_PATH,'r',encoding='utf-8') as base1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:
            while True:
                info=base1.readline()
                if info:
                    if index != id(info):
                        base2.write(info)
                    else:
                        print(info)
                        now=datetime.now()                                                          # текущее время
                        new_id=now.strftime("%Y%m%d%H%M%S")                                             # 
                        date=now.strftime("%d.%m.%Y %H:%M")                                         # Запись текущего времени в строку
                        name=input("Введите новое название заметки: ")
                        notes=input("Напишите заметку: ")
                        no_whrite=input("Если хотите изменить заметку наберите [1], если нет наберите [0] ")
                        if int (no_whrite) ==1:
                            base2.write(new_id+';'+date+';'+name+';'+notes+'\n')
                        else:
                            base2.write(info)
                else:
                    break
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)

def delete():                                                                   # Удаление выбранной строки
    index=int(input("Введите id строки: "))
    with open(FILE_PATH,'r',encoding='utf-8') as base1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as base2:
            while True:
                info=base1.readline()
                if info:
                    if index != id(info):
                        base2.write(info)
                else:
                    break
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)
    print("Все готово")


FILE_PATH = r"control_work_01\base.txt"                                             # Начальная база
FILE_PATH_TEMP = r"control_work_01\base_temp.txt"

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

    # implemented