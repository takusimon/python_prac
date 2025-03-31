import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    file = open('packing_list.csv',"r")
    csv_reader = csv.reader(file)
    for item in csv_reader:
        print(item)
except FileNotFoundError:
    print("Packing list file not found. Creating a new one.")
    file = open("packing_list.csv","w",newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)