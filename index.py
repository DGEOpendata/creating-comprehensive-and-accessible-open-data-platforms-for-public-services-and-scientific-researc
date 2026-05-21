python
import requests
import pandas as pd

# Example: Fetching Abu Dhabi Air Quality Data from Open Data API
API_URL = "https://example.opendata.abudhabi/api/air_quality"  # Replace with actual API endpoint
API_KEY = "your_api_key_here"

# Define headers with API Key
headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Fetch data
response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
    # Convert JSON data to DataFrame for analysis
    df = pd.DataFrame(data)
    # Save to CSV for further analysis
    df.to_csv("abu_dhabi_air_quality.csv", index=False)
    print("Data fetched and saved successfully!")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
