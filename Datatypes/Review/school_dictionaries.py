def create_school_dictionary(school_codes, school_names):
    d = {}
    for i in range(len(school_codes)):
        if school_codes[i] not in d:
            d[school_codes[i]] = school_names[i]
        else:
            print("School already in the dictionary")
    return d

print(create_school_dictionary(['aph', 'irs'], ['Abbey Park', 'Iroquois Ridge']))