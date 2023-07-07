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
    """API's base route that redirects to the documentation page."""
    return RedirectResponse(url="/docs")


@app.get("/countries/")
async def get_countries():
    """Returns a list of unique countries."""
    return {"countries": get_unique_countries()}


@app.get("/regions/")
async def get_regions():
    """Returns a list of unique regions."""
    return {"regions": get_unique_regions()}


@app.get("/cases/")
async def get_total_cases(
    country: str = Query(None, description="The name of the country."),
    region: str = Query(None, description="The code of the region."),
    year: int = Query(None, description="The year.")
):
    """
    Retrieves the total cases for the given country, region, and year.

    Parameters:
    - `country`: The name of the country (optional).
    - `region`: The code of the region (optional).
    - `year`: The year (optional).

    Returns:
    - If `country` is provided, returns the total cases for the given country.
    - If `region` is provided, returns the total cases for the given region.
    - If both `country` and `year` are provided, returns the total cases for the given country in the specified year.
    - If both `region` and `year` are provided, returns the total cases for the given region in the specified year.
    - If no parameters are provided, returns the total cases for all countries, regions, and years.

    Example usage:
    - /cases?country=France
    - /cases?region=AFRO
    - /cases?country=France&year=2020
    - /cases?region=AFRO&year=2020
    - /cases
    """
    total_cases = 0

    for row in db:
        if country and year:
            if row['Country'] == country and row['Date_reported'].startswith(str(year)):
                total_cases += int(row['Cumulative_cases'])
        elif region and year:
            if row['WHO_region'] == region and row['Date_reported'].startswith(str(year)):
                total_cases += int(row['Cumulative_cases'])
        elif country:
            if row['Country'] == country:
                total_cases += int(row['Cumulative_cases'])
        elif region:
            if row['WHO_region'] == region:
                total_cases += int(row['Cumulative_cases'])
        elif year:
            if row['Date_reported'].startswith(str(year)):
                total_cases += int(row['Cumulative_cases'])
        else:
            total_cases += int(row['Cumulative_cases'])

    return {"total_cases": total_cases}


@app.get("/deaths/")
async def get_total_deaths(
    country: str = Query(None, description="The name of the country."),
    region: str = Query(None, description="The code of the region."),
    year: int = Query(None, description="The year.")
):
    """
    Retrieves the total deaths for the given country, region, and year.

    Parameters:
    - `country`: The name of the country (optional).
    - `region`: The code of the region (optional).
    - `year`: The year (optional).

    Returns:
    - If `country` is provided, returns the total deaths for the given country.
    - If `region` is provided, returns the total deaths for the given region.
    - If both `country` and `year` are provided, returns the total deaths for the given country in the specified year.
    - If both `region` and `year` are provided, returns the total deaths for the given region in the specified year.
    - If no parameters are provided, returns the total deaths for all countries, regions, and years.

    Example usage:
    - /deaths?country=France
    - /deaths?region=AFRO
    - /deaths?country=France&year=2020
    - /deaths?region=AFRO&year=2020
    - /deaths
    """
    total_deaths = 0

    for row in db:
        if country and year:
            if row['Country'] == country and row['Date_reported'].startswith(str(year)):
                total_deaths += int(row['Cumulative_deaths'])
        elif region and year:
            if row['WHO_region'] == region and row['Date_reported'].startswith(str(year)):
                total_deaths += int(row['Cumulative_deaths'])
        elif country:
            if row['Country'] == country:
                total_deaths += int(row['Cumulative_deaths'])
        elif region:
            if row['WHO_region'] == region:
                total_deaths += int(row['Cumulative_deaths'])
        elif year:
            if row['Date_reported'].startswith(str(year)):
                total_deaths += int(row['Cumulative_deaths'])
        else:
            total_deaths += int(row['Cumulative_deaths'])

    return {"total_deaths": total_deaths}


@app.get("/max_deaths")
async def get_country_with_max_deaths(
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    """
    Finds the country with the most deaths.

    Parameters:
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - If `min_date` and `max_date` are provided, returns the country with the most deaths between the given date range.
    - If no date range is provided, returns the country with the most deaths overall.
    """
    max_deaths = 0
    country_with_max_deaths = ""

    for row in db:
        if min_date and max_date:
            if min_date <= row['Date_reported'] <= max_date:
                deaths = int(row['Cumulative_deaths'])
                if deaths > max_deaths:
                    max_deaths = deaths
                    country_with_max_deaths = row['Country']
        else:
            deaths = int(row['Cumulative_deaths'])
            if deaths > max_deaths:
                max_deaths = deaths
                country_with_max_deaths = row['Country']

    return {"country_with_max_deaths": country_with_max_deaths, "max_deaths": max_deaths}
@app.get("/min_deaths")
async def get_min_deaths(
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    """
    Retrieves the minimum number of deaths within the provided date range.

    Parameters:
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - The minimum number of deaths within the date range.
    """
    min_deaths = None

    for row in db:
        if min_date and max_date:
            if min_date <= row['Date_reported'] <= max_date:
                deaths = int(row['Cumulative_deaths'])
                if min_deaths is None or deaths < min_deaths:
                    min_deaths = deaths
        else:
            deaths = int(row['Cumulative_deaths'])
            if min_deaths is None or deaths < min_deaths:
                min_deaths = deaths

    if min_deaths is None:
        raise HTTPException(status_code=404, detail="No deaths found within the provided date range.")

    return {"min_deaths": min_deaths}



@app.get("/avg_deaths")
async def get_average_deaths(
    country: str = Query(None, description="The name of the country."),
    min_date: str = Query(None, description="The minimum date."),
    max_date: str = Query(None, description="The maximum date.")
):
    """
    Finds the average number of deaths per day within the provided date range and country.

    Parameters:
    - `country`: The name of the country (optional).
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - The average number of deaths per day within the date range and country
    """
    total_deaths = 0
    num_days = 0

    for row in db:
        date_reported = datetime.datetime.strptime(row['Date_reported'], "%Y-%m-%d")
        if min_date and max_date:
            if datetime.datetime.strptime(min_date, "%Y-%m-%d") <= date_reported <= datetime.datetime.strptime(max_date, "%Y-%m-%d"):
                if country and row['Country'] == country:
                    deaths = int(row['Cumulative_deaths'])
                    total_deaths += deaths
                    num_days += 1
                elif not country:
                    deaths = int(row['Cumulative_deaths'])
                    total_deaths += deaths
                    num_days += 1
        else:
            if country and row['Country'] == country:
                deaths = int(row['Cumulative_deaths'])
                total_deaths += deaths
                num_days += 1
            elif not country:
                deaths = int(row['Cumulative_deaths'])
                total_deaths += deaths
                num_days += 1

    average_deaths_per_day = total_deaths / num_days

    return {"average_deaths_per_day": average_deaths_per_day}

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)

