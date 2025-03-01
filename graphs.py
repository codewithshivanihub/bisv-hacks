import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
os.chdir('D:/workspace/Proj1/Hackathon')
data = pd.read_csv('US_Crime_Rates_1960_2014.csv')
num = data
for col_name in num.columns:
    if(num[col_name].dtype == 'object'):
        num[col_name] = num[col_name].astype('category')
        num[col_name] = num[col_name].cat.codes
corr_ma = num.corr()
sns.heatmap(corr_ma, annot=True)

scatter_plot = plt.figure()
year_violence = scatter_plot.add_subplot(1, 1, 1)
year_violence.scatter(data['Year'], data['Violent'])
year_violence.set_title('Year vs Violence')
year_violence.set_xlabel('Year')
year_violence.set_ylabel('Violence Rate')

scatter_plot = plt.figure()
year_violence = scatter_plot.add_subplot(1, 1, 1)
year_violence.scatter(data['Year'], data['Total'], color='red')
year_violence.set_title('Year vs Total Crimes')
year_violence.set_xlabel('Year')
year_violence.set_ylabel('Total Crimes')

