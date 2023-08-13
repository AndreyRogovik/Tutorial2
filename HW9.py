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
