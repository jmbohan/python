import csv

fhand = input('Enter file name: ')
pilot_names = []
data = []
with open(fhand, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        data.append(row)
avg_first = 0
avg_last = 0
row_len = 0
for row in reader:
    avg_first += len(row[1])
    avg_last += len(row[2])
    row_len += 1
avg_test1 = 0
avg_test2 = 0
avg_test3 = 0
print(reader)
# for row in reader:
#     avg_test1 += int(row[6])
#     avg_test2 += int(row[7])
#     avg_test3 += int(row[8])
# avg_test1 = int(avg_test1 / row_len)
# avg_test2 = int(avg_test2 / row_len)
# avg_test3 = int(avg_test3 / row_len)
# colors = dict()
# for row in reader:
#     if row[5] in colors:
#         colors[row[5]] += 1
#     else:
#         colors[row[5]] = 1
# pilot_id = 0
# highest_test = 0
# best_pilot = dict()
# for row in reader:
#     test_sum = int(row[6]) + int(row[7]) + int(row[8])
#     if test_sum > highest_test:
#         highest_test = test_sum
#         pilot_id = int(row[0]) - 1
#         best_pilot['First Name'] = reader[pilot_id[1]]
#         best_pilot['Last Name'] = reader[pilot_id[2]]
#         best_pilot['Robot Serial'] = reader[pilot_id[4]]
#         best_pilot['Color'] = reader[pilot_id[5]]
#         best_pilot['Average Score'] = str(int(highest_test / 3))
# print("Average first name length: %d" % avg_first)
# print("Average Last name length: %d" % avg_last)
# print("Average field test 1 Score: %d" % avg_first)
# print("Average field test 2 Score: %d" % avg_test2)
# print("Average field test 3 Score: %d" % avg_test3)
#
# print(best_pilot["FirstName"] + " " + best_pilot["LastName"] +
#       ",Robot Serial" + best_pilot["Robot Serial"] + "," + best_pilot["Color"] +
#       ", with an average field Test Score of " + best_pilot["AvgScore"])
#
# for color in colors:
#     print(color + " : " + str(colors[color]) + ",")
reader.close