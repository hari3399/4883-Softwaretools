from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
import datetime

description = """🚀
## 4883 Software Tools
### Where awesomeness happens
"""

app = FastAPI(description=description)

db = []

# Open the CSV file and populate the `db` list with all the CSV data
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    db = list(reader)


def get_unique_countries():
    global db
    countries = set()

    for row in db:
        countries.add(row['Country'])

    return list(countries)


def get_unique_regions():
    global db
    regions = set()

    for row in db:
        regions.add(row['WHO_region'])

    return list(regions)


@app.get("/")
async def docs_redirect():
    #API's base route that shows documentation page.
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def get_countries():
    #Returns a names of unique countries
    return {"countries": get_unique_countries()}


@app.get("/regions/")
async def get_regions():
    #Returns a list of unique regions.
    return {"regions": get_unique_regions()}


def calculate_total_cases(db, country=None, region=None, year=None):
    total_cases = 0

    for row in db:
        if (
            (country and row['Country'] == country) or
            (region and row['WHO_region'] == region) or
            (year and row['Date_reported'].startswith(str(year))) or
            (not country and not region and not year)
        ):
            total_cases += int(row['Cumulative_cases'])

    return total_cases


@app.get("/cases/")
async def get_total_cases(
    country: str = Query(None, description="Name of the country."),
    region: str = Query(None, description="Region code."),
    year: int = Query(None, description="Year.")
):
    total_cases = calculate_total_cases(db, country, region, year)
    return {"total_cases": total_cases}


def calculate_total_deaths(db, country=None, region=None, year=None):
    total_deaths = 0

    for row in db:
        if (
            (country and row['Country'] == country) or
            (region and row['WHO_region'] == region) or
            (year and row['Date_reported'].startswith(str(year))) or
            (not country and not region and not year)
        ):
            total_deaths += int(row['Cumulative_deaths'])

    return total_deaths


@app.get("/deaths/")
async def get_total_deaths(
    country: str = Query(None, description="Name of the country."),
    region: str = Query(None, description="Region code."),
    year: int = Query(None, description="Year.")
):
    total_deaths = calculate_total_deaths(db, country, region, year)
    return {"total_deaths": total_deaths}


def find_country_with_max_deaths(db, min_date=None, max_date=None):
    max_deaths = 0
    country_with_max_deaths = ""

    for row in db:
        try:
            deaths = int(row['Cumulative_deaths'])
        except (KeyError, ValueError):
            # Skip rows without valid 'Cumulative_deaths' value
            continue

        date_reported = row['Date_reported']
        if (not min_date or date_reported >= min_date) and (not max_date or date_reported <= max_date):
            if deaths > max_deaths:
                max_deaths = deaths
                country_with_max_deaths = row['Country']

    return country_with_max_deaths, max_deaths


@app.get("/max_deaths")
async def get_country_with_max_deaths(
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    try:
        country_with_max_deaths, max_deaths = find_country_with_max_deaths(db, min_date, max_date)
        if country_with_max_deaths:
            return {"country_with_max_deaths": country_with_max_deaths, "max_deaths": max_deaths}
        else:
            return {"message": "No data found for the specified date range."}
    except Exception as e:
        return {"error": str(e)}




def find_country_with_min_deaths(db, min_date=None, max_date=None):
    min_deaths = float('inf')
    country_with_min_deaths = ""

    for row in db:
        try:
            deaths = int(row['Cumulative_deaths'])
        except (KeyError, ValueError):
            # Skip rows without valid 'Cumulative_deaths' value
            continue

        date_reported = row['Date_reported']
        if (not min_date or date_reported >= min_date) and (not max_date or date_reported <= max_date):
            if deaths < min_deaths:
                min_deaths = deaths
                country_with_min_deaths = row['Country']

    return country_with_min_deaths, min_deaths


@app.get("/min_deaths")
async def get_country_with_min_deaths(
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    try:
        country_with_min_deaths, min_deaths = find_country_with_min_deaths(db, min_date, max_date)
        if country_with_min_deaths:
            return {"country_with_min_deaths": country_with_min_deaths, "min_deaths": min_deaths}
        else:
            return {"message": "No data found for the specified date range."}
    except Exception as e:
        return {"error": str(e)}


    

import datetime

def calculate_average_deaths(db, country=None, min_date=None, max_date=None):
    total_deaths = 0
    num_days = 0

    try:
        min_date = datetime.datetime.strptime(min_date, "%Y-%m-%d") if min_date else None
        max_date = datetime.datetime.strptime(max_date, "%Y-%m-%d") if max_date else None

        for row in db:
            date_reported = datetime.datetime.strptime(row['Date_reported'], "%Y-%m-%d")
            if (not min_date or date_reported >= min_date) and (not max_date or date_reported <= max_date):
                if not country or (country and row['Country'] == country):
                    deaths = int(row['Cumulative_deaths'])
                    total_deaths += deaths
                    num_days += 1

        if num_days == 0:
            raise ValueError("No data found for the specified filters.")

        average_deaths_per_day = total_deaths / num_days
        return average_deaths_per_day

    except (KeyError, ValueError, TypeError) as e:
        raise ValueError("Invalid data format or filters.") from e


@app.get("/avg_deaths")
async def get_average_deaths(
    country: str = Query(None, description="The name of the country."),
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    try:
        average_deaths_per_day = calculate_average_deaths(db, country, min_date, max_date)
        return {"average_deaths_per_day": average_deaths_per_day}

    except ValueError as e:
        return {"error": str(e)}



if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)