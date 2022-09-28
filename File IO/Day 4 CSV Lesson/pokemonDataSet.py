import csv


def sort_pokemon_type(filename):
    pokemon_dictionary = {}
    
    with open(filename) as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)
        for line in reader:
            pokemon_entry = [line[1], line[2], line[3], int(line[4]), int(line[5]), int(line[6]), int(line[7]), int(line[8]), int(line[9]), int(line[10]), int(line[11]), bool(line[12])]
            if line[2] not in pokemon_dictionary:
                pokemon_dictionary[line[2]] = []
            if line[3] not in pokemon_dictionary:
                if line[3] != "":
                    pokemon_dictionary[line[3]] = []
            
            pokemon_dictionary[line[2]].append(pokemon_entry)
            if line[3] != "":
                pokemon_dictionary[line[3]].append(pokemon_entry)
    return pokemon_dictionary
pokemon_dictionary = sort_pokemon_type(r"Pokemon.csv")
print(pokemon_dictionary)