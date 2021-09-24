# pickling 
'''
import pickle
dogs_dict = {'Ozzy' : 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barko': 12, 'Balou': 9, 'Laika': 16}
filename = 'dogs'
outfile = open(filename, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()
'''
# unpickling 
import pickle

filename = 'dogs'
infile = open(filename, 'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(type(new_dict))