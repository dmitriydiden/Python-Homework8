import sqlite3
from turtle import title

with sqlite3.connect("database1.db") as db: 
    cursor = db.cursor()

    # cursor.execute("""CREATE TABLE IF NOT EXISTS staff(
    #     id INTEGER PRIMARY KEY,
    #     FIO VARCHAR(30),
    #     age INTEGER(3),
    #     sex INTEGER NOT NULL DEFAULT 1,
    #     department VARCHAR(100),
    #     title VARCHAR(100)
    # )""")

    # values = [
    #     ("Диденко Д.Н.", "43", "1", "Департамент логистики", "Директор по логистике"),
    #     ("Каруна Т.В.", "35", "2", "Финансово-экономический отдел", "Финансовый директор"),
    #     ("Дворяшина Н.Н.", "33", "2", "Департамент учета и отчетности", "Главный бухгалтер"),
    #     ("Золоторева М.А.", "26", "2", "Отдел по работе с персоналом", "Менеджер по работе с персоналом"),
    #     ("Лучин А.С.", "36", "1", "Департамент логистики", "Директор по транспорту")

    # ]

    # cursor.executemany("INSERT INTO staff(FIO, age, sex, department, title) VALUES(?, ?, ?, ?, ?)", values)
def data_output():
    try:
        db = sqlite3.connect("database1.db")
        cursor = db.cursor()   
    
        for data in cursor.execute("SELECT * FROM staff"): # Этот метод выводит все записи таблицы по строчно
            print(data)
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()

def registration():
    FIO = input("Введите Фамилию и инициалы сотрудника: ")
    age = int(input("Введите возраст сотрудника: "))
    sex = int(input("Введите пол сотрудника 1-муж./2-жен.: "))
    department = input("Введите название отдела/департамента: ")
    title = input("Введите должность сотрудника: ")

    try:
        db = sqlite3.connect("database1.db")
        cursor = db.cursor()

        cursor.execute("SELECT FIO FROM staff WHERE FIO = ?", [FIO])
        if cursor.fetchone() is None:
            values = [FIO, age, sex, department, title]

            cursor.execute("INSERT INTO staff(FIO, age, sex, department, title) VALUES(?, ?, ?, ?, ?)", values)
            db.commit()
            print("Сотрудник зарегистрирован!")
        else:
            print('Такой сотрудник уже существует!')
            registration()
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close() 

def delete_db(FIO):
    try:
        db = sqlite3.connect("database1.db")
        cursor = db.cursor()
    
        cursor.execute("DELETE FROM staff WHERE FIO = ?", [FIO])     
        db.commit()
        print("Запись удалена")
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()

def update_db(column_name, value, FIO):
    try:
        db = sqlite3.connect("database1.db")
        cursor = db.cursor()
    
        cursor.execute(f'UPDATE staff SET {column_name} = ? WHERE FIO = ?', (value, FIO))
        db.commit()
        print("Изменения внесены!")
    except sqlite3.Error as e:
        print("Error", e)
    finally:
        cursor.close()
        db.close()
 
