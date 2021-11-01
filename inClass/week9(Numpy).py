# Classes 
'''

class Dog:
    breed = ""
    coatColor = ""
    barkType = ""
    #We can define defaults#
    def __init__(self, breed="", cc="", bt=""):
        self.coatColor = cc
        self.breed = breed
        self.barkType = bt

    def setCoatColor(self, coat):
        self.coatColor = coat

    def setBreed(self,breed):
        self.breed = breed

    def setBarkType(self,bark):
        self.barkType = bark

    def bark(self):
        print(self.barkType * 3)

d = Dog()
d.breed = "Pomeranian"

'''
##############################################

# import json
# data = '''{
#   "name" : "Chuck",
#   "phone" : {
#     "type" : "intl",
#     "number" : "+1 734 303 4456"
#    },
#    "email" : {
#      "hide" : "yes"
#    }
# }'''

##############################################

# info = json.loads(data)
# print('Name:',info["name"])
# print('Hide:',info["email"]["hide"])
# print('Phone area code:',info["phone"]["number"][3:6])

# import json
# input = '''[
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Jerry"
#   }
# ]'''

# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])

'''
import numpy as np
cvalues = [25.3, 24.8, 26.9, 23.9]  #celsius values                                         
C = np.array(cvalues)
print(C)
fahrenArray = (C * 9/5 + 32)
print('Fahrenheit: ', fahrenArray)
'''

from ctypes import resize
import numpy as np 

sampledata = [['Town', 'Population'], ['MyTown', '500'], ['YourTown', '600'], ['SomeoneElseTown', '800']]

# a = np.array(sampledata)
# print(a)
# print(type(a))
#a = np.array(sampledata, dtype= 'U30, i4')
# removedHeader = sampledata[1:]
# a = np.array(removedHeader)
# print(a)

'''
def convertToTuples(listData):
    convertList = []
    for row in listData:
        newTuple = tuple(row)
        convertList.append(newTuple)
    return convertList

sampledata = [['Town', 'Population'],['MyTown', '500'], ['YourTown', '600'], ['SomeoneElseTown', '800']]

removedHeader = sampledata[1:]
headerRow = sampledata[0:1]

type_spec = np.dtype([(headerRow[0][0],'U30'), (headerRow[0][1], 'i4')])

listConvert = convertToTuples(removedHeader)      #(sampledata[1:])

finalArray = np.array(listConvert, type_spec)

print(finalArray)
print(finalArray['Town'])
print(finalArray['Population'])
'''
'''
import numpy as np
def convertToTuples(listData):
    convertList = []
    for row in listData:
        newTuple = tuple(row)
        convertList.append(newTuple)
    return convertList

dog_info=[]
while True:
    doglist=[input("Insert the information of dog, breed, age, sex: ").split()]
    if doglist[0][0]=="quit":
        break
    print(doglist)
    dog_info.extend(doglist)
    print(dog_info)

headerRow = ["Breed","Age","Sex"]
print(headerRow)
type_spec = np.dtype([(headerRow[0],'U30'), (headerRow[1], 'i4'),(headerRow[2], 'U30')])
listConvert = convertToTuples(dog_info)
print(listConvert)
finalArray = np.array(listConvert, type_spec)
print(finalArray)
print(finalArray['Breed']) 

'''

'''

import numpy as np
x0=np.array([True,True,False])
print(x0)
x0=np.array([[2,0,4],[3,2,7]], np.int32)
print(x0)
x4=np.empty([4,3])
print(x4)
x4=np.empty_like(x0)
print(x4)
x4=np.zeros(4,np.complex64)
print(x4)
x4=np.arange(1,9,2.0)
print(x4)
x4=np.diag([1,2,4])
print(x4)
x4=np.linspace(0,np.pi,10)
print(x4)

'''
'''
import numpy as np
# lst = [2, 3, 4, 6]
# value = 5
# numArr = np.array(lst)
# print(numArr * value)

# a bit easier
# much faster

A = np1 = np.array([[1,2,3], [2,3,4], [1,1,2]])
B = np2 = np.ones((3,3))
print(A + B)
print(A * (B+1))
'''
'''
import numpy as np
np1 = np.array([[1,2,3], [2,3,4], [1,1,2]])
np2 = np.ones((3,3))
print(np1*np2,'\n')
print(np1 * (np2+1),'\n')
print(np.dot(np1,np2),'\n')
print(np.kron(np1,np2),'\n')
print(np.linalg.norm(np2),'\n')
print(np.linalg.cond(np2),'\n')
'''
'''
import numpy as np
temp=[]
for i in range(2):
    matrix_size = input("insert the rows and cols of matrix: ").split()
    temp.append( np.zeros((int(matrix_size[0]), int(matrix_size[1]))))
    for row in range(int(matrix_size[0])):
        for col in range(int(matrix_size[1])):
            print(row)
            temp[i][row][col] = int(input(("insert the %d row and %d col matrix: " % (row, col))))
print(type(temp))
print(type(temp[0]))
try:
    print(np.dot(temp[0],temp[1]))
except:
    print("Matrix size does not match")
print("Matrix equality: ",np.array_equal(temp[0],temp[1])) 
'''
'''
import numpy as np
temp1 = np.array([[1,2,3],[4,5,6]])
print("temp1: ",temp1)
temp2 = temp1.T
print("temp2: ",temp2)
for element in temp1.flat:
    print("flat: ",element)
for row in temp1:
    print("slice: ",row)

for i in range(temp1.shape[0]): 
    for j in range(temp1.shape[1]):
        print(temp1[i][j])
'''
'''
import numpy as np
A = np.arange(8) 
print(A,'\n')
A=A.reshape(2,4)
print(A,'\n')

b = np.array([[0, 1], [2, 3]])
b.resize(2, 3) 
print(b,'\n')

a=np.array([[0,1],[2,3]])
b=np.resize(a,(2,3))
print(b,'\n')

b=np.resize(a,(1,4))
print(b,'\n')

b=np.resize(a,(2,4))
print(b)
'''
import numpy as np
np.random.seed(2) 
x = np.random.randn(50)
print(x)
np.random.seed(2) 
y = 3.5*x+2+np.random.randn(50)*0.3 
print(y)
