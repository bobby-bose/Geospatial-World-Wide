import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.models import Sequential
import seaborn as sns
import folium

# Create some static data for demonstration purposes
# Let's assume we have 100 samples with a window size of 1
num_samples = 100
window_size = 1

# Generate some random data for X_train and Y_train
X_train = np.random.rand(num_samples, window_size)
Y_train = np.random.rand(num_samples)

# Reshape input data for LSTM
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))

# Build LSTM model
model = Sequential()
model.add(LSTM(2000, activation='tanh', recurrent_activation='hard_sigmoid', input_shape=(1, window_size)))
model.add(Dropout(0.2))
model.add(Dense(500))
model.add(Dropout(0.4))
model.add(Dense(500))
model.add(Dropout(0.4))
model.add(Dense(400))
model.add(Dropout(0.4))
model.add(Dense(1, activation='linear'))
model.compile(loss="mean_squared_error", optimizer="adam")

# Train LSTM model
model.fit(X_train, Y_train, epochs=1, batch_size=64)

# Function to predict and score
def predict_and_score(model, X, Y):
    # Fill in static data for demonstration purposes
    pred = np.random.rand(len(Y), 1)  # Example prediction data
    orig_data = np.random.rand(len(Y))  # Example original data
    score = np.sqrt(mean_squared_error(orig_data, pred[:, 0]))
    return score, pred

# Perform prediction and scoring (replace static data with actual predictions)
rmse_train, train_predict = predict_and_score(model, X_train, Y_train)

# Plotting and visualization code...

# Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(np.random.rand(10, 10), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix Heatmap')
plt.show()

# Choropleth map (replace with actual data and map creation)
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
          'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
          'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
          'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

rainfall_data = pd.DataFrame({
    'State': states,
    'Rainfall': np.random.uniform(50, 500, len(states))  # Random rainfall values between 50 and 500 mm
})

choropleth_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
# choropleth_map.choropleth(geo_data='states.geojson', data=rainfall_data,
#                           columns=['State', 'Rainfall'], key_on='feature.properties.name',
#                           fill_color='YlGnBu', legend_name='Rainfall (mm)')

# Correct the above wrong code

choropleth_map.save('choropleth_map.html')

# Evaluation metrics (replace static data with actual metrics)
accuracy = 0.85
precision = 0.78
recall = 0.82
f1_score = 0.80

print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')

# Okay now display the graphical language on geometrical map of India with rainfall measured and show it to me

import folium

# Define the states and their corresponding rainfall data
states = ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Goa', 'Gujarat',
          'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra',
          'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
          'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

rainfall_data = pd.DataFrame({
    'State': states,
    'Rainfall': np.random.uniform(50, 500, len(states))  # Random rainfall values between 50 and 500 mm
})

# Create a map centered around India
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add the choropleth layer to the map
folium.Choropleth(
    geo_data='states.geojson',  # GeoJSON file containing state boundaries
    data=rainfall_data,          # Rainfall data
    columns=['State', 'Rainfall'],  # Columns to use for the choropleth
    key_on='feature.properties.name',  # Key in the GeoJSON file that corresponds to the state name
    fill_color='YlGnBu',  # Color scale
    legend_name='Rainfall (mm)'  # Legend title
).add_to(india_map)

# Save the map to an HTML file
india_map.save('rainfall_map.html')
