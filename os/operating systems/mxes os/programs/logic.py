def generate_base_characters():
    digits = "0123456789"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    extra_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    base_characters = []

    # Combine all characters
    all_chars = digits + upper_case + lower_case + extra_chars

    # Base 2 to 100
    for i in range(2, 95):
        base_characters.append(all_chars[:i])

    return base_characters

base_characters = generate_base_characters()

# Print characters for each base
for base, chars in enumerate(base_characters, start=2):
    print(f"Base {base}: {chars}")
