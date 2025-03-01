import os
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('D:/workspace/Proj1/Hackathon')
data = pd.read_csv('US_Crime_Rates_1960_2014.csv')
#reading the data from a csv
num = data
#next few lines convert strings into their corresponding numerical values so that it is eaiser to work with
for col_name in num.columns:
    if(num[col_name].dtype == 'object'):
        num[col_name] = num[col_name].astype('category')
        num[col_name] = num[col_name].cat.codes

corr_ma = num.corr()
# correlates the data and a heatmap is created to visualize how correlated different features are(the lighter in color, the more correlated)
sns.heatmap(corr_ma, annot=True)

# a scatter plot is created to show the correlation between the violence rate and the year
scatter_plot = plt.figure()
year_violence = scatter_plot.add_subplot(1, 1, 1)
year_violence.scatter(data['Year'], data['Violent'])
year_violence.set_title('Year vs Violence')
year_violence.set_xlabel('Year')
year_violence.set_ylabel('Violence Rate')

# a scatter plot is created to show the correlation between the year and the total number of crimes
scatter_plot = plt.figure()
year_violence = scatter_plot.add_subplot(1, 1, 1)
year_violence.scatter(data['Year'], data['Total'], color='red')
year_violence.set_title('Year vs Total Crimes')
year_violence.set_xlabel('Year')
year_violence.set_ylabel('Total Crimes')

#describes what the graph shows
''' The data shows that there is a correlation between the year and the total crimes. Additionally, most types of crimes increase each year. 
Between the years of 1980 and 2000, there are more crimes, and they are more violent. Before 1980, the number of crimes steadily increases.
After 2000, the number of crimes decreases slightly but seems to remain constant after that. 
Between those years, crimes were probably paid more attention to, but still are very common. We need to work now, rather than later,
to decrease the number of crimes and make our world safer for everyone. Everyone deserves the right to feel safe and have access to
    healthcare without the worry of getting attacked. '''
