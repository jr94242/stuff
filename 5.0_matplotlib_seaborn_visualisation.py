import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline   # this is when running in conda environment so that plots appear below the executed cells


#yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

# in conda environment this will output a plot with the 6 yields for apples ; also plt.plot(yield_apples); will output just the plot
#plt.plot(yield_apples)







years = [2010, 2011, 2012, 2013, 2014, 2015]
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]

#plt.plot(years, yield_apples)  # this will output both the lists as they have equal 
# number of elements, each value corresponding to a particular year - both will be combined into a single plot 
# (years below on the x axis, values on the y axis)



# and to edit the axis appearance and values:
# plt.plot(years, yield_apples)
# plt.xlabel('Year')
# plt.ylabel('Yield (tons per hectare)');









# the same can be done for multiple lines:
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]

# plt.plot(years, apples)
# plt.plot(years, oranges)
# plt.xlabel('Year')
# plt.ylabel('Yield (tons per hectare)');

# this  will output a plot with 2 lines, one for apples, one for oranges

# and then to add additionally a title and a legend:

#plt.title("Crop Yields in Kanto")
#plt.legend(['Apples', 'Oranges']);   # in such order because we first defined the apples, then the oranges (should be in a list!!!)






# and to add MARKERS, the syntax is the following:

#plt.plot(years, apples, marker='o')
#plt.plot(years, oranges, marker='x')

# with all the other additional arguments for plot-building






# other plot styling methods(linestyle ; color ; linewidth ; markersize ; markeredgecolor ; markeredgewidth 
# ; markerfacecolor ; aplha)


# for example, it can look like this:
#plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')









# there is also an fmt marker that is a single string specifying the 3 most customizable thnigs in such cases
# fmt = '[marker][line][color]'

# plt.plot(years, apples, 's-b')
# plt.plot(years, oranges, 'o--r')

# if the line is not specified in fmt, only the markers will be drawn





# to change the shape of the figure ---> .figure

# plt.figure(figsize=(12, 6))
# plt.plot(years, apples, 'or')










# SEABORN - improving default style 

#sns.set_style('whitegrid') # once defined, this will be applied to all the plots created by matplotlib
#sns.set_style('darkgrid')



# you can kinda do the same directly from matplotlib
# import matplotlib
# matplotlib.rcParams['font.size'] = 14
# matplotlib.rcParams['figure.figsize'] = (9, 5)
# matplotlib.rcParams['figure.facecolor'] = '#00000000'
# to see what else is customisable ----> matplotlib.rcParams









# SCATTER PLOT

# load data into a pandas df
flowers_df = sns.load_dataset('iris')

#print(flowers_df)

u = flowers_df.species.unique()

#print(u)

#plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)  --> not a very useful plot, therefore a line chart is not 
# the most useful tool for analysis here, lets try a scatterplot



#sns.scatterplot(flowers_df.sepal_length, flowers_df.sepal_width) ---> this will output a scatterplot graph, only points, no lines






# ADDING HUES TO THE SCATTERPLOT --> a hue is sth to differentiate around ---> in this case, for each different species of 
# flowers, the dots will be a different color


#sns.scatterplot(x=flowers_df.sepal_length, y=flowers_df.sepal_width, hue=flowers_df.species, s=100);   --> s is for the size of dots






# you can then combine plt and sns when building a plot:

# plt.figure(figsize=(12, 6))
# plt.title('Sepal Dimensions')

# sns.scatterplot(x=flowers_df.sepal_length, 
#                 y=flowers_df.sepal_width, 
#                 hue=flowers_df.species,
#                 s=100);








# and then to build plots via seaborn and pandas df's:
# plt.title('Sepal Dimensions')
# sns.scatterplot(x='sepal_length', 
#                 y='sepal_width', 
#                 hue='species',
#                 s=100,
#                 data=flowers_df);  ---> inputting just the column names and in data we specify the correct df








# HISTOGRAMS
# data from a single column

# plt.title("Distribution of Sepal Width")
# plt.hist(flowers_df.sepal_width)



# we can then specify the number of bins:
# plt.hist(flowers_df.sepal_width, bins=5)

import numpy as np

# specifying boundaries of each bin:
# plt.hist(flowers_df.sepal_width, bins=np.arrange(2, 5, 0.25));


# bins of unequal sizes:
# plt.hist(flowers_df.sepal_width, bins=[1, 3, 4, 4.5])







# MULTIPLE HISTOGRAMS

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']

# plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));
# plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25));

# this will produce 2 histograms on top of each other, opacity is slightly decreased of both, so that the whole picture is clear








# the same thing can also be done for multiple histograms, stacked on top of each other:
# plt.title('Distribution of Sepal Width')

# plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
#          bins=np.arange(2, 5, 0.25), 
#          stacked=True);

# plt.legend(['Setosa', 'Versicolor', 'Virginica']);










# BAR CHART - very similar to linecharts, but they show bars for each value ---> plt.bar()

years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

# plt.bar(years, oranges);
# plt.bar(years, apples);

# this will draw the bar chart, in this case the two will be on top of one another 





# to also combine line charts with bar charts as they both have elements representing each value:
# plt.bar(years, oranges);
# plt.plot(years, oranges, 'o--r');  ---> this will draw both the plots and it will be more visually appealing to me





