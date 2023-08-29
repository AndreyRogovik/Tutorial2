import collections
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

class Field:
    def __init__(self, value=None):
        self.value = value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_records(self, criteria):
        results = []
        for name, record in self.data.items():
            if criteria.lower() in name.lower():
                results.append(record)
        return results

def main():
    bot = ContactBot()
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            _, name, phone = command.split(" ", 2)
            print(bot.add_contact(name, phone))
        elif command.startswith("change "):
            _, name, phone = command.split(" ", 2)
            print(bot.change_phone(name, phone))
        elif command.startswith("phone "):
            _, name = command.split(" ", 1)
            print(bot.get_phone(name))
        elif command.startswith("search "):
            _, criteria = command.split(" ", 1)
            results = bot.search_records(criteria)
            if results:
                print("Search results:")
                for record in results:
                    print(f"Name: {record.name.value}")
                    print("Phones:", ", ".join(phone.value for phone in record.phones))
                    print()
            else:
                print("No matching records found.")
        elif command == "show all":
            print(bot.show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return str(e)
    return wrapper

class ContactBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return f"Contact '{name}' with phone '{phone}' added."

    @input_error
    def change_phone(self, name, new_phone):
        self.contacts[name] = new_phone
        return f"Phone number for '{name}' updated to '{new_phone}'."

    @input_error
    def get_phone(self, name):
        return f"Phone number for '{name}': {self.contacts[name]}"

    def show_all(self):
        if not self.contacts:
            return "No contacts saved."
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        return f"All contacts:\n{contact_list}"

def main():
    bot = ContactBot()
    while True:
        command = input("Enter a command: ").lower()
        
        if command == "hello":
            print("How can I help you?")
        elif command.startswith("add "):
            _, name, phone = command.split(" ", 2)
            print(bot.add_contact(name, phone))
        elif command.startswith("change "):
            _, name, phone = command.split(" ", 2)
            print(bot.change_phone(name, phone))
        elif command.startswith("phone "):
            _, name = command.split(" ", 1)
            print(bot.get_phone(name))
        elif command == "show all":
            print(bot.show_all())
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()