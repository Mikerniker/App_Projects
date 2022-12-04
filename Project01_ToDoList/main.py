todos = []

while True:
    user_action = input("Type add, show, or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case whatever:
            print("Hey, you entered an unknown command.")

print("test")

print("Bye!")