def save_contacts(contacts, filename):
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")

def load_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                name, phone = line.strip().split(': ')
                contacts[name] = phone
            return contacts
    except FileNotFoundError:
        return {}

def add_contact(contacts):
    name = input("Введите имя контакта: ")
    surname = input("Введите фамилию контакта: ")
    phone = input("Введите номер телефона: ")
    contacts[f"{name} {surname}"] = phone
    print("Контакт успешно добавлен.")

def search_contact(contacts):
    query = input("Введите имя или фамилию контакта для поиска: ")
    found = False
    for name, phone in contacts.items():
        if query.lower() in name.lower():
            print(f"Найден контакт: {name}, телефон: {phone}")
            found = True
    if not found:
        print("Контакт не найден.")

def copy_string(contacts):
    n = int(input("Введите номер строки: "))
    keys_list = list(contacts.keys())
    if n >= len(keys_list):
        print("Введенный номер строки больше, чем количество строк в контактах.")
        return
    key_to_copy = keys_list[n]
    with open("string_with_phone.txt", 'a') as r:
        r.write(f"{key_to_copy}: {contacts[key_to_copy]}\n")
def main():
    contacts_filename = 'contacts.txt'
    contacts = load_contacts(contacts_filename)

    while True:
        print("\n1. Добавить контакт")
        print("2. Поиск контакта")
        print("3. Скопировать строку")
        print("4. Выйти")

        choice = input("Выберите действие: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contact(contacts)
        elif choice == '3':
            copy_string(contacts)
        elif choice == '4':
            save_contacts(contacts, contacts_filename)
            print("Справочник сохранен.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()