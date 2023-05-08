import matplotlib.pyplot as plot

# set up your lists

numlist = [8, 6, 5, 3]

namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']

colorlist = ['pink', 'yellow', 'purple', 'green' ]
#(Colors Associated with the name list-corresponds to Index position )

explodelist = [0.1, 0.1, 0.1, 0.1]
#(used as a way to separate the Pie pieces with the decimal place being the space)

# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
#(Start Angle at 90 degrees begins with Sophmores and shifts the angle to whatever user enters)
#Auto PCT allows me to display cetrain percentage values using python string values

plot.axis('equal')
plot.savefig('piechart.png')

#Hey found this out using Google :)
plot.show()