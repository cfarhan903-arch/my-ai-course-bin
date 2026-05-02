import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# Load the dataset
data = pd.read_csv('realestate-usa.csv')
# display the types of the dataset
print(data.dtypes)
dffillter=data.head(40)
dffillter=data.head(100)
#sample the data
data_sampled = data.sample(n=100, random_state=42)
# set the style of the plot
sns.set_style('ticks')
# Create a cat plot of price vs. square footage 
sns.catplot(x='house_size', y='price', data=data_sampled)
# Show the plot
plt.show()
# other themes can be set similarly using sns.set_style('theme_name') where theme_name can be 'white', 'dark', 'whitegrid', 'darkgrid', or 'ticks'. 
sns.set_style('whitegrid')
sns.catplot(x='house_size', y='price', data=data_sampled)   
plt.show()
sns.set_style('darkgrid')
sns.catplot(x='house_size', y='price', data=data_sampled)
plt.show()
sns.set_style('dark')
sns.catplot(x='house_size', y='price', data=data_sampled)
plt.show()
sns.set_style('white')
sns.catplot(x='house_size', y='price', data=data_sampled)
plt.show()
# customize the theme
sns.set_style('whitegrid', {'axes.facecolor': 'lightblue'})
sns.catplot(x='house_size', y='price', data=data_sampled)
plt.show()
# create a plot
sns.lineplot(x='bed', y='bath', data=data_sampled)
plt.show()
# customize the theme for the line plot
sns.set_style('darkgrid', {'axes.facecolor': 'lightyellow'})        
sns.lineplot(x='bed', y='bath', data=data_sampled)
plt.show()
sns.set_style('whitegrid')
# kind='hist'
g=sns.displot(x='house_size', data=data_sampled, hue='price', kind='hist')
g.figure.suptitle("sns.displot(data=dffillter,x='house_size',y='price',hue='prev_sold_date',kind='hist')")
#display the plot
g.figure.show()
# kind='kde'
g=sns.barplot(x='house_size', data=data_sampled, hue='price')
g.figure.suptitle("sns.barplot(data=dffillter,x='house_size',y='price',hue='prev_sold_date',kind='kde')")
#display the plot
g.figure.show()
# kind='ecdf'
g=sns.ecdfplot(x='house_size', data=data_sampled, hue='price')
g.figure.suptitle("sns.ecdfplot(data=dffillter,x='house_size',y='price',hue='prev_sold_date')")
#display the plot   
g.figure.show()
# use seabone to create a plot
sns.set_style('whitegrid')
sns.boxplot(x='bed', y='bath', data=data_sampled)  
plt.show()
# customize the theme for the box plot
sns.set_style('darkgrid', {'axes.facecolor': 'lightyellow'})
sns.boxplot(x='bed', y='bath', data=data_sampled)
plt.show()
# create a violin plot
sns.set_style('whitegrid')
sns.violinplot(x='bed', y='bath', data=data_sampled)
plt.show()
# customize the theme for the violin plot
sns.set_style('darkgrid', {'axes.facecolor': 'lightyellow'})    
sns.violinplot(x='bed', y='bath', data=data_sampled)
plt.show()
# create a pair plot
sns.set_style('whitegrid')  
sns.pairplot(data_sampled, hue='price')
plt.show()
# customize the theme for the pair plot
sns.set_style('darkgrid', {'axes.facecolor': 'lightyellow'})
sns.pairplot(data_sampled, hue='price') 
plt.show()
# create a heatmap
sns.set_style('whitegrid')  
correlation_matrix = data_sampled.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
# customize the theme for the heatmap
sns.set_style('darkgrid', {'axes.facecolor': 'lightyellow'})
correlation_matrix = data_sampled.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()