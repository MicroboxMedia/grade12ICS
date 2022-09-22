def sort_emails(filename):
    yahoo = []
    hotmail = []
    gmail = []
    hdsb = []
    fake = []

    with open(filename) as fileIn:
        for line in fileIn:
            line = line.strip().split("@")
            temp_string = f"{line[0]}@{line[1]}"
            if line[1] == "yahoo.com":
                yahoo.append(temp_string)
            elif line[1] == "hotmail.com":
                hotmail.append(temp_string)
            elif line[1] == "gmail.com":
                gmail.append(temp_string)
            elif line[1] == "hdsb.ca":
                hdsb.append(temp_string)
            else:
                fake.append(temp_string)

    return fake
print(sort_emails("emailAddresses.txt"))