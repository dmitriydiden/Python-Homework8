import interface
import data_processing

def control():
    number_operation = 0
    while number_operation != 4:
        number_operation = int(interface.inter())
        if number_operation == 1:
            data_processing.data_output()
        elif number_operation ==2:
            data_processing.registration()
        elif number_operation == 3:
            family_name = input("Введите Фамилию и инициалы сотрудника запись по которому хотите удалить: ")
            data_processing.delete_db(family_name)
        elif number_operation == 4:
            family_name = input("Введите Фамилию и инициалы сотрудника запись по которому хотите изменить: ")
            number = int(input("Введите номер столбца данные в которм хотите изменить: \n Фамилия -1, Возраст - 2, Пол - 3, Название отдела - 4, Название должности - 5: "))
            value = input("Введите текст изменения: ")
            if number == 1:
                column_name = 'FIO'
            if number == 2:
                column_name = 'age'
            if number == 3:
                column_name = 'sex'
            if number == 4:
                column_name = 'department'
            if number == 5:
                column_name = 'title'
            data_processing.update_db(column_name, value, family_name)
        elif number_operation ==5:
            break
