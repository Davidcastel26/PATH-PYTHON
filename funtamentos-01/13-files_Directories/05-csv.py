import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre", 'Edad'])
    writer.writerow(["Ricardo", 25])
    writer.writerow(["Fernando", 23])
    
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)