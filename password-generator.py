import secrets
import string
import os
import pyperclip

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def press_menu():
    input("\nPress Enter to return to the menu...")

def get_password_length():
    print("------------------------")
    try:
        password_length = int(input("Password length: "))
    except ValueError:
        print("Password length must be a number.")
        return None

    if password_length <= 0:
        print("Password length must be greater than 0.")
        return None

    return password_length

def generate_password(length, characters):
    print("------------------------")
    print(f"Generating password with length {length}...")
    return ''.join(secrets.choice(characters) for _ in range(length))

def copy_and_show_password(password):
    pyperclip.copy(str(password))
    print("\n------------------------")
    print("[✓] Password generated successfully.")
    print("[✓] Copied to clipboard.")
    print("------------------------")
    print("Password: " + password)

def create_password():
    numbers = True
    letters = False
    symbols = False
    password_length = 100
    
    while True:
        clear_screen()

        print("========================\n OPTIONS\n========================")
        print("[1] Numbers: " + ("ON" if numbers else "OFF"))
        print("[2] Letters: " + ("ON" if letters else "OFF"))
        print("[3] Symbols: " + ("ON" if symbols else "OFF"))   
        print(f"[4] Password length: {password_length}" + (" (default)" if password_length == 100 else ""))
        print("[5] Generate password")
        print("[6] Back to menu")

        input_key = input("> ")

        match input_key:
            case "1":
                numbers = not numbers
            case "2":
                letters = not letters
            case "3":
                symbols = not symbols
            case "4":
                password_length = get_password_length()
                if password_length is None:
                    print("Password length must be greater than 0.")
                    print("Reset to default.")
                    password_length = 100
                    press_menu()
                    continue
            case "5":
                if password_length is None:
                    press_menu()
                    continue
                
                characters = ""
                if numbers:
                    characters += string.digits
                if letters:
                    characters += string.ascii_letters
                if symbols:
                    characters += string.punctuation

                if not characters:
                    print("No character types selected. Please select at least one.")
                    press_menu()
                    continue
               
                clear_screen()
                password = generate_password(password_length, characters)
                copy_and_show_password(password)
                press_menu()
                break
            case "6":
                break
            case _:
                print("Invalid option. Try again.")
                press_menu()

def create_words_password():
    clear_screen()
    
    name_file = input("Enter wordlist file path: ")

    try:
        with open(name_file, "r") as file:
            words = [line.strip() for line in file if line.strip()]
            print("Words loaded from file.")
    except FileNotFoundError:
        print("File not found.")
        press_menu()
        return
    
    length_password = get_password_length()

    if length_password is None:
        print("Password length must be greater than 0.")
        press_menu()
        return
    
    separator = input("Enter the separator (default is space): ") or " "
    
    
    if (length_password <= len(words)):
        password = separator.join(secrets.SystemRandom().sample(words, length_password))
    else:
        password = separator.join(secrets.choice(words) for _ in range(length_password))

    clear_screen()
    copy_and_show_password(password)
    press_menu()


def main():
    while True:
        clear_screen()
        print("\n========================\n PASSWORD TOOL\n========================")
        print("[1] Start password generation")
        print("[2] Generate passphrase")
        print("[3] exit")
        input_key = input("> ")

        match input_key:
            case "1":
                create_password()
            case "2":
                create_words_password()
            case "3":
                break
            case _:
                print("Invalid option. Try again.")
                press_menu()
    print("\nGoodbye!")
                
if __name__ == "__main__":
    main()