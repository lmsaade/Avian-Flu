import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

data_path = r"C:\Users\Lina\OneDrive\Documents\AIT 580\data-clean_04May2025_1746388797025_part00000.csv"
shape_path = r"C:\Users\Lina\OneDrive\Documents\AIT 580\shapedata\cb_2024_us_state_500k.shp"

flock_data = pd.read_csv(data_path)
flock_data['Confirmed'] = pd.to_datetime(flock_data['Confirmed'])

flock_group = flock_data[flock_data['Confirmed'] != ''].groupby('Incident Site Name', as_index= False).size()
print(flock_group)

shape = gpd.read_file(shape_path)
shape = pd.merge(
    left = shape,
    right = flock_group,
    left_on = 'NAME',
    right_on = 'Incident Site Name',
    how = 'left'
)

shape = shape[~shape['NAME'].isin(['Alaska', 'Hawaii', 'Puerto Rico', 'Commonwealth of the Northern Mariana Islands', 'United States Virgin Islands', 'American Samoa', 'Guam'])]

ax = shape.boundary.plot(edgecolor = 'black', linewidth = .2, figsize = (10, 5))
shape.plot(ax = ax, column = "size", legend = True, cmap = 'coolwarm', legend_kwds = {'shrink': .6, 'orientation': 'horizontal'})

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

for edge in ['right', 'bottom', 'top', 'left']:
    ax.spines[edge].set_visible(False)

ax.set_title('Current HPAI H5N1 Outbreak Frequency in the United States', size = 15, weight = 'bold')
plt.show()