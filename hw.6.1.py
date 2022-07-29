import json, csv

# data = None

with open("jsonfile.json", "r") as jfile:
    data = json.load(jfile)
print(data)

with open("new_data.csv", "w") as csv_file:
    # writer = csv.DictWriter(csv_file, fieldnames = [key for key in data[0].keys()])
    # writer.writerow(key for key in data[0].keys())
    writer = csv.writer(csv_file)
    writer.writerow(key for key in data[0].keys()) # получаем ключи по словарю и записываем отдельной строкой
    # writer.writerow(value for value in data[0].values())  # достаем из словаря по первому пользователю

    for item in data:
        writer.writerow(value for value in item.values())