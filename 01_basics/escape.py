def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the ASCII base (uppercase or lowercase)
            ascii_base = ord('A') if char.isupper() else ord('a')
            # Shift within the range of 26 letters
            new_position = (ord(char) - ascii_base + shift) % 26
            # Append the new character to encrypted_text
            encrypted_text += chr(ascii_base + new_position)
        else:
            # If not a letter, keep the character as it is (e.g., spaces or punctuation)
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            ascii_base = ord('A') if char.isupper() else ord('a')
            new_position = (ord(char) - ascii_base - shift) % 26
            decrypted_text += chr(ascii_base + new_position)
        else:
            decrypted_text += char
    return decrypted_text

# Example usage
text = "Hello World!"
shift = 3

encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)
