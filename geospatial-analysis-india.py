import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import folium

# Read the dataset
cities = pd.read_csv("cities_r2.csv")

# Drop unnecessary columns
cities = cities.drop(["name_of_city", "state_name"], axis=1)

# Check the column names
print(cities.columns)

# Group cities by state code and count the number of cities in each state
states = cities.groupby('state_code')['state_code'].count().sort_values(ascending=True)

# Plot the number of cities per state
states.plot(kind="barh", fontsize=20, color='green')
plt.grid()
plt.xlabel('Number of cities per state', fontsize=20)
plt.show()

lit_by_states = cities.groupby('state_code').agg({'literates_total': 'sum'})  # Use 'sum' instead of np.sum
pop_by_states = cities.groupby('state_code').agg({'population_total': 'sum'})  # Use 'sum' instead of np.sum
literate_rate = lit_by_states.literates_total * 100 / pop_by_states.population_total
literate_rate = literate_rate.sort_values(ascending=True)
plt.subplots(figsize=(7, 6))
ax = sns.barplot(x=literate_rate, y=literate_rate.index, color='brown')
ax.set_title('States according to literacy rate', size=20, alpha=0.5, color='red')
ax.set_xlabel('Literacy Rate(as % of population)', size=15, alpha=0.5, color='red')
ax.set_ylabel('States', size=15, alpha=0.5, color='red')

numeric_data = cities.select_dtypes(include=['int64', 'float64'])
kurtosis_values = numeric_data.kurt()
print(kurtosis_values)

numeric_data = cities.select_dtypes(include=['int64', 'float64'])
skewness_values = numeric_data.skew()
print(skewness_values)

cities['latitude'] = cities['location'].apply(lambda x: x.split(',')[0])
cities['longitude'] = cities['location'].apply(lambda x: x.split(',')[1])

top_pop_cities = cities.sort_values(by='population_total', ascending=False).head(20)

graduates_above_1lakh = cities[cities['total_graduates'] > 100000]

uttarpradesh = cities[cities['state_code'] == 9]

m_1 = folium.Map(location=[20.5936832, 78.962883], tiles='cartodbpositron', zoom_start=5)
for idx, row in uttarpradesh.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(m_1)

graduates_sizes = graduates_above_1lakh["total_graduates"].apply(lambda x: int(x / 6000))
colorbar_values = np.linspace(graduates_above_1lakh["total_graduates"].min(),
                               graduates_above_1lakh["total_graduates"].max(), num=10).astype(int)




import json
import numpy as np

def np_encoder(object):
    if isinstance(object, np.integer):
        return int(object)
    elif isinstance(object, np.floating):
        return float(object)
    elif isinstance(object, np.ndarray):
        return object.tolist()
    else:
        raise TypeError(f"Object of type {type(object)} is not JSON serializable")

# Your NumPy object
obj = np.array([1, 2, 3], dtype=np.int64)

# Serialize to JSON using the custom encoder
json_str = json.dumps(obj, default=np_encoder)
print(json_str)

# Heat Map
plt.figure(figsize=(10, 8))
sns.heatmap(cities.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Choropleth Map
# (Assuming you have a GeoJSON file for states boundaries)
# choropleth_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
# choropleth_map.choropleth(geo_data='states.geojson', data=your_data, columns=[...], key_on='feature.id', fill_color='YlGnBu', legend_name='Your Legend')
# choropleth_map.save('choropleth_map.html')

# Additional Graphs
plt.figure(figsize=(10, 6))
sns.boxplot(x='state_code', y='population_total', data=cities)
plt.title('Boxplot of Population Total by State Code')
plt.xlabel('State Code')
plt.ylabel('Population Total')
plt.show()

# Evaluation Metrics
# (Assuming you have classification results stored in variables)
accuracy = 0.85
precision = 0.78
recall = 0.82
f1_score = 0.80

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1_score}')




