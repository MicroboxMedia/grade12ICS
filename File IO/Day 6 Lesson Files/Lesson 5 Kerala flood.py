import csv

def create_kerala_districts(filename):
    
    kerala_flood_info = {}

    with open(filename, "r") as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        
        for line in reader:
            district = line[0]
            fatalities = int(line[1])
            num_camps = int(line[2])
            actual_rainfall = float(line[3])
            normal_rainfall = float(line[4])
            num_landslides = int(line[5])
            damaged_houses = int(line[6])
            warnings = []
            
            kerala_flood_info[district] = {
                "fatalities":fatalities,
                "num_camps":num_camps,
                "actual_rainfall":actual_rainfall,
                "normal_rainfall":normal_rainfall,
                "num_landslides":num_landslides,
                "damaged_houses":damaged_houses,
                "warnings":warnings
            }
            
    return kerala_flood_info
        


def add_kerala_flood_warnings(filename, kerala_flood_info):

    with open(filename, "r") as file_in:
        file_in.readline()
        reader = csv.reader(file_in)
        for line in reader:
            district = line[0]
            date = line[1]
            actual = line[2]
            predicted = line[3]
            data = [date, actual, predicted]
            kerala_flood_info[district]["warnings"] += [data]
        




def print_kerala_flood_info(kerala_flood_info):
    for key in (kerala_flood_info):
        print(key)
        print(kerala_flood_info[key])



def main():
    

      flood_dict = create_kerala_districts(r"district_wise_details.csv")
      add_kerala_flood_warnings(r"warnings_actual_predicted.csv", flood_dict)

      print_kerala_flood_info(flood_dict)

main()
        
