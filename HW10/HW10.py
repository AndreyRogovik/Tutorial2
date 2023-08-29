from collections import UserDict

def main():
    # обробляю команди віфд користувача 
    while True:
        command = input("Enter a command: ").lower()
        if command in ["hello", "hi"]:
            print("How can I help you?")
            
        elif command.startswith("add "):
            _, name, phone = command.split(" ", 2)
            bot.add_contact(name, phone)
        
        elif command.startswith("add_phone "):
            _, name, phone = command.split(" ", 2)
            bot.add_phone(name, phone)    
            
        # elif command.startswith("change "):
        #     _, name, phone = command.split(" ", 2)
        #     print(bot.change_phone(name, phone))
        
        elif command.startswith("find "):
            _, name = command.split(" ", 1) 
            bot.get_phone(name) 
                
        elif command == "show all":
            bot.show_all()
            
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")
            
            
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper
#  тут логіка яка виконується для команд.
class ContactBot:
    def __init__(self):
        self.contacts = {}

    def add_phone(self, name, phone):
        found_records = address_book.search_by_name(name)
        if found_records:
            record = found_records[0]  # Беремо перший знайдений запис
            record.add_phone(phone)
            print(f"Phone '{phone}' added to contact '{name}'.")
        else:
            print(f"No records found with name '{name}'.")
            
    @input_error
    def add_contact(self, name, phone):
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        print(f"Contact '{name}' with phone '{phone}' added to the address book.")

    # @input_error
    # # def change_phone(self, name, new_phone):
    # #     self.contacts[name] = new_phone
    # #     return f"Phone number for '{name}' updated to '{new_phone}'."
    
    @input_error
    def get_phone(self, name):
        found_records = address_book.search_by_name(name)
        if found_records:
            print(f"Found {len(found_records)} record(s) with name '{name}':")
            for record in found_records:
                print(f"Name: {record.name.get_value()}")
                for phone in record.phones:
                    print(f"Phone: {phone}")
            print("----------------------")
        else:
            print(f"No records found with name '{name}'.")
            print("----------------------")

    
    @input_error
    def show_all(self):
        if not address_book.data:
            print("No contacts saved.")
        else:
            print("All contacts:")
            for record in address_book.values():
                print(f"Name: {record.name.get_value()}")
                for phone in record.phones:
                    print(f"Phone: {phone}")
                print("----------------------")



class Field:
    def __init__(self, value=None):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


class Name(Field):
    def set_value(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        super().set_value(value)
        
        
class Phone(Field):
    def add_phone(self, phone_number):
        self.value.append(phone_number)

    def remove_phone(self, phone_number):
        if phone_number in self.value:
            self.value.remove(phone_number)

    def remove_phone(self, phone_number):
        if phone_number in self.value:
            self.value.remove(phone_number)


class Record:
    def add_phone(self, phone_number):
        self.phones.append(phone_number)
        
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(phone_number)

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.get_value()] = record

    def search_by_name(self, name):
        found_records = []
        for record in self.data.values():
            if record.name.get_value().lower() == name.lower():
                found_records.append(record)
        return found_records


bot = ContactBot()
address_book = AddressBook()



if __name__ == "__main__":
    main()