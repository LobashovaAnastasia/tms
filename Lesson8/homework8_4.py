import json
import csv

with open(
    "json_file.json",
    mode="r"
) as file:
    data = json.loads(file.read())  # Правильно: data = json.load(file) !!!

with open("csv_file.csv", mode="w") as file:
    writer = csv.writer(file)
    writer.writerow(('id', 'name', 'age', 'phone'))

for user in data:
    id_ = user
    name = data[user][0]
    age = data[user][1]
    with open("csv_file.csv", mode="a") as file:
        writer = csv.writer(file)
        writer.writerow((id_, name, age))
