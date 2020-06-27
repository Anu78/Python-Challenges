import csv

with open("SampleData.csv") as f:
    rows = csv.DictReader(f)
    rows = [row for row in rows]

sums = {
    "East": 0,
    "West": 0,
    "Central": 0,
}

for row in rows:
    sums[row['Region']] += int(row['Units'])
print(sums)