from bokeh.plotting import figure 
from bokeh.io import output_file, show
from numpy import cos, linspace

output_file("testBokeh.html", title='Bokeh Plot') 
#Display plots in html
#Use numpy to make some data
x = linspace(-6,6,100)
y  =  cos(x)

# Use Bokeh to make  a plot p
p = figure(width=500, height=500)
p.circle(x, y, size=7, color="firebrick", alpha=0.5)
show(p)
# alpha is saturation
