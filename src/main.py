#To use the sting pre configurated
import string
#Module to generete secure random numbers, and ohter features
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length: int, symbols: bool, uppercase: bool) -> str :
    combination: str = string.ascii_lowercase + string.digits
    
    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase
    combination_length = len(combination)
    new_password: str = ''
    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    print(new_password)
    if not contains_symbols(new_password):
        random_symbols: str = secrets.choice(string.punctuation)
        new_password_length: int = len(new_password)
        new_password_list: list[str] = [char for char in new_password]
        new_password_list[secrets.randbelow(new_password_length)] = random_symbols
        new_password = ''.join(new_password_list)

    elif not contains_upper(new_password):
        random_symbols: str = secrets.choice(string.ascii_uppercase)
        new_password_length: int = len(new_password)
        new_password_list: list[str] = [char for char in new_password]
        new_password_list[secrets.randbelow(new_password_length)] = random_symbols
        new_password = ''.join(new_password_list)
    
    return new_password

if __name__ == "__main__":
    for i in range(1,2):
        new_pass: str = generate_password(length=3,symbols=True,uppercase=True)
        print(f"{i} -> {new_pass} (U: {contains_upper(new_pass)} S: {contains_symbols(new_pass)})")