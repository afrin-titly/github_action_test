import sys
import csv
import os

start_time = sys.argv[1]
end_time = sys.argv[2]

print("Hello World!!")
print("Start time: " + start_time)
print("End time: " + end_time)

path = "csv"
isExist = os.path.exists("csv")
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(path)
   print("The new directory is created!")

with open('./csv/profiles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]

    writer.writerow(field)
    writer.writerow(["Oladele Damilola", "40", "Nigeria"])
    writer.writerow(["Alina Hricko", "23", "Ukraine"])
    writer.writerow(["Isabel Walter", "50", "United Kingdom"])
