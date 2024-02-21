# Добавить контакт
def add_contact():
    name = input('Введите имя: ')
    number_phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    with open('phone_book.txt', 'a+', encoding='utf-8') as data:
        data.seek(0)
        lines = data.readlines()
        line_count = len(lines) + 1
        data.write(f'{line_count}. {name}, {number_phone}, {comment}\n')
        print("Контакт успешно добавлен.")

# Удалить контакт
def remove_contact():
    with open('phone_book.txt', 'r', encoding='utf-8') as contacts:
        data = contacts.readlines()
        print(*data, sep='')
        index = int(input('Какой контакт нужно удалить?\nВыберите номер контакта: '))
        line_count = index - 1
        data.pop(line_count)
    with open('phone_book.txt', 'w', encoding='utf-8') as contacts:
        contacts.writelines(data)
        print("Контакт успешно удален.")


# Изменить контакт
def edit_contact():
    with open('phone_book.txt', 'r', encoding='utf-8') as contacts:
        data = contacts.readlines()
        print(*data, sep='')
        line = int(input('Введите номер строки, которую хотите изменить: '))
        new_name = input('Введите новое имя: ')
        new_number_phone = input('Введите новый номер телефона: ')
        new_comment = input('Введите новый комментарий: ')
        line_count = line - 1
        data[line_count] = (f'{line}. {new_name}, {new_number_phone}, {new_comment}\n')
        print('Контакт успешно изменен')
    with open('phone_book.txt', 'w', encoding='utf-8') as contacts:
        contacts.writelines(data)

# Показать все контакты            
def all_contacts():
    with open('phone_book.txt', 'r', encoding='utf-8') as contacts:
        data = contacts.readlines()
        print(*data, sep='')

# Ищет контакты по параметрам
def find_contact():
    with open('phone_book.txt', 'r', encoding='utf-8') as contacts:
        data = contacts.readlines()
    find = int(input("По какому параметру хотите найти контакт?\n 1 - Имя, 2 - Номер телефона, 3 - комментарий: "))
    if find == 1:
        name = input('Введите имя: ')
        found_contacts = []
        for contact in data:
            if name.lower() in contact.lower():
                found_contacts.append(contact.strip())
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Такого имени в списке нет")
    elif find == 2:
        number_phone = input('Введите номер телефона: ')
        found_contacts = []
        for contact in data:
            if number_phone.lower() in contact.lower():
                found_contacts.append(contact.strip())
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Такого номера телефона в списке нет")
    elif find == 3:
        comment = input('Введите комментарий: ')
        found_contacts = []
        for contact in data:
            if comment.lower() in contact.lower():
                found_contacts.append(contact.strip())
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Такого комментария в списке нет")
    else:
        print("Неверный ввод параметра")
