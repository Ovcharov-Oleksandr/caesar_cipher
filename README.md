# Caesar Cipher (Python Script)

This is a Python script that allows you to **encrypt and decrypt text** using the **Caesar cipher**.
It supports both **English** and **Russian** alphabets and preserves the case of letters. Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged.

---

## Features

- Supports **encryption** (`e`) and **decryption** (`d`)
- Works with **English (`en`)** and **Russian (`ru`)** alphabets
- Preserves **uppercase and lowercase letters**
- Ignores non-alphabetic characters
- Simple **command-line interface** (input prompts)

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Open a terminal or command prompt.
3. Navigate to the folder containing `caesar_cipher.py`.
4. Run the script:

```bash
python caesar_cipher.py
```

5. Follow the prompts:
   - Choose language: `en` (English) or `ru` (Russian)
   - Choose action: `e` (encryption) or `d` (decryption)
   - Enter the text you want to encrypt or decrypt
   - Enter the shift step (integer)

---

## Example

### Encrypt English text

Input:
```
Choose a language: en
What to do: Encryption (e) or Decryption (d): e
Enter text: Hello World!
Shift step: 3
```

Output:
```
Khoor Zruog!
```

### Decrypt Russian text

Input:
```
Choose a language: ru
What to do: Encryption (e) or Decryption (d): d
Enter text: Кщкщ
Shift step: 3
```

Output:
```
Зззз
```

---

## How it Works

- `correct_input(prompt, option1, option2)` — ensures that the user selects a valid option from the choices.
- `caesar_cipher(step, text)` — performs the Caesar cipher shift on each letter in the text. Supports both English and Russian alphabets.
- `algorithm(shift_step, text, to_do)` — chooses whether to encrypt or decrypt based on user input.

---

## Notes

- Only **letters** are shifted; numbers, punctuation, and spaces stay the same.
- The shift is **circular**, so letters wrap around at the end of the alphabet.
- Uppercase letters remain uppercase; lowercase letters remain lowercase.

---

## License

This project is free to use, modify, and share.
