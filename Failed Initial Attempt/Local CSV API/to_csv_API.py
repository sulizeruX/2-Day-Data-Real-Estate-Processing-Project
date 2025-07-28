import requests
import pandas as pd

# Replace this with your actual RentCast API key
API_KEY = '73bef0b7acff4fbc8dc2ba6d917ca294'
BASE_URL = 'https://api.rentcast.io/v1/properties'
HEADERS = {
    'Accept': 'application/json',
    'X-Api-Key': API_KEY
}

def fetch_properties(params=None, limit=500, max_records=1000):
    all_props = []
    offset = 0

    while len(all_props) < max_records:
        batch_size = min(limit, max_records - len(all_props))
        query = params.copy() if params else {}
        query.update({'limit': batch_size, 'offset': offset})

        resp = requests.get(BASE_URL, headers=HEADERS, params=query)
        resp.raise_for_status()
        data = resp.json()

        # FIX: Handle if response is a list or dict
        if isinstance(data, list):
            records = data
        elif isinstance(data, dict):
            records = data.get('data') or data.get('records') or []
        else:
            print("Unexpected response format")
            break

        if not records:
            break

        all_props.extend(records)
        offset += batch_size

        if len(records) < batch_size:
            break

    return all_props

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
    params = {'city': 'Austin', 'state': 'TX'}  # adjust to suit your data scope
    raw = fetch_properties(params=params, limit=500, max_records=1000)
    aligned_data = transform_for_alignment(raw)

    df = pd.DataFrame(aligned_data)
    df.to_csv('rentcast_aligned.csv', index=False)
    print("Saved to rentcast_aligned.csv — ready for concat()")
