months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10,
          "NOV": 11, "DEC": 12}


def split_date(string):
    date_list = string.split("-")
    return "19", str(date_list[2]), ", ", str(months[date_list[1]]), ", ", str(date_list[0])


print("".join(split_date("8-MAR-85")))
print("yyyy,mm,dd")
