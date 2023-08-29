# Імпортуємо клас UserDict з модуля collections
from collections import UserDict

# Клас для представлення адресної книги, який успадковує клас UserDict
class AddressBook(UserDict):
    # Метод для додавання запису до книги
    def add_record(self, record):
        self.data[record.name.value] = record # саме обьект классу record

    # Метод для видалення запису з книги
    def remove_record(self, record_name):
        if record_name in self.data:
            del self.data[record_name]

    def remove_phone(self, record_name, phone_value):
        record = self.data.get(record_name)
        if record:
            record.remove_phone(phone_value)
            print(f"Номер телефону '{phone_value}' видалено з запису '{record_name}'.")
        else:
            print(f"Запис '{record_name}' не знайдено.")
        print("Оновлений список записів:")
        for name in self.data.keys():
            print(name)

# Клас для представлення запису
class Record:
    def __init__(self, name_value):
        self.name = Name(name_value)  # Створюємо об'єкт класу Name
        self.phones = []  # Список для збереження об'єктів класу Phone

    # Метод для додавання номера телефону до запису
    def add_phone(self, phone_value):
        self.phones.append(Phone(phone_value))

    # Метод для видалення номера телефону з запису
    def remove_phone(self, phone_value):
        self.phones = [phone for phone in self.phones if phone.value != phone_value]

# Базовий клас для представлення поля
class Field:
    def __init__(self, value):
        self.value = value

# Клас для представлення імені (спеціальний випадок поля)
class Name(Field):
    pass

# Клас для представлення номера телефону (спеціальний випадок поля)
class Phone(Field):
    pass

# Головна функція для виконання програми
def main():
    book = AddressBook()  # Створюємо об'єкт адресної книги
    while True:
        command = input("Введіть команду: ").lower()

        if command == "hello":
            print("Як я можу вам допомогти?")
            
        elif command.startswith("add record "):
            _, _, record_name = command.split(" ", 2)
            record = Record(record_name)
            book.add_record(record_name, record)
            print(f"Запис '{record_name}' додано.")
            
        elif command.startswith("remove record "):
            _, _, record_name = command.split(" ", 2)
            book.remove_record(record_name)
            print(f"Запис '{record_name}' видалено.")
            
        elif command.startswith("add phone "):
            _, _, record_name, phone_value = command.split(" ", 3)
            record = book.data.get(record_name)
            if record:
                record.add_phone(phone_value)
                print(f"Номер телефону '{phone_value}' додано до запису '{record_name}'.")
            else:
                print(f"Запис '{record_name}' не знайдено.")
        elif command.startswith("remove phone "):
            _, record_name, phone_value = command.split(" ", 2)
            book.remove_phone(record_name, phone_value)
            
        elif command == "show all":
            # Виводимо лише назви записів, розділені комами
            record_names = ", ".join(book.data.keys())
            print(record_names)
            
        elif command in ["good bye", "close", "exit"]:
            print("До побачення!")
            break
        
        else:
            print("Невідома команда. Будь ласка, спробуйте ще раз.")

if __name__ == "__main__":
    main()
