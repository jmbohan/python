import csv

filename = input("Enter a pilot data file name: ")
data = []

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    fieldNames = csv_reader.__next__()

    for row in csv_reader:
        data.append(row)

# Get average first and last name length
avgFirst = 0
avgLast = 0
rowLen = 0
for row in data:
    avgFirst += len(row[1])
    avgLast += len(row[2])
    rowLen += 1
avgFirst = int(avgFirst / rowLen)
avgLast = int(avgLast / rowLen)
print(avgFirst, avgLast)
# get the average test score
avgFieldOne = 0
avgFieldTwo = 0
avgFieldThree = 0
for row in data:
    avgFieldOne += int(row[6])
    avgFieldTwo += int(row[7])
    avgFieldThree += int(row[8])
avgFieldOne = int(avgFieldOne / rowLen)
avgFieldTwo = int(avgFieldTwo / rowLen)
avgFieldThree = int(avgFieldThree / rowLen)
print(avgFieldOne, avgFieldTwo, avgFieldThree)

# get the best pilot
bestId = 0
bestFieldTestSum = 0
tempFieldTestSum = 0
for row in data:
    tempFieldTestSum = int(row[6]) + int(row[7]) + int(row[8])
if tempFieldTestSum > bestFieldTestSum:
    bestFieldTestSum = tempFieldTestSum
bestId = int(row[0]) - 1
bestPilot = dict()
bestPilot["FirstName"] = data[bestId][1]
bestPilot["LastName"] = data[bestId][2]
bestPilot["serialRS"] = data[bestId][4]
bestPilot["Color"] = data[bestId][5]
bestPilot["AvgScore"] = str(int(bestFieldTestSum / 3))
# printing the data to the Console Now
# Printing average First name length and Last Name length
print("Average first name length: %d" % avgFirst)
print("Average Last name length: %d" % avgLast)
# Printing the three Field Test Scores' average
print("Average field test 1 Score: %d" % avgFieldOne)
print("Average field test 2 Score: %d" % avgFieldTwo)
print("Average field test 3 Score: %d" % avgFieldThree)
# printing the best pilot data
print(bestPilot["FirstName"] + " " + bestPilot["LastName"] + ",serial RS: " + bestPilot["serialRS"] + "," + bestPilot[
    "Color"] + ", with an average field Test Score of " + bestPilot["AvgScore"])
# Getting Color Histograms, color histogram is represented by a dict
colorHistogram = dict()

for row in data:
    # row[5] represents the color
    if row[5] in colorHistogram:
        colorHistogram[row[5]] += 1
    else:
        colorHistogram[row[5]] = 1

# printing the colors Histogram
for color in colorHistogram:
    print(color + " : " + str(colorHistogram[color]) + ",")
