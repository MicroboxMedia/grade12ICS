def contracrostipunctus(filename):
    contracrostipunctus_string = ""
    with open(filename) as fileIn:
        for line in fileIn:
            line = line.strip().split(":")
            contracrostipunctus_string += line[1][1]
    return contracrostipunctus_string
            
print(contracrostipunctus("contracrostipunctus.txt"))