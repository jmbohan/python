'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace (0, 10, 1000)
y = np. power(x, 2)
plt.plot (x, y)
plt.show()
plt.savefig('plot.png')
'''
'''
import matplotlib.pyplot as plt
plt.plot([-1, -4.5, 16, 23], "ob")

plt.show()
plt.savefig('plot.png')
'''
'''
import matplotlib.pyplot as plt
days = [5,10,15,20]
celcius_values = [24, 16, 16, 23]
plt.plot(days, celcius_values, "ob")
plt.xlabel('Day')
plt.ylabel('Degrees Celsius')
plt.show()
plt.savefig('plot3.png')
'''
'''
import matplotlib.pyplot as plt
days = list(range(1,9))
celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
plt.xlabel('Day')
plt.ylabel('Degrees Celsius')
plt.plot(days, celsius_min,
         days, celsius_min, "oy",
         days, celsius_max, 
         days, celsius_max, "or")
print("The current limits for the axes are:")        
print(plt.axis())
print("We set the axes to the following values:")
xmin, xmax, ymin, ymax = 0, 10, 14, 45
print(xmin, xmax, ymin, ymax)
plt.axis([xmin, xmax, ymin, ymax])
plt.show()
plt.savefig('maxAndMin.png')
'''
'''
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)
F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
starty, endy = -3.1, 3.1
plt.axis([startx, endx, starty, endy])
plt.plot(X,F1)
plt.plot(X,F2)
plt.plot(X,F3)
plt.plot(X, F1, 'ro')
plt.plot(X, F2, 'bx')
plt.show()
plt.savefig("plot5.png")
'''
'''
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
F1 = 3 * np.sin(X)
F2 = np.sin(2*X)
F3 = 0.3 * np.sin(X)
F4 = np.cos(X)
plt.plot(X, F1, color="blue", linewidth=2.5, linestyle="-")
plt.fill_between(X,0,F1, color='blue', alpha=.1)
plt.plot(X, F2, color="red", linewidth=1.5, linestyle="--")
plt.plot(X, F3, color="green", linewidth=2, linestyle=":")
plt.plot(X, F4, color="grey", linewidth=2, linestyle="-.")
plt.show()
plt.savefig('plot6.png')
'''
# subplots 

'''
import numpy as np
import matplotlib.pyplot as plt

for i in range(1,7):
    plt.subplot(2,3,i)
    plt.text(0.5, 0.5, str((2, 3, i)),
    fontsize =18, ha= 'center')
plt.show()
plt.savefig('plot7.png')
'''
'''
import numpy as np
import matplotlib.pyplot as plt
numerical_data = np.array([1,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,5,4,6,7,8])
plt.hist(numerical_data)
plt.title("Numbergram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
plt.savefig('plot8.png')
'''
'''
import numpy as np
import matplotlib.pyplot as plt

num_data_2 = np.array([-1,-5,-2,-10,-11 ,0,0,0,0,0, 1,2,3,4,5,6,7,8,9])
plt.hist(num_data_2, bins=100,color="#875F9A")
plt.title("Number Bins")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
plt.savefig('plot9.png')
'''
'''
import matplotlib.pyplot as plt
import numpy as np
mu, sigma = 0, 0.1 # mean and standard deviation
gaussian_numbers = np.random.normal(mu, sigma, 10000)
plt.hist(gaussian_numbers, bins=100)
plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
plt.savefig("plot10.png")
'''
'''
import matplotlib.pyplot as plt
fig =plt.figure(figsize=(6,4))
fig.subplots_adjust(bottom=0.025, left=0.025, top = 0.975, right=0.975)
X = [ (3,3,(1,3)), (3,3,(4,5)), (3,3,(6,9)), (3,3,7),(3,3,8) ]
for nrows, ncols, plot_number in X:
    sub = plt.subplot(nrows, ncols, plot_number)
    sub.set_xticks([])
    sub.set_yticks([])
plt.show()
plt.savefig('plot11.png')
'''
'''
import matplotlib.pyplot as plt
import numpy as np
X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)
mylist1 = 3 * np.sin(X)
mylist2 = np.sin(2*X)
mylist3 = 0.3 * np.sin(X)
mylist4 = 3 * np.cos(X)
mylist5 = np.tan(2*X)
mylist6 = 0.3 * np.cos(X)

mylist=[mylist1, mylist2,mylist3,mylist4, mylist5,mylist6]
mycol=['r','b','y','k','c','m']
fig = plt.figure(figsize=(6, 4))
fig.subplots_adjust(bottom=0.025, left=0.025, top=0.975, right=0.975)

Y = [(3, 3, (1, 3)), (3, 3, (4, 5)), (3, 3, (6, 9)), (3, 3, 7), (3, 3, 8)]
i=0
for nrows, ncols, plot_number in Y:
    sub = plt.subplot(nrows, ncols, plot_number)
    sub.set_xticks([])
    sub.set_yticks([])
    plt.plot(mylist[i],mycol[i])
    i+=1
plt.show()
plt.savefig('plot12.png')
'''
'''
names = ['group_a', 'group_b', 'group_c'] 
values = [1, 10, 100] 

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(9, 3)) 
plt.subplot(131) 
plt.bar(names, values) 
plt.subplot(132) 
plt.scatter(names, values) 
plt.subplot(133) 
plt.plot(names, values) 
plt.suptitle('Categorical Plotting') 
plt.show() 
plt.savefig('plot13.png')
'''
'''
import matplotlib.pyplot as plt
import numpy as np

def f(t): 
    return np.exp(-t) * np.cos(2*np.pi*t) 

t1 = np.arange(0.0, 5.0, 0.1) 
t2 = np.arange(0.0, 5.0, 0.02) 
plt.figure()    #optional
plt.subplot(211) 
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k') 
plt.subplot(212) 
plt.plot(t2, np.cos(2*np.pi*t2), 'r--') 
plt.show() 
plt.savefig('plot14.png')
'''
'''
import matplotlib.pyplot as plt
import numpy as np
labels = ['G1', 'G2', 'G3', 'G4', 'G5']
USA_means = [20, 34, 30, 35, 27]
Russia_means = [25, 32, 34, 20, 25]
China_means = [25, 32, 34, 20, 25]
x = np.arange(len(labels)) # the label locations
width = 0.25 # the width of the bars
fig , ax = plt.subplots()
rects1 = ax.bar(x - width, USA_means, width, label='USA', color="blue",edgecolor="black")
rects2 = ax.bar(x , Russia_means, width, label='Russia',color="green",edgecolor="black")
rects2 = ax.bar(x + width, China_means, width, label='China',color="red",edgecolor="black")
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by Countries')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()
plt.savefig('plot15.png')
# '''
import matplotlib.pyplot as plt 
import numpy as np 
last_week_cups = (20, 35, 30, 35, 27) 
this_week_cups = (25, 32, 34, 20, 25) 
names = ['Mary', 'Paul', 'Billy', 'Franka', 'Stephan'] 
fig = plt.figure() 
left, bottom, width, height = 0.1, 0.3, 0.8, 0.6 
ax = fig.add_axes([left, bottom, width, height]) 
width = 0.35 
ticks = np.arange(len(names)) 
ax.bar(ticks, last_week_cups, width, label='Last week') 
ax.bar(ticks + width, this_week_cups, width, label='This week') 
ax.set_ylabel('Cups of Coffee') 
ax.set_title('Coffee Consummation') 
ax.set_xticks(ticks + width/2) 
ax.set_xticklabels(names)
ax.legend(loc='best') 
plt.show()
plt.savefig('plot17.png')