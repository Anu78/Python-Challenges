import csv
import bokeh
from pprint import pprint
ages,races,sex = []

with open("overdoses.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ages.append(row["Age"])
        races.append(row['Race'])
        sex.append(row['Sex'])

ages[:] = (value for value in ages if value != "")
races[:] = (value for value in races if value != "")
sex[:] = (value for value in sex if value != "")

ages = list(map(int,ages))

dataDictionary = {
    "Average Age: ": round(sum(ages)/int(len(ages))),
    "Males: ": sex.count("Male"),
    "Females: ": sex.count("Female"),
    "White: ": races.count("White"),
    "Black: ": races.count("Black"),
    "Other: ": len(races) - races.count("White") - races.count("Black"),
}

pprint(dataDictionary)