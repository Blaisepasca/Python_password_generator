import random
import string

def generate_password(min_length, has_number, has_special):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    all_chars = letters

    if has_number:
        all_chars += digits
    if has_special:
        all_chars += special_chars

    password = ""
    meets_criteria = False  # ✅ Initialisation obligatoire

    while not meets_criteria or len(password) < min_length:
        password = "".join(random.choice(all_chars) for _ in range(min_length))

        # Vérification des critères
        has_num = any(char in digits for char in password)
        has_spec = any(char in special_chars for char in password)

        if has_number and not has_num:
            meets_criteria = False
        elif has_special and not has_spec:
            meets_criteria = False
        else:
            meets_criteria = True

    return password

# === Partie principale ===
min_length = int(input("Enter the minimum Length : "))
has_number = input("Do you want to have numbers (y/n): ").lower() == "y"
has_special = input("Do you want to have special (y/n): ").lower() == "y"

pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
