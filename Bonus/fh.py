import os


def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")
    except IOError:
        print(f"Failed to create file '{file_name}'.")
    else:
        print("File creation completed successfully.")
    finally:
        print("Create file operation completed.")


def write_to_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Content written to '{file_name}' successfully.")
    except IOError:
        print(f"Failed to write to file '{file_name}'.")
    else:
        print("File write operation completed successfully.")
    finally:
        print("Write to file operation completed.")


def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':")
            print(content)
    except IOError:
        print(f"Failed to read file '{file_name}'.")
    else:
        print("File read operation completed successfully.")
    finally:
        print("Read file operation completed.")


def append_to_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
            print(f"Content appended to '{file_name}' successfully.")
    except IOError:
        print(f"Failed to append to file '{file_name}'.")
    else:
        print("File append operation completed successfully.")
    finally:
        print("Append to file operation completed.")


def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to delete file '{file_name}'.")
    else:
        print("File deletion completed successfully.")
    finally:
        print("Delete file operation completed.")


def main():
    while(1):
        print("File operations:")
        print("1. Create a file")
        print("2. Write to a file")
        print("3. Read a file")
        print("4. Append to a file")
        print("5. Delete a file")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            file_name = input("Enter the file name: ")
            create_file(file_name)
        elif choice == "2":
            file_name = input("Enter the file name: ")
            content = input("Enter the content: ")
            write_to_file(file_name, content)
        elif choice == "3":
            file_name = input("Enter the file name: ")
            read_file(file_name)
        elif choice == "4":
            file_name = input("Enter the file name: ")
            additional_content = input("Enter additional content to append: ")
            append_to_file(file_name, additional_content)
        elif choice == "5":
            file_name = input("Enter the file name: ")
            delete_file(file_name)
        else:
            print("Invalid choice.")


if __name__ == '__main__':
    main()
