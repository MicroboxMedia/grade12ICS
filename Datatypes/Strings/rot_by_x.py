def rotate_word(string, num):
    new = ""
    string = string.lower()
    for char in string:
        if ord(char) + num > 122:
            new += chr(96 + ord(char) + num - 122)
        elif ord(char) + num < 97:
            new += chr(123 - (97 - (ord(char) + num)))
        else:
            new += chr(ord(char) + num)
    return new


print(rotate_word(input("Input a word to rotate"), int(input("Input an integer to rotate by"))))
    