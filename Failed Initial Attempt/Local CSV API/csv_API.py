from fastapi import FastAPI
from fastapi.responses import FileResponse
import pandas as pd
import os
import uvicorn
import random
from faker import Faker

fake = Faker()

# # Replace this with your actual 102-column list
# column_list = ['id', 'address', 'apiURLs', 'assessedValues', 'brokers', 'buildingName', 'city', 'companies', 'congressionalDistrictHouse', 'country',
# 'county', 'countyFIPS', 'currentOwnerType', 'dateAdded', 'dateUpdated', 'deposits', 'descriptions', 'domains', 'estimatedPrices', 'features',
# 'fees', 'floorSizeValue', 'floorSizeUnit', 'geoLocation', 'imageURLs', 'instrumentNumber', 'keys', 'languagesSpoken', 'latitude', 'leasingTerms',
# 'legalDescription', 'legalRange', 'listingName', 'longitude', 'lotSizeValue', 'lotSizeUnit', 'managedBy', 'mostRecentPriceAmount', 'mostRecentPriceDomain',
# 'mostRecentPriceSourceURL', 'mostRecentPriceDate', 'mostRecentPriceFirstDateSeen', 'mostRecentBrokerAgent', 'mostRecentBrokerCompany', 'mostRecentBrokerEmails',
# 'mostRecentBrokerPhones', 'mostRecentBrokerDateSeen', 'mostRecentPriceAmount.1', 'mostRecentPriceDomain.1', 'mostRecentPricePerSquareFoot', 'mostRecentPriceSourceURL.1',
# 'mostRecentPriceDate.1', 'mostRecentPriceFirstDateSeen.1', 'mostRecentRentalPriceAmount', 'mostRecentRentalPricePeriod', 'mostRecentRentalPriceDomain',
# 'mostRecentRentalPricePerSquareFoot', 'mostRecentRentalPriceSourceURL', 'mostRecentRentalPriceDate', 'mostRecentRentalPriceFirstDateSeen', 'mostRecentEstimatedPriceAmount',
# 'mostRecentEstimatedPriceDomain', 'mostRecentEstimatedPricePerSquareFoot', 'mostRecentEstimatedPriceSourceURL', 'mostRecentEstimatedPriceDate', 'mostRecentEstimatedPriceFirstDateSeen',
# 'mostRecentStatus', 'mostRecentStatusDate', 'mostRecentStatusFirstDateSeen', 'mostRecentVacancy', 'mostRecentVacancyFirstDateSeen', 'mostRecentAbsenteeOwner',
# 'mostRecentAbsenteeOwnerFirstDateSeen', 'mostRecentInvoluntaryJudgement', 'mostRecentInvoluntaryLien', 'mostRecentInvoluntaryLienJudgementFirstDateSeen', 
# 'mlsNumber', 'neighborhoods', 'numBathroom', 'numBedroom', 'numFloor', 'numPeople', 'numRoom', 'numUnit', 'parking', 'paymentTypes', 'people', 'petPolicy',
# 'phones', 'postalCode', 'prices', 'propertyTaxes', 'propertyType', 'province', 'reviews', 'rules', 'subdivision', 'sourceURLs', 'statuses', 'taxID', 'transactions', 'yearBuilt']  # Dummy names; replace with actual names

# def generate_row():
#     row = {}
#     for col in column_list:
#         if "id" in col.lower():
#             row[col] = fake.uuid4()
#         elif "address" in col.lower():
#             row[col] = fake.address().replace("\n", ", ")
#         elif "date" in col.lower():
#             row[col] = fake.date_between(start_date='-3y', end_date='today').isoformat()
#         elif "price" in col.lower():
#             row[col] = random.randint(50000, 2000000)
#         elif "latitude" in col.lower():
#             row[col] = round(random.uniform(-90, 90), 6)
#         elif "longitude" in col.lower():
#             row[col] = round(random.uniform(-180, 180), 6)
#         elif "name" in col.lower():
#             row[col] = fake.company()
#         elif "city" in col.lower():
#             row[col] = fake.city()
#         elif "country" in col.lower():
#             row[col] = fake.country()
#         elif "postal" in col.lower():
#             row[col] = fake.postcode()
#         elif "email" in col.lower():
#             row[col] = fake.email()
#         elif "phone" in col.lower():
#             row[col] = fake.phone_number()
#         elif "url" in col.lower() or "domain" in col.lower():
#             row[col] = fake.url()
#         elif "tax" in col.lower():
#             row[col] = round(random.uniform(100.0, 10000.0), 2)
#         elif "description" in col.lower():
#             row[col] = fake.sentence()
#         elif "language" in col.lower():
#             row[col] = fake.language_name()
#         elif "status" in col.lower():
#             row[col] = random.choice(["Active", "Pending", "Sold", "Off Market"])
#         elif "value" in col.lower():
#             row[col] = round(random.uniform(100.0, 5000.0), 2)
#         else:
#             row[col] = fake.word()
#     return row

# # Create 98 rows of data
# data = [generate_row() for _ in range(98)]
# df = pd.DataFrame(data)

# # Save the CSV
# full_sample_102_columns = df.to_csv("full_sample_102_columns.csv", index=False)
# print("CSV file generated: full_sample_102_columns.csv")

app = FastAPI()
# DATA_PATH = "../../Downloads/2-Day-Data-Real-Estate-Processing-Project/967840_1.csv"

# @app.post("/upload")
# async def upload_csv(file: UploadFile = File(...)):
#     if not file.filename.endswith('.csv'):
#         raise HTTPException(status_code=400, detail="Invalid file type. Only CSV files are allowed.")
#     with open(DATA_PATH, "wb") as f:
#         content = await file.read()
#         f.write(content)
#     return {"message": "File uploaded successfully"}


@app.get("/data")
def get_csv():

    file_path = "corrected_contextual_synthetic_real_estate_data.csv"  # Replace with the path to your CSV file
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            media_type="text/csv",
            filename="example.csv"  # This sets the filename for the client
        )

if __name__ == "__main__":
    # if not os.path.exists(os.path.dirname(DATA_PATH)):
    #     os.makedirs(os.path.dirname(DATA_PATH))
    uvicorn.run(app, host="localhost", port=8000)
    print("Server is running at http://localhost:8000")
    print("Use /upload to upload a CSV file and /data to download the stored CSV file.")
    print("Press Ctrl+C to stop the server.")