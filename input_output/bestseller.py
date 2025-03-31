from csv import reader,writer
try:
    file_path = "/home/taku/Desktop/stuff/python_prac/input_output/Bestseller.csv"
    file = open(file_path,'r')
    csv_reader= reader(file)
    for row in csv_reader:
        print(row)
finally:
    file.close()


try:
    csv_writer = writer('bestseller_info.csv', 'w')
    csv_writer.writerow(['hi','nice','to','meet','you'])
finally:
    file.close()
