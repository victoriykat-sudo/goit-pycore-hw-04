def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [ім'я] [номер телефону]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [ім'я] [новий номер телефону]"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [ім'я]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts saved."
    result = "All contacts:\n" + "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")
        
        elif command in commands:
            if command == "all":
                print(commands[command](contacts))
            else:
                print(commands[command](args, contacts))
        
        elif command:
             print("Invalid command.")
        else:
             print("Please enter a command.")

if __name__ == "__main__":
    main()