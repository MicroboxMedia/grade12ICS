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
            
def generate_names():
    names = parse_names(r"names.csv")
    name = f'{random.choice(names[0])} {random.choice(names[1])}'
    return name

        
def generate_salary():
    salary = f'${str(random.randint(25000, 125000))}'
    return salary


def generate_people():
    people = []
    for i in range(500):
        id = generate_id()
        name = generate_names()
        occupation = random.choice(parse_occupations(r"occupations.csv"))
        salary = generate_salary()
        person = f'{id}, {name}, {occupation}, {salary}'
        people.append(person)
    return people
        

def write_to_file(filename, people):
    with open(filename, "w") as fileOut:
        writer = csv.writer(fileOut)
        writer.writerow(f'Id Key, Name, Occupation, Salary\n')
        for person in people:
            s = f'{person}\n'
            writer.writerow(s)
    

def main():
    people_list = generate_people()
    write_to_file(r"people.csv", people_list)
    print("Generated File")
    

main()
