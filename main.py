from fastapi import FastAPI, HTTPException
from restcountries import RestCountryApiV2 as rapi

app = FastAPI(title="Country Details API")


allowed_countries = ["us", "ca", "swe", "in", "cyp"]

@app.get("/country/{country_code}", tags=['Country'])
async def get_country_data(country_code: str):
    if country_code.lower() not in allowed_countries:
        raise HTTPException(status_code=404, detail="Country not found in the given list")

    response = rapi.get_country_by_country_code(country_code)

    return response