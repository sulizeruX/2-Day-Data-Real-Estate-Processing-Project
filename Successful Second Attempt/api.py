from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import pandas as pd
import io

app = FastAPI()

@app.get("/generate-property-data")
def generate_property_data():
    n = 500  # number of rows
    data = {
        "identifier_Id": range(1, n + 1),
        "lot_lotnum": [str((i % 20) + 1) for i in range(n)],
        "lot_lotsize1": [0.1 + (i % 10) * 0.05 for i in range(n)],
        "lot_lotsize2": [4000 + (i % 50) * 100 for i in range(n)],
        "lot_pooltype": ["NO POOL" if i % 2 == 0 else "POOL" for i in range(n)],
        "area_blockNum": [i % 10 for i in range(n)],
        "area_subdname": [f"Subdivision {i % 5}" for i in range(n)],
        "area_taxcodearea": [f"TX{i % 3}" for i in range(n)],
        "address_line1": [f"{1000+i} Main St" for i in range(n)],
        "address_locality": [f"City{i % 10}" for i in range(n)],
        "address_postal2": [f"ZIP2-{i % 100}" for i in range(n)],
        "address_postal3": [f"ZIP3-{i % 50}" for i in range(n)],
        "location_accuracy": ["ROOFTOP" for _ in range(n)],
        "location_geoIdV4_CO": [f"CO{i % 1000}" for i in range(n)],
        "summary_proptype": ["Single Family" if i % 2 == 0 else "Condo" for i in range(n)],
        "summary_propertyType": ["Residential" for _ in range(n)],
        "summary_yearbuilt": [1950 + (i % 75) for i in range(n)],
        "summary_propIndicator": ["Y" if i % 10 != 0 else "N" for i in range(n)],
        "utilities_coolingtype": ["Central" if i % 2 == 0 else "None" for i in range(n)],
        "utilities_heatingtype": ["Gas" if i % 3 == 0 else "Electric" for i in range(n)],
        "building_size_bldgsize": [1000 + i * 2 for i in range(n)],
        "building_size_grosssize": [1200 + i * 2 for i in range(n)],
        "building_size_grosssizeadjusted": [1100 + i * 2 for i in range(n)],
        "building_size_livingsize": [950 + i * 2 for i in range(n)],
        "building_size_sizeInd": ["Actual" for _ in range(n)],
        "building_size_universalsize": [1050 + i * 2 for i in range(n)],
        "building_rooms_bathsfull": [2 + (i % 3) for i in range(n)],
        "building_rooms_bathstotal": [2.5 + (i % 2) * 0.5 for i in range(n)],
        "building_interior_bsmtsize": [0 if i % 4 == 0 else 500 for i in range(n)],
        "building_interior_bsmttype": ["Finished" if i % 3 == 0 else "Unfinished" for i in range(n)],
        "building_interior_fplcind": ["Y" if i % 5 == 0 else "N" for i in range(n)],
        "building_interior_fplctype": ["Wood" if i % 2 == 0 else "Gas" for i in range(n)],
        "building_construction_constructiontype": ["Frame" for _ in range(n)],
        "building_construction_roofcover": ["Asphalt" for _ in range(n)],
        "building_construction_roofShape": ["Gable" for _ in range(n)],
        "building_construction_wallType": ["Siding" for _ in range(n)],
        "building_parking_garagetype": ["Attached" if i % 3 == 0 else "Detached" for i in range(n)],
        "building_parking_prkgSize": [200 + i % 100 for i in range(n)],
        "building_parking_prkgSpaces": [1 + i % 3 for i in range(n)],
        "building_parking_prkgType": ["Garage" for _ in range(n)],
        "building_summary_archStyle": ["Ranch" if i % 2 == 0 else "Colonial" for i in range(n)],
        "building_summary_bldgType": ["House" for _ in range(n)],
        "building_summary_imprType": ["TypeA" for _ in range(n)],
        "building_summary_levels": [1 + i % 3 for i in range(n)],
        "building_summary_quality": ["Average" for _ in range(n)],
        "building_summary_storyDesc": ["One Story" if i % 2 == 0 else "Two Story" for i in range(n)],
        "building_summary_viewCode": ["NONE" for _ in range(n)],
        "sale_amount_saletranstype": ["Full" for _ in range(n)],
        "sale_amount_saleamt": [100000 + i * 1000 for i in range(n)],
        "sale_calculation_pricepersizeunit": [100 + i % 30 for i in range(n)],
    }

    df = pd.DataFrame(data)

    # Convert to CSV in-memory
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)

    return StreamingResponse(
        stream,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=property_data.csv"}
    )

# Entry point for running locally
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
