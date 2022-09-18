def generate_rot_alphabet():
    mappedLetters = {chr(i): chr(i + 13) for i in range(97, 110)}
    for i in range(110, 123):
        mappedLetters[chr(i)] = chr(i - 13)

    return mappedLetters


def encrypt_string(string, letterMap):
    return "".join(letterMap[char] for char in string)


letterMap = generate_rot_alphabet()
print(encrypt_string(input("Input a string : "), letterMap))

