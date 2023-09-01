import requests
from PIL import Image

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b"

# WMS parameters
params = {
    "SERVICE": "WMS",
    "REQUEST": "GetMap",
    "SHOWLOGO": "false",
    "VERSION": "1.3.0",
    "LAYERS": "NDVI",
    "MAXCC": "20",
    "WIDTH": "100",
    "HEIGHT": "100",
    "CRS": "EPSG:4326",
    "BBOX": "-118.9519,33.7056,-118.1553,34.3373",
    "TIME": "2020-01/2020-02",
    "FORMAT": "image/jpeg"
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Save the JPEG image to a file
    output_file = r"C:\Muneer\world3.jpg"
    with open(output_file, 'wb') as file:
        file.write(response.content)

    print(f"JPEG image exported to {output_file}")

    # Optionally, you can open and display the image
    image = Image.open(output_file)
    image.show()

else:
    print("Error: Failed to retrieve data from the WMS server.")

import requests
import json

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b?SERVICE=WMS&REQUEST=GetMap&SHOWLOGO=false&VERSION=1.3.0&LAYERS=NDVI&MAXCC=20&WIDTH=640&HEIGHT=640&CRS=EPSG:4326&BBOX=38.481634,-122.503351,38.533838,-122.42798&FORMAT=application/json"

# WMS parameters
params = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "COLOR_HEX": "FFFFFF",
        "ID": 0
      },
      "geometry": {
        "type": "MultiPolygon",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC::CRS84"
            }
        },
        "coordinates": [[[
            [-122.503351, 38.51637],
            [-122.478057, 38.533838],
            [-122.42798, 38.499095],
            [-122.454379, 38.481634],
            ...
        ]]]
      }
    },
    ...
  ]
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data
    geojson_data = response.json()

    # Save GeoJSON data to a file
    output_file = r"C:\Muneer\ndvi_napa_wineries_9.geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson_data, file)

    print(f"GeoJSON data exported to {output_file}")

else:
    print("Error: Failed to retrieve data from the WMS server.")

import requests
import json

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b?SERVICE=WMS&REQUEST=GetMap&SHOWLOGO=false&VERSION=1.3.0&LAYERS=SOIL&MAXCC=20&WIDTH=640&HEIGHT=640&CRS=EPSG:4326&BBOX=38.481634,-122.503351,38.533838,-122.42798&FORMAT=application/json"

# WMS parameters
params = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "COLOR_HEX": "FFFFFF",
        "ID": 0
      },
      "geometry": {
        "type": "MultiPolygon",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC::CRS84"
            }
        },
        "coordinates": [[[
            [-122.503351, 38.51637],
            [-122.478057, 38.533838],
            [-122.42798, 38.499095],
            [-122.454379, 38.481634],
            ...
        ]]]
      }
    },
    ...
  ]
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data
    geojson_data = response.json()

    # Save GeoJSON data to a file
    output_file = r"C:\Muneer\NDVI_III.geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson_data, file)

    print(f"GeoJSON data exported to {output_file}")

else:
    print("Error: Failed to retrieve data from the WMS server.")

import requests
import json

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b?SERVICE=WMS&REQUEST=GetMap&SHOWLOGO=false&VERSION=1.3.0&LAYERS=SWBM&MAXCC=20&WIDTH=640&HEIGHT=640&CRS=EPSG:4326&BBOX=38.481634,-122.503351,38.533838,-122.42798&FORMAT=application/json"

# WMS parameters
params = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "COLOR_HEX": "FFFFFF",
        "ID": 0
      },
      "geometry": {
        "type": "MultiPolygon",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC::CRS84"
            }
        },
        "coordinates": [[[
            [-122.503351, 38.51637],
            [-122.478057, 38.533838],
            [-122.42798, 38.499095],
            [-122.454379, 38.481634],
            ...
        ]]]
      }
    },
    ...
  ]
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data
    geojson_data = response.json()

    # Save GeoJSON data to a file
    output_file = r"C:\Muneer\water.geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson_data, file)

    print(f"GeoJSON data exported to {output_file}")

else:
    print("Error: Failed to retrieve data from the WMS server.")

import requests
import json

# WMS URL
wms_url = "https://services.sentinel-hub.com/ogc/wms/9b1b49e6-1f7c-4947-a853-3d481601a66b?SERVICE=WMS&REQUEST=GetMap&SHOWLOGO=false&VERSION=1.3.0&LAYERS=LST&MAXCC=20&WIDTH=640&HEIGHT=640&CRS=EPSG:4326&BBOX=38.481634,-122.503351,38.533838,-122.42798&FORMAT=application/json"

# WMS parameters
params = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "COLOR_HEX": "FFFFFF",
        "ID": 0
      },
      "geometry": {
        "type": "MultiPolygon",
        "crs": {
            "type": "name",
            "properties": {
                "name": "urn:ogc:def:crs:OGC::CRS84"
            }
        },
        "coordinates": [[[
            [-122.503351, 38.51637],
            [-122.478057, 38.533838],
            [-122.42798, 38.499095],
            [-122.454379, 38.481634],
            ...
        ]]]
      }
    },
    ...
  ]
}

# Send WMS request
response = requests.get(wms_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Load the GeoJSON data
    geojson_data = response.json()

    # Save GeoJSON data to a file
    output_file = r"C:\Muneer\temperature_3.geojson"
    with open(output_file, 'w') as file:
        json.dump(geojson_data, file)

    print(f"GeoJSON data exported to {output_file}")

else:
    print("Error: Failed to retrieve data from the WMS server.")




