import random
import csv


def generate_id():
    id = ""
    for _ in range(3):
        id_digit = str(random.randint(0,9))
        id += str(id_digit)
    id += "-"
    for _ in range(2):
        id_digit = str(random.randint(0,9))
        id += id_digit
    id += "-"
    for _ in range(4):
        id_digit = str(random.randint(0,9))
        id += id_digit
        
    return id


def parse_names(filename):
    first_names = []
    last_names = []
    with open(filename, "r") as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)
        
        for line in reader:
            first_names.append(line[0])
            last_names.append(line[1])
    return first_names, last_names
            

def parse_occupations(filename):
    occupations = []
    with open(filename, "r") as fileIn:
        fileIn.readline()
        reader = csv.reader(fileIn)
        
        for line in reader:
            occupations.append(line[0])

    return occupations
            
def generate_names(first_names_list, last_names_list):
    name = f'{random.choice(first_names_list)} {random.choice(last_names_list)}'
    return name


def generate_people():
    people = []
    for i in range(500):
        id = generate_id()
        name = generate_names(parse_names(r"names.csv")[0], parse_names(r"names.csv")[1])
        occupation = random.choice(parse_occupations(r"occupations.csv"))
        salary = generate_salary()
        person = f'{id}, {name}, {occupation}, {salary}'
        people.append(person)
    return people
        
        
        
def generate_salary():
    salary = f'${str(random.randint(25000, 125000))}"'
    return salary


def write_to_file(filename, people):
    with open(filename, "w") as fileOut:
        fileOut.write(f'Id Key, Name, Occupation, Salary\n')
        for person in people:
            s = f'{person}\n'
            fileOut.write(s)
    
def main():
    people_list = generate_people()
    write_to_file(r"people.csv", people_list)
    

main()
print("Generated File")