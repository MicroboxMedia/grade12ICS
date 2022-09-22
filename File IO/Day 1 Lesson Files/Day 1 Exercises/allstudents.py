def sort_students(filename):
    grade_nine = []
    grade_ten = []
    grade_eleven = []
    grade_twelve = []

    with open(filename) as fileIn:
        
        for line in fileIn:
            line = line.strip().split()

            temp_entry = [line[1].capitalize()]
            temp_entry.append(line[2].capitalize())
            if line[0] == '09':
                grade_nine.append(temp_entry)
            elif line[0] == '10':
                grade_ten.append(temp_entry)
            elif line[0] == '11':
                grade_eleven.append(temp_entry)
            else:
                grade_twelve.append(temp_entry)
    return grade_nine, grade_ten, grade_eleven, grade_twelve

grade_9, grade_10, grade_11, grade_12 = sort_students("allStudents.txt")[0], sort_students("allStudents.txt")[1], sort_students("allStudents.txt")[2], sort_students("allStudents.txt")[3]

print(len(grade_9))
print(len(grade_10))
print(len(grade_11))
print(len(grade_12))
