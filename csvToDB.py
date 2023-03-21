import csv

import json

csvreader = csv.reader(open('dataset.csv'))

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December', 'Average']
years = [str(2000+x) for x in range(6,21)]
dict1 = {}

sectors = []
for row in csvreader:
    data = [float(x) for x in row[1:]]
    sectors.append(row[0])
    dict1[row[0]] = {}
    for j,y in enumerate(years):
        dict1[row[0]][y] = data[j*13:(j*13)+13]
        
# Serializing json
json_object = json.dumps(dict1, indent=4)
 
# Writing to sample.json
with open("dataset.json", "w") as outfile:
    outfile.write(json_object)