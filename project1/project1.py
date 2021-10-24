import csv
from pprint import pformat


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


def name_avg() -> str:
    first_avg = 0
    last_avg = 0
    row_len = 0
    for row in rows:
        first_avg += len(row[1])
        last_avg += len(row[2])
        row_len += 1
    first_avg = int(first_avg / row_len)
    last_avg = int(last_avg / row_len)
    print('Average first name length: {0}\nAverage last name length: {1}'.format(first_avg, last_avg))
    name = str('Average first name length: {0}\nAverage last name length: {1}'.format(first_avg, last_avg))
    with open('Pilots1_report.txt', 'a') as o:
        o.write('Average first name length: {0}\nAverage last name length: {1}\n'.format(first_avg, last_avg))


def test_avg(test_one=0, test_two=0, test_three=0, row_len=0):
    for row in rows:
        test_one += int(row[6])
        test_two += int(row[7])
        test_three += int(row[8])
        row_len += 1
    test_one = int(test_one / row_len)
    test_two = int(test_two / row_len)
    test_three = int(test_three / row_len)
    print(
        'Average field test one score: {}\nAverage field test two score: '
        '{}\nAverage field test three score: {}\n'.format(
            test_one, test_two, test_three))
    with open('Pilots1_report.txt', 'a') as o:
        o.write(
            'Average field test one score: {}\nAverage field test two score: '
            '{}\nAverage field test three score: {}\n'.format(
                test_one, test_two, test_three))


def best_pilot():
    # get the best pilot
    best_id = 0
    highest_test = 0
    test_sum = 0
    for row in rows:
        test_sum = int(row[6]) + int(row[7]) + int(row[8])
        if test_sum > highest_test:
            highest_test = test_sum
            best_id = int(row[0]) - 1
    best_pilot = dict()
    best_pilot["FirstName"] = rows[best_id][1]
    best_pilot["LastName"] = rows[best_id][2]
    best_pilot["serialRS"] = rows[best_id][4]
    best_pilot["Color"] = rows[best_id][5]
    best_pilot["AvgScore"] = str(int(highest_test / 3))

    print("\nBest pilot data: \n" + best_pilot["FirstName"] + " " + best_pilot["LastName"] + ", "
          + best_pilot["serialRS"] + ", " + best_pilot["Color"] + ", With an average field test score of "
          + best_pilot["AvgScore"])
    with open('Pilots1_report.txt', 'a') as o:
        o.write("\nBest pilot data: \n" + best_pilot["FirstName"] + " " + best_pilot["LastName"] + ", "
                + best_pilot["serialRS"] + ", " + best_pilot["Color"] + ", With an average field test score of "
                + best_pilot["AvgScore"])


def get_color():
    for row in rows:
        # row[5] represents the color
        if row[5] in color:
            color[row[5]] += 1
        else:
            color[row[5]] = 1
    return color


rows = []
color = dict()
name_str = ''
open_file(input('Enter file name: '))
print('\nTest Site Report: ')
with open('Pilots1_report.txt', 'a') as o:
    o.write("Test Site Report: \n")
    o.close()
name_avg()
test_avg()
best_pilot()
get_color()
color_sorted = (sorted(color.items()))
print(pformat(color_sorted))
with open('Pilots1_report.txt', 'a') as o:
     o.write("\n" + pformat(color_sorted))
