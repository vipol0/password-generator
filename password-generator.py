import random
import string 

def create_password():
    password_status = input("enter what the password will consist of(value or string): ")
    password_length = int(input("enter the password length: "))

    if password_length <= 0:
        print("password must be longer than 0")
        return

    match password_status: 
        case "value":
            min_value = 10**(password_length - 1)
            max_value = (10**password_length) - 1
            result = random.randint(min_value, max_value)
            print("password: " + str(result))

        case "string":
            result = ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=password_length
            ))
            print("password: " + result)

        case _:
            print("unknown command")


while True:
    input_key = input("enter command(exit, pws): ")

    if input_key == "exit":
        break
    elif input_key == "pws":
        сreate_password()
