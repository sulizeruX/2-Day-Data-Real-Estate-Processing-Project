import requests
import pandas as pd

# Replace this with your actual RentCast API key
API_KEY = '73bef0b7acff4fbc8dc2ba6d917ca294'
BASE_URL = 'https://api.rentcast.io/v1/properties'
HEADERS = {
    'Accept': 'application/json',
    'X-Api-Key': API_KEY
}

def fetch_properties_filtered(params=None, batch_size=500, required_clean=1000):
    clean_rows = []
    offset = 0

    while len(clean_rows) < required_clean:
        query = params.copy() if params else {}
        query.update({'limit': batch_size, 'offset': offset})

        response = requests.get(BASE_URL, headers=HEADERS, params=query)
        response.raise_for_status()
        data = response.json()

        # Validate format
        if not isinstance(data, list):
            print("Unexpected response format.")
            break

        # Transform and filter this batch
        transformed = transform_for_alignment(data)
        df = pd.DataFrame(transformed)

        # Keep only rows with no NaNs in important fields
        important_fields = ['address', 'city', 'latitude', 'longitude', 'numBedroom', 'numBathroom']
        df_clean = df.dropna(subset=important_fields)

        clean_rows.extend(df_clean.to_dict(orient='records'))

        offset += batch_size
        print(f"Fetched {len(clean_rows)} clean rows so far...")

        if len(data) < batch_size:
            print("No more data available from API.")
            break

    return clean_rows[:required_clean]

def transform_for_alignment(raw_data):
    transformed = []
    for item in raw_data:
        address_info = item.get('address', {})
        geo = item.get('geoLocation', {})
        transformed.append({
            'id': item.get('id'),
            'address': address_info.get('line'),
            'city': address_info.get('city'),
            'province': address_info.get('state'),
            'postalCode': address_info.get('zipCode'),
            'country': address_info.get('country'),
            'latitude': geo.get('latitude'),
            'longitude': geo.get('longitude'),
            'numBedroom': item.get('bedrooms'),
            'numBathroom': item.get('bathrooms'),
            'floorSizeValue': item.get('squareFootage'),
            'yearBuilt': item.get('yearBuilt'),
            'propertyType': item.get('propertyType'),
            'mostRecentEstimatedPriceAmount': item.get('estimatedValue'),
            'mostRecentRentalPriceAmount': item.get('rent'),
        })
    return transformed

if __name__ == '__main__':
    params = {'city': 'Austin', 'state': 'TX'}  # Customize if needed
    clean_data = fetch_properties_filtered(params=params, batch_size=500, required_clean=1000)

    df_final = pd.DataFrame(clean_data)
    df_final.to_csv("rentcast_aligned_clean.csv", index=False)
    print("✅ Saved 1000 clean rows to rentcast_aligned_clean.csv")
