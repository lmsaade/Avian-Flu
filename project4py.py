#Import packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

#Read flock_data from S3/AWS Glue job export into Python.
what_the_flock = pd.read_parquet(r"C:\Users\Lina\OneDrive\Documents\AIT 580\data-clean_04May2025_1746381079185_part00000.parquet")
print(what_the_flock)

#Print dataframe data types
print(what_the_flock.dtypes)

#Oh no! Our data types aren't aligned with our Glue job. Let's fix the data types.
what_the_flock['Confirmed'] = pd.to_datetime(what_the_flock['Confirmed'])
what_the_flock['Control_Area_Released'] = pd.to_datetime(what_the_flock['Control_Area_Released'])
what_the_flock['Control_Zone_Release'] = pd.to_datetime(what_the_flock['Control_Zone_Release'])
what_the_flock['Last_Reported_Detection'] = pd.to_datetime(what_the_flock['Last_Reported_Detection'])

print(what_the_flock.describe())

#Have avian flu cases been increasing in the United States?
what_the_flock['Month_Year'] = pd.to_datetime(what_the_flock['Confirmed']).dt.to_period('M').dt.to_timestamp()
uptick = what_the_flock.groupby(['Month_Year']).size().reset_index(name= 'frequency')
uptick_plot = sns.lineplot(data= uptick, x= 'Month_Year', y= 'frequency')
uptick_plot.xaxis.set_major_formatter(mdates.DateFormatter('%B %Y'))
uptick_plot.set_xlabel('Date', fontsize = 15)
uptick_plot.set_ylabel("Frequency of Avian Flu Cases", fontsize = 15)
uptick_plot.set_title("Avian Flu Cases Over Time in the United States", fontsize = 20)
uptick_plot.tick_params(axis = 'both', labelsize = 12)
plt.xticks(rotation = 30)
plt.figure(figsize = (8, 6))
plt.savefig("seaborn_plot1.png", dpi = 300)


