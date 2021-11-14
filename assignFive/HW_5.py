import numpy as np
import csv
import matplotlib.pyplot as plt

def animal_count(animal_name):
    animal_count = 0
    for element in finalArray['Animal'] == animal_name:
        if element == True:
            animal_count = animal_count +1
    return animal_count

def convert_to_tuples(list_data):
    convert_list = []
    for row in list_data:
        new_tuple = tuple(row)
        convert_list.append(new_tuple)
    return convert_list


with open('Hidden_Island.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=','))
removedHeader = data[1:]
headerRow = data[0:1]

type_spec = np.dtype([(headerRow[0][0], "U30"), (headerRow[0][1], "i4"), (headerRow[0][2], "i4")])
listConvert = convert_to_tuples(removedHeader)
finalArray = np.array(listConvert, type_spec)
animal = finalArray['Animal']
range_number = finalArray['Range']
u_ind = finalArray['Unique Individuals']
puffin_count = 0 
finalArray = finalArray.reshape(600,1)

puffin_count = animal_count('Purple Puffin')
wombat_count = animal_count('Wisteria Wombat')
pomeranian_count = animal_count('Pumpkin Pomeranian')
bichon_count = animal_count('Burgundy Bichon Frise')

puffin = np.where(animal == 'Purple Puffin')
wombat = np.where(animal == 'Wisteria Wombat')
pomeranian = np.where(animal == 'Pumpkin Pomeranian')
bichon = np.where(animal == 'Burgundy Bichon Frise')
r_one = np.where(range_number == 1)
r_one_count = np.count_nonzero(r_one)
r_two = np.where(range_number == 2)
r_two_count = np.count_nonzero(r_two)
r_three = np.where(range_number == 3)
r_three_count = np.count_nonzero(r_three)

animal_tot = np.count_nonzero(animal)

temp1 = np.array(list(zip(animal, range_number)))
data2 = finalArray[['Animal','Range']]

puffin_tot = np.count_nonzero(puffin)
#print('\nPuffin Total: ', puffin_tot)
puffin_r_1 = np.where((animal == 'Purple Puffin') & (range_number == 1))

puffin_r_1_count = np.count_nonzero(puffin_r_1) 
#print('Puffin Range 1 total: ', puffin_r_1_count)
puffin_r_1_mean = r_one_count/puffin_r_1_count
#print('Puffin Range 1 mean: ', puffin_r_1_mean)    

puffin_r_2 = np.where((animal == 'Purple Puffin') & (range_number == 2))
puffin_r_2_count = np.count_nonzero(puffin_r_2) 
#print('Puffin Range 2 total: ', puffin_r_2_count)
puffin_r_2_mean = r_two_count/puffin_r_2_count
#print('Puffin Range 2 mean: ', puffin_r_2_mean)

puffin_r_3 = np.where((animal == 'Purple Puffin') & (range_number == 3))
puffin_r_3_count = np.count_nonzero(puffin_r_3) 
#print('Puffin Range 3 total: ', puffin_r_3_count)
puffin_r_3_mean = r_three_count/puffin_r_3_count
#print('Puffin Range 3 mean: ', puffin_r_3_mean)
#print('Puffin Mean: ', animal_tot/puffin_tot)
#print(puffin_r_1_mean)
#print(puffin_r_2_mean)
#print(puffin_r_3_mean)

wombat_tot = np.count_nonzero(wombat)
#print('\nWombat Total: ', wombat_tot)
wombat_r_1 = np.where((animal == 'Wisteria Wombat') & (range_number == 1))
wombat_r_1_count = np.count_nonzero(wombat_r_1) 
#print('Wombat Range 1 total: ', wombat_r_1_count)
wombat_r_1_mean = r_one_count/wombat_r_1_count
#print('Wombat Range 1 mean: ', wombat_r_1_mean)

wombat_r_2 = np.where((animal == 'Wisteria Wombat') & (range_number == 2))
wombat_r_2_count = np.count_nonzero(wombat_r_2) 
#print('Wombat Range 2 total: ', wombat_r_2_count)
wombat_r_2_mean = r_two_count/wombat_r_2_count
#print('Wombat Range 2 mean: ', wombat_r_2_mean)

wombat_r_3 = np.where((animal == 'Wisteria Wombat') & (range_number == 3))
wombat_r_3_count = np.count_nonzero(wombat_r_3) 
#print('Wombat Range 3 total: ', wombat_r_3_count)
wombat_r_3_mean = r_three_count/wombat_r_3_count
#print('Wombat Range 3 mean: ', wombat_r_3_mean)
#print('Wombat Mean: ', animal_tot/wombat_tot)
#print(wombat_r_1_mean)
#print(wombat_r_2_mean)
#print(wombat_r_3_mean)

pomeranian_tot = np.count_nonzero(pomeranian)
#print('\nPomeranian Total: ',pomeranian_tot)
pomeranian_r_1 = np.where((animal == 'Pumpkin Pomeranian') & (range_number == 1))
pomeranian_r_1_count = np.count_nonzero(pomeranian_r_1) 
pomeranian_r_1_mean = r_one_count/pomeranian_r_1_count
#print('Pomeranian Range 1 total: ', pomeranian_r_1_count)
#print('Pomeranian Range 1 mean: ', pomeranian_r_1_mean)

pomeranian_r_2 = np.where((animal == 'Pumpkin Pomeranian') & (range_number == 2))
pomeranian_r_2_count = np.count_nonzero(pomeranian_r_2) 
#print('Pomeranian Range 2 total: ', pomeranian_r_2_count)
pomeranian_r_2_mean = r_two_count/pomeranian_r_2_count
#print('Pomeranian Range 2 mean: ', pomeranian_r_2_mean)

pomeranian_r_3 = np.where((animal == 'Pumpkin Pomeranian') & (range_number == 3))
pomeranian_r_3_count = np.count_nonzero(pomeranian_r_3) 
#print('Pomeranian Range 3 total: ', pomeranian_r_3_count)
pomeranian_r_3_mean = r_three_count/pomeranian_r_3_count
#print('Pomeranian Range 3 mean: ', pomeranian_r_3_mean)
#print('Pomeranian Mean: ', animal_tot/pomeranian_tot)

#print(pomeranian_r_1_mean)
#print(pomeranian_r_2_mean)
#print(pomeranian_r_3_mean)

bichon_tot = np.count_nonzero(bichon)
#print('\nBichon Total: ',bichon_tot)
bichon_r_1 = np.where((animal == 'Burgundy Bichon Frise') & (range_number == 1))
bichon_r_1_count = np.count_nonzero(bichon_r_1) 
#print('Bichon Range 1 total: ', bichon_r_1_count)
bichon_r_1_mean = r_one_count/bichon_r_1_count
#print('Bichon Range 1 mean: ', bichon_r_1_mean)

bichon_r_2 = np.where((animal == 'Burgundy Bichon Frise') & (range_number == 2))
bichon_r_2_count = np.count_nonzero(bichon_r_2) 
#print('Bichon Range 2 total: ', bichon_r_2_count)
bichon_r_2_mean = r_two_count/bichon_r_2_count
#print('Bichon Range 2 mean: ', bichon_r_2_mean)

bichon_r_3 = np.where((animal == 'Burgundy Bichon Frise') & (range_number == 3))
bichon_r_3_count = np.count_nonzero(bichon_r_3) 
#print('Bichon Range 3 total: ', bichon_r_3_count)
bichon_r_3_mean = r_three_count/bichon_r_3_count
#print('Bichon Range 3 mean: ', bichon_r_3_mean)
#print('Bichon Mean: ', animal_tot/bichon_tot)
#print(bichon_r_1_mean)
#print(bichon_r_2_mean)
#print(bichon_r_3_mean)


print('\nPurple Puffin Means: \nRange 1: {0}' '\nRange 2: {1}''\nRange 3: {2} '.format(puffin_r_1_mean,puffin_r_2_mean,puffin_r_3_mean))
print('\nWisteria Wombat Means: \nRange 1: {0}' '\nRange 2: {1}''\nRange 3: {2} '.format(wombat_r_1_mean,wombat_r_2_mean,wombat_r_3_mean))
print('\nPumpkin Pomeranian Means: \nRange 1: {0}' '\nRange 2: {1}''\nRange 3: {2} '.format(pomeranian_r_1_mean,pomeranian_r_2_mean,pomeranian_r_3_mean))
print('\nBurgundy Bichon Frise Means: \nRange 1: {0}' '\nRange 2: {1}''\nRange 3: {2} '.format(bichon_r_1_mean,bichon_r_2_mean,bichon_r_3_mean))
print('\nHighest Population:     Range 1: Pomeranian w/ {0}' '\n\t\t\tRange 2: Bichon w/ {1}' '\n\t\t\tRange 3: Pomeranian w/ {2}'.format(pomeranian_r_1_count,bichon_r_2_count,pomeranian_r_3_count))
print('\nLowest Population:      Range 1: Wombat w/ {0}' '\n\t\t\tRange 2: Puffin w/ {1}' '\n\t\t\tRange 3: Puffin w/ {2}'.format(wombat_r_1_count,puffin_r_2_count,puffin_r_3_count))
print('\nPuffin Mean: {0}' '\nWombat Mean: {1}' '\nPomeranian Mean: {2}' '\nBichon Mean: {3}'.format(animal_tot/puffin_tot, animal_tot/wombat_tot, animal_tot/pomeranian_tot, animal_tot/bichon_tot))
print('\nPuffin Standard Deviation: {}'.format(np.std(animal=='Purple Puffin')))
print('Wisteria Wombat Deviation: {}'.format(np.std(animal=='Wisteria Wombat')))
print('Pumpkin Pomeranian Deviation: {}'.format(np.std(animal=='Pumpkin Pomeranian')))
print('Burgundy Bichon Frise Deviation: {}'.format(np.std(animal=='Burgundy Bichon Frise')))

###################################################
labels = ['Region 1', 'Region 2', 'Region 3']
puffin_means = [puffin_r_1_mean, puffin_r_2_mean, puffin_r_3_mean]
wombat_means = [wombat_r_1_mean, wombat_r_2_mean, wombat_r_3_mean]
pomeranian_means = [pomeranian_r_1_mean, pomeranian_r_2_mean, pomeranian_r_3_mean]
bichon_means = [bichon_r_1_mean, bichon_r_2_mean, bichon_r_3_mean ]
x = np.arange(len(labels)) # the label locations
width = 0.2 # the width of the bars
fig , ax = plt.subplots()
rects1 = ax.bar(x - width*1.5, puffin_means  , width, label='Purple Puffin', color="purple",edgecolor="black")
rects2 = ax.bar(x - width*.5, wombat_means, width, label='Wisteria Wombat',color="pink",edgecolor="black")
rects2 = ax.bar(x + width*.5, pomeranian_means, width, label='Pumpkin Pomeranian',color="orange",edgecolor="black")
rects2 = ax.bar(x + width*1.5, bichon_means, width, label='Burgundy Bichon Frise',color="maroon",edgecolor="black")
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Species Count')
ax.set_title('Hidden Island')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
#plt.show()
plt.savefig('Hidden_Island_Means.png')
plt.show()