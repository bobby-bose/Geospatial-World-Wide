
import json
import numpy as np

# Define the states with their coordinates for creating polygons
states_data = {
    'Andhra Pradesh': [[(78, 14), (82, 14), (82, 20), (78, 20), (78, 14)]],  # Example coordinates for Andhra Pradesh
    'Arunachal Pradesh': [[(91, 27), (97, 27), (97, 31), (91, 31), (91, 27)]],  # Example coordinates for Arunachal Pradesh
    'Assam': [[(89, 24), (95, 24), (95, 29), (89, 29), (89, 24)]],  # Example coordinates for Assam
    'Bihar': [[(83, 23), (89, 23), (89, 28), (83, 28), (83, 23)]],  # Example coordinates for Bihar
    'Chhattisgarh': [[(80, 17), (86, 17), (86, 23), (80, 23), (80, 17)]],  # Example coordinates for Chhattisgarh
    'Goa': [[(73, 14), (75, 14), (75, 16), (73, 16), (73, 14)]],  # Example coordinates for Goa
    'Gujarat': [[(68, 20), (75, 20), (75, 25), (68, 25), (68, 20)]],  # Example coordinates for Gujarat
    'Haryana': [[(74, 27), (79, 27), (79, 31), (74, 31), (74, 27)]],  # Example coordinates for Haryana
    'Himachal Pradesh': [[(75, 30), (79, 30), (79, 34), (75, 34), (75, 30)]],  # Example coordinates for Himachal Pradesh
    'Jharkhand': [[(83, 20), (88, 20), (88, 25), (83, 25), (83, 20)]],  # Example coordinates for Jharkhand
    'Karnataka': [[(74, 11), (78, 11), (78, 17), (74, 17), (74, 11)]],  # Example coordinates for Karnataka
    'Kerala': [[(74, 6), (78, 6), (78, 11), (74, 11), (74, 6)]],  # Example coordinates for Kerala
    'Madhya Pradesh': [[(75, 20), (81, 20), (81, 26), (75, 26), (75, 20)]],  # Example coordinates for Madhya Pradesh
    'Maharashtra': [[(70, 15), (76, 15), (76, 21), (70, 21), (70, 15)]],  # Example coordinates for Maharashtra
    'Manipur': [[(92, 23), (96, 23), (96, 27), (92, 27), (92, 23)]],  # Example coordinates for Manipur
    'Meghalaya': [[(88, 24), (92, 24), (92, 28), (88, 28), (88, 24)]],  # Example coordinates for Meghalaya
    'Mizoram': [[(90, 21), (94, 21), (94, 25), (90, 25), (90, 21)]],  # Example coordinates for Mizoram
    'Nagaland': [[(91, 25), (95, 25), (95, 29), (91, 29), (91, 25)]],  # Example coordinates for Nagaland
    'Odisha': [[(82, 16), (88, 16), (88, 21), (82, 21), (82, 16)]],  # Example coordinates for Odisha
    'Punjab': [[(73, 29), (78, 29), (78, 33), (73, 33), (73, 29)]],  # Example coordinates for Punjab
    'Rajasthan': [[(68, 24), (74, 24), (74, 30), (68, 30), (68, 24)]],  # Example coordinates for Rajasthan
    'Sikkim': [[(87, 26), (91, 26), (91, 30), (87, 30), (87, 26)]],  # Example coordinates for Sikkim
    'Tamil Nadu': [[(76, 8), (80, 8), (80, 13), (76, 13), (76, 8)]],  # Example coordinates for Tamil Nadu
    'Telangana': [[(77, 15), (81, 15), (81, 20), (77, 20), (77, 15)]],  # Example coordinates for Telangana
    'Tripura': [[(91, 22), (95, 22), (95, 26), (91, 26), (91, 22)]],  # Example coordinates for Tripura
    'Uttar Pradesh': [[(78, 25), (84, 25), (84, 30), (78, 30), (78, 25)]],  # Example coordinates for Uttar Pradesh
    'Uttarakhand': [[(77, 29), (81, 29), (81, 33), (77, 33), (77, 29)]],  # Example coordinates for Uttarakhand
    'West Bengal': [[(85, 20), (91, 20), (91, 25), (85, 25), (85, 20)]]  # Example coordinates for West Bengal

    # Add coordinates for other states here
}

# Generate random fire detection boundaries for each state
fire_detection_data = {}
for state in states_data:
    # Generate random coordinates within the state's boundaries
    min_lon, min_lat = np.min(states_data[state][0], axis=0)
    max_lon, max_lat = np.max(states_data[state][0], axis=0)
    num_points = np.random.randint(5, 15)  # Random number of points for fire detection boundary
    fire_detection_data[state] = [(np.random.uniform(min_lon, max_lon), np.random.uniform(min_lat, max_lat))
                                   for _ in range(num_points)]

# Create GeoJSON data for states
states_geojson = {
    "type": "FeatureCollection",
    "features": []
}

for state, coordinates in states_data.items():
    states_geojson['features'].append({
        "type": "Feature",
        "properties": {"name": state},
        "geometry": {
            "type": "Polygon",
            "coordinates": coordinates
        }
    })

# Save states_geojson to a file
with open('states.geojson', 'w') as f:
    json.dump(states_geojson, f)

# Create GeoJSON data for fire detection boundaries
fire_detection_geojson = {
    "type": "FeatureCollection",
    "features": []
}

for state, coordinates in fire_detection_data.items():
    fire_detection_geojson['features'].append({
        "type": "Feature",
        "properties": {"state": state},
        "geometry": {
            "type": "LineString",
            "coordinates": coordinates
        }
    })

# Save fire_detection_geojson to a file
with open('fire_detection_boundaries.geojson', 'w') as f:
    json.dump(fire_detection_geojson, f)

print("Dummy GeoJSON data generated successfully!")
