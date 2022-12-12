import matplotlib.pyplot as plt


#Creating variables for the bar graph 
x = ["Math",'Science','English']
y = [350,400,800]


#Changing the color and width of the bars
#You can change the edge color of the bars by typing "edgecolor = green"
c = ["orange",'pink','black']
plt.bar(x,y,color=c, width=0.5,edgecolor='green',linewidth=3)


plt.xlabel('Courses',color='yellow')
plt.ylabel('Number of students enrolled',color='blue')
plt.title("Amount of students enrolled in different courses",color='red')
plt.show()
