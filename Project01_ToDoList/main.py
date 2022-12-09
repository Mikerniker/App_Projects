while True:
    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("todos.txt", "r") as file:
                todos = file.readlines()  

            todos.append(todo)
            
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            
        case 'show':

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.title().strip('\n')
                print(f"{index + 1}-{item}")

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            
            with open("todos.txt", "r") as file:
                todos = file.readlines()
                
            new_todo = input("Add your new todo: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)
   
   
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open("todos.txt", "r") as file:
                todos = file.readlines()
         
            todos.pop(number-1)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case 'exit':
            break
        case whatever:
            print("Hey, you entered an unknown command.")


print("Bye!")