# to stack 2 bar charts on top of one another:
# plt.bar(years, apples)
# plt.bar(years, oranges, bottom=apples);










# BARPLOTS WITH AVERAGES ---> automatically computes averages

tips_df = sns.load_dataset('tips')

# print(tips_df)


# and now to create a barplot:
#sns.barplot(x='day', y='total_bill', data=tips_df);

# we can also specify a hue for the data:
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df);



# you can also make horizontal bars, by switching the x-y axis:
# sns.barplot(x='total_bill', y='day', hue='sex', data=tips_df);



# otherwise, with just a plt.bar() it would have looked like this:
# bill_avg_df = tips_df.groupby('day')[['total_bill]].mean()
#plt.bar(bill_avg_df.index, bill_avg_df.total_bill)


# x-axis is the one we want to group by, the y-axis is the values we are interested in














# HEATMAP ---> A heatmap is used to visualize 2-dimensional data like a matrix or a table using colors:

flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")

#print(flights_df)  # ---> pivoting results in rows: months ; columns: years ; values: passengers
# what this pivot method does is it makes the df look more like a matrix


#sns.heatmap(flight_df);   ---> this will make a heatmap of the dataset

# and ofcourse there are customization methods:
# plt.title("No. of Passengers (1000s)")
# sns.heatmap(flights_df, fmt="d", annot=True, cmap='Blues');

# what this means is: annot - will show values of each square if True ; cmap is the colormap, 
# to find others --> "matplotlib colormaps" ; fmt he has shown before, but I am unsure in what case is it used in 
# the example now (but removing it makes the values in the squares appear all fucked up and crooked)














# IMAGES - using matplotlib to display images


# from urllib.request import urlretrieve
# urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');

from PIL import Image
#img = Image.open('chart.jpg')




# an image from PIL is simply an np array containing the information for the colors of the image

# therefore, we can convert it to an array
# img_array = np.array(img)

# img_array.shape ----> in this case will display (481, 640, 3)



# and to display with matplotlib:
# plt.imshow(img)



# to modify the way it displays:
# plt.grid(False)
# plt.title('A data science meme')
# plt.axis('off')
# plt.imshow(img);



# to display just a part of the image, we select a slice from the array:
# plt.grid(False)
# plt.axis('off')
# plt.imshow(img_array[125:325,105:305]);













# PLOTTING MULTIPLE CHARTS IN A GRID

# to do this, you need to use:



#fig, axes = plt.subplot(2, 3, figsize=(16, 8))   ---> the 2 and 3 represent the rows(2) and columns(3)
# plt.tight_layout(pad=2)   ---> this will specify the distance betweeen the values of the plots

# if we access the axes, we can see that its an object, that can be manipulated:
# axes[0, 0].plot(years, oranges, 'o--r')

# for the one to the right, we need to populate axis[0, 1]




# and so on and so forth, until we end up with something like that:

# fig, axes = plt.subplots(2, 3, figsize=(16, 8))

# # Use the axes for plotting
# axes[0,0].plot(years, apples, 's-b')
# axes[0,0].plot(years, oranges, 'o--r')
# axes[0,0].set_xlabel('Year')
# axes[0,0].set_ylabel('Yield (tons per hectare)')
# axes[0,0].legend(['Apples', 'Oranges']);
# axes[0,0].set_title('Crop Yields in Kanto')


# # Pass the axes into seaborn
# axes[0,1].set_title('Sepal Length vs. Sepal Width')
# sns.scatterplot(x=flowers_df.sepal_length, 
#                 y=flowers_df.sepal_width, 
#                 hue=flowers_df.species, 
#                 s=100, 
#                 ax=axes[0,1]);

# # Use the axes for plotting
# axes[0,2].set_title('Distribution of Sepal Width')
# axes[0,2].hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
#          bins=np.arange(2, 5, 0.25), 
#          stacked=True);

# axes[0,2].legend(['Setosa', 'Versicolor', 'Virginica']);

# # Pass the axes into seaborn
# axes[1,0].set_title('Restaurant bills')
# sns.barplot(x='day', y='total_bill', hue='sex', data=tips_df, ax=axes[1,0]);

# # Pass the axes into seaborn
# axes[1,1].set_title('Flight traffic')
# sns.heatmap(flights_df, cmap='Blues', ax=axes[1,1]);

# # Plot an image using the axes
# axes[1,2].set_title('Data Science Meme')
# axes[1,2].imshow(img)
# axes[1,2].grid(False)
# axes[1,2].set_xticks([])
# axes[1,2].set_yticks([])

# plt.tight_layout(pad=2);


# notice that the same methods that we use on normal plots, in subplots they are typed differently, 
# instead of .title it is .set_title and others like that

# where is the fig element used tho, and why is it necessary???

# https://matplotlib.org/3.3.1/api/axes_api.html#the-axes-class 








# PAIR PLOTS WITH SEABORN

# sns.pairplot(flowers_df, hue='species');

# this will output different types of plots, all under one image, that will contain all sorts of information

# sns.pairplot(tips_df, hue='sex');    ----> same here 











# lesson finished, what I have to do now is to do the course project for data analysis































































