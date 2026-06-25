import secrets
import string
import os
import pyperclip

DEFAULT_PASSWORD_LENGTH = 100

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

def press_menu() -> None:
    input("\nPress enter to continue...")

def get_password_length() -> int:
    while True:
        print("------------------------")
        try:
            password_length = int(input("Password length: "))
        except ValueError:
            print("[ERROR] Password length must be a number.")
            press_menu()
            continue

        if password_length <= 0:
            print("[ERROR] Password length must be greater than 0.")
            press_menu()
            continue

        break

    return password_length

def generate_password(length: int, characters: str) -> str:
    print("------------------------")
    print(f"Generating password with length {length}...")
    return ''.join(secrets.choice(characters) for _ in range(length))

def copy_and_show_password(password: str) -> None:
    print("------------------------")
    print("[OK] Password generated successfully.")
    try:
        pyperclip.copy(password)
        print("[OK] Copied to clipboard.")
    except pyperclip.PyperclipException:
        print("[ERROR] Could not copy to clipboard.")
    print("------------------------")
    print(f"Password: {password}")

def create_password() -> None:
    numbers = True
    letters = False
    symbols = False
    password_length = DEFAULT_PASSWORD_LENGTH
    
    while True:
        clear_screen()

        print("========================\n OPTIONS\n========================")
        print("[1] Numbers: " + ("ON" if numbers else "OFF"))
        print("[2] Letters: " + ("ON" if letters else "OFF"))
        print("[3] Symbols: " + ("ON" if symbols else "OFF"))   
        print(f"[4] Password length: {password_length}" + (" (default)" if password_length == DEFAULT_PASSWORD_LENGTH else ""))
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
            case "5":
                characters = ""
                if numbers:
                    characters += string.digits
                if letters:
                    characters += string.ascii_letters
                if symbols:
                    characters += string.punctuation

                if not characters:
                    print("[ERROR] No character types selected. Please select at least one.")
                    press_menu()
                    continue
               
                clear_screen()
                password = generate_password(password_length, characters)
                copy_and_show_password(password)
                press_menu()
            case "6":
                break
            case _:
                print("[ERROR] Invalid option. Try again.")
                press_menu()

def create_words_password() -> None:
    clear_screen()
    
    name_file = input("Enter wordlist file path: ")

    try:
        with open(name_file, "r", encoding="utf-8") as file:
            words = [line.strip() for line in file if line.strip()]
            print("Words loaded from file.")
    except FileNotFoundError:
        print("[ERROR] File not found.")
        press_menu()
        return
    
    if not words:
        print("[ERROR] Wordlist is empty.")
        press_menu()
        return
    
    length_password = get_password_length()
    
    separator = input("Enter the separator (default is space): ") or " "
    
    print("------------------------")
    print(f"Generating password with length {length_password}...")
    
    if length_password <= len(words):
        password = separator.join(secrets.SystemRandom().sample(words, length_password))
    else:
        password = separator.join(secrets.choice(words) for _ in range(length_password))

    clear_screen()
    copy_and_show_password(password)
    press_menu()


def main() -> None:
    while True:
        clear_screen()
        print("\n========================\n PASSWORD TOOL\n========================")
        print("[1] Start password generation")
        print("[2] Generate passphrase")
        print("[3] Exit")
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