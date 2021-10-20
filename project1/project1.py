import csv


def open_file(fname):
    # read the csv file
    with open(fname, 'r') as csv_file:
        # create a csv reader
        csv_reader = csv.reader(csv_file)
        # extract field names 
        field_names = next(csv_reader)
        # get data row by row 
        for row in csv_reader:
            rows.append(row)
        return field_names, rows


def name_avg(first_avg=0, last_avg=0, row_len=0):
    for row in rows:
        first_avg += len(row[1])
        last_avg += len(row[2])
        row_len += 1
    first_avg = int(first_avg / row_len)
    last_avg = int(last_avg / row_len)
    print('Average first name length: {0}\nAverage last name length: {1}\n'.format(first_avg, last_avg))


rows = []
open_file(input('Enter file name: '))
print('Test Site Report: ')
name_avg()
