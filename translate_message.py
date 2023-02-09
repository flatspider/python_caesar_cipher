import string


def translate_message(message, shift):

    converted_message = ""

    lower_alphabet_bank = string.ascii_lowercase
    upper_alphabet_bank = string.ascii_uppercase

    # Each letter needs to be converted to a number.
    # Does it correspond with an upper letter or a lowercase letter?
    # Zero index is A.

    for each in range(0, len(message)):
        char = message[each]
        if (char.isalpha()):
            if (char.isupper()):
                # ASCII modification to get a value 0 to 25
                char_value = ord(char) - 65
                char_value = (char_value + shift) % 26
                converted_message = converted_message + \
                    upper_alphabet_bank[char_value]
            else:
                char_value = ord(char) - 97
                char_value = (char_value + shift) % 26
                converted_message = converted_message + \
                    lower_alphabet_bank[char_value]
        else:
            converted_message = converted_message + message[each]

    print(f'Here is your encrypted message: {converted_message}')

    # Take in a message. "duck"
    # Read in the key (shift parameter)
    # Apply the shift to each letter in the message.
    # Ignore spaces, periods, commas, etc.
    # if letter, convert to that letter plus key.
    # I need an alphabet key.
    # Cycle through each character in the message array.
    # If letter is alpha, then proceed to apply alphabet shift.
    #

# translate_message('fizz,BU3ZZ', 3)


message = input("Please type your message: ")
shift = int(input("Encrypt using what number? "))

translate_message(message, shift)


def decrypt_message(message, shift):

    converted_message = ""

    lower_alphabet_bank = string.ascii_lowercase
    upper_alphabet_bank = string.ascii_uppercase

    # Each letter needs to be converted to a number.
    # Does it correspond with an upper letter or a lowercase letter?
    # Zero index is A.

    for each in range(0, len(message)):
        char = message[each]
        if (char.isalpha()):
            if (char.isupper()):
                # ASCII modification to get a value 0 to 25
                char_value = ord(char) - 65
                char_value = (char_value - shift) % 26
                converted_message = converted_message + \
                    upper_alphabet_bank[char_value]
            else:
                char_value = ord(char) - 97
                char_value = (char_value - shift) % 26
                converted_message = converted_message + \
                    lower_alphabet_bank[char_value]
        else:
            converted_message = converted_message + message[each]

    print(f'Here is your decrypted message: {converted_message}')


message = input("Please type your encrypted message: ")
shift = int(input("Decrypt using what number? "))

decrypt_message(message, shift)
