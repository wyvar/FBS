import os.path
import csv

dir_data="collected_data/"
field_names=['date','start', 'end']


def create_file(name):
    file_name = name + '.csv'
    print(file_name)
    with open(dir_data + file_name, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)
        csv_writer.writeheader()

def add_to_file(file_name, dict_con):
    file_name = file_name + '.csv'
    with open(dir_data + file_name,"a") as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=field_names)
        csv_writer.writerow(dict_con)

def readfile(name):
    file_name = name + ".csv"
    data =[{}]
    with open(dir_data + file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
        for row in csv_reader:
            data.append(row)
        
        csv_file.close()
    return data
    