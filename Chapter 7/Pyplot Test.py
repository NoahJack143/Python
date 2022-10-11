#Import
import matplotlib.pyplot as plt

#This program displays a simple line graph.

def main(): #7-19 #ORANGE FOR SOME REASON
    
    #Add a title
    plt.title('Sales by Year')
    
    #add labels to the axes
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    #set the axis limits
    #plt.xlim(xmin = -1, xmax = 10)
    #plt.ylim(ymin = -1, ymax = 6)
    
    #Change the ticks
    plt.xticks([0, 1, 2, 3, 4],['2000', '2001', '2002', '2003','2004'])
    plt.yticks([0, 1, 2, 3, 4],['$0m', '$1m', '$2m', '$3m', '$4m'])
    
    #Create lists with the X and Y coordinates of each data point.
    x_coords = [0,1,2,3,4]
    y_coords = [0,3,1,5,2]
    
    #Build the line graph.
    plt.plot(x_coords, y_coords)
    
    #Draw the line graph
    plt.plot(x_coords, y_coords, marker = 'D') #marker affects the points on the graph
    
    #Grid lines?
    plt.grid(True)
    
    #dipslay the line raph.
    plt.show()

#Max of the graph
#plt.xlim(xmin=1, xmax=100)
#plt.ylim(ymin=1, ymax=100)

#Ticks
#plt.xticks([0, 1, 2, 3, 4],['2000', '2001', '2002', '2003','2004'])
#plt.yticks([0, 1, 2, 3, 4],['$0m', '$1m', '$2m', '$3m', '$4m'])

def bar_test(): #Prgoram 7-24
    #bar chart accepts noa rguments
    #it creates two lists for left edges
    #and bar heights and uses matplotlib to plot a bar chat
    
    #create a list ofr bar center and height
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    
    #set the bar width
    bar_width = 10
    
    #plot the chart
    plt.bar(left_edges, heights, bar, width,
            color = ('r', 'g', 'b', 'y', 'k'))
    
    #Add a title
    plt.title('Sales by Year')
    
    #add labels for axes
    plt.xlabel('Year')
    plt.ylabel('Sales')
    
    #add custom tick marks
    plt.xticks([5, 15, 25, 35, 45],['2000', '2001', '2002', '2003', '2004'])
    plt.yticks([0, 100, 200, 300, 400, 500,],['$0m', '$1m', '$2', '$3', '$4m', '$5m'])
    
    #Show the graph
    plt.show()
    
def pie_test(): #Program 7-27
    #pie chart accepts no arguments
    #it creates a list of values
    #and uses matplotlib to plot a pie chart
    
    #set values
    sales = [100, 400, 300, 600]
    
    #Set slice lables
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    
    #set the pie colors
    plt.pie(sales, colors = ('r','g','b','k'))
    
    #draw the pie chart
    plt.pie(sales, labels=slice_labels)
    
    #add a title
    plt.title('Sales by Quarter')
    
    #show the pie chart
    plt.show()
    