import secrets
import string

DEFAULT_PUNC_STRING = ['!', '@', '#', '$', '%', '^', '&', '*', '_', ',', '.']

UPPERCASE_PROMPT = "Enter the number of uppercase alphabetic characters in the password: "
LOWERCASE_PROMPT = "Enter the number of lowercase alphabetic characters in the password: "
NUMERIC_PROMPT = "Enter the number of numeric characters in the password: "
TARGET_APPLICATION_PROMPT = "Enter the target application for the password: "

def get_characters(prompt, characters):
    while True:
        try:
            count = int(input(prompt))
            if count < 0:
                print("Please enter a non-negative integer.")
            else:
                chosen = [secrets.choice(characters) for _ in range(count)]
                print(f"The characters chosen for the password are: {chosen}")
                return chosen
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def get_puncs():
    while True:
        print(f"Default punctuation symbols: {DEFAULT_PUNC_STRING}")
        
        choice = input("Do you want to exclude any punctuation symbols? (y/n): ")[0]
        if choice.lower() == 'y':
            excluded = input("Enter the characters to exclude (without spaces): ")
            excluded_puncs = list(excluded)
            allowed_puncs = [p for p in DEFAULT_PUNC_STRING if p not in excluded_puncs]
            print(f"The allowed punctuation symbols are: {allowed_puncs}")
            return allowed_puncs
        elif choice.lower() == 'n':
            return DEFAULT_PUNC_STRING
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def generate():
    target_application = input(TARGET_APPLICATION_PROMPT)
    
    uppercase_chars = get_characters(UPPERCASE_PROMPT, string.ascii_uppercase)
    lowercase_chars = get_characters(LOWERCASE_PROMPT, string.ascii_lowercase)
    numeric_chars = get_characters(NUMERIC_PROMPT, string.digits)
    punctuation_chars = get_puncs()

    usable = uppercase_chars + lowercase_chars + numeric_chars + punctuation_chars
    print(f"The usable characters are: {usable}")
    
    while True:
        choice = input("Do you want to shuffle? (y/n): ")[0]
        if choice.lower() == 'y':
            secrets.SystemRandom().shuffle(usable)
        elif choice.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    password = "".join(usable)

    return password

def main():
    print("\t----PASSWORD GENERATION----\t")
    while True:        
        password = generate()
        print(f"Generated Password: {password}")
        choice = input("Are you satisfied with the password? (y/n): ")
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            print("\t----PASSWORD REGENERATION----\t")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
