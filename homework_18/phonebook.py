import sys
from src import (
    read_dataset,
    write_dataset,
    print_commands,
    print_result,
    read_values,
    create,
    update,
    delete,
    search_record,
)


def main_func(file_path):
    dataset = read_dataset(file_path)
    if dataset is None:
        print(
            "You must pass the name of the phonebook as an argument on the command line. \n Example: $ python main.py <myphonebook.json>"
        )
        sys.exit()
    print_commands()
    while True:
        command = input("Enter a command from the list: ")
        if command == "print":
            print_result(dataset)
        elif command == "new":
            values = read_values()
            dataset = create(dataset, values)
            write_dataset(dataset, file_path)
        elif command == "sf":
            value = input("Enter a first name: ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "sl":
            value = input("Enter a last name: ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "sfl":
            value = input("Enter a full name: ").split(" ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "sp":
            value = input("Enter your phone number: ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "sct":
            value = input("Enter City: ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "sc":
            value = input("Enter Country: ")
            result = search_record(dataset, command, value)
            print_result(result)
        elif command == "up":
            result = read_values()
            dataset = update(dataset, result)
            write_dataset(dataset, file_path)
        elif command == "del":
            value = input("Enter your phone number to delete: ")
            delete(dataset, value)
            write_dataset(dataset, file_path)
        elif command == "help":
            print_commands()
        elif command == "exit":
            write_dataset(dataset, file_path)
            break
        else:
            print("This command is not available")


if __name__ == "__main__":
    try:
        script, ph_book_name = sys.argv
        ph_book_name = "database/" + ph_book_name
    except ValueError:
        ph_book_name = "0"
    main(ph_book_name)
