def correct_input(prompt, option1, option2):
    # Ensure input is one of two valid options
    while True:
        user_input = input(prompt).lower()
        if user_input in (option1, option2):
            return user_input
        print(f'Enter {option1} or {option2}')

def algorithm(shift_step, text, to_do):
    # Encrypt or decrypt text depending on user choice
    return caesar_cipher(-shift_step if to_do == 'd' else shift_step, text)

def caesar_cipher(step, text):
    en = 'abcdefghijklmnopqrstuvwxyz'
    ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    result = []

    for i in text:
        if i.lower() in en:
            index = (en.find(i.lower()) + step) % len(en)  # circular shift
            result.append(en[index].upper() if i.isupper() else en[index])
        elif i.lower() in ru:
            index = (ru.find(i.lower()) + step) % len(ru)
            result.append(ru[index].upper() if i.isupper() else ru[index])
        else:
            result.append(i)  # keep non-alphabetic characters unchanged

    return ''.join(result)

# Collect user input
language = correct_input('Choose a language: En or Ru: ', 'en', 'ru')
to_do = correct_input('What to do: Encryption (e) or Decryption (d)', 'e', 'd')
text = input('Enter text: ')
shift_step = int(input('Shift step: '))

# Run cipher
print(algorithm(shift_step, text, to_do))
