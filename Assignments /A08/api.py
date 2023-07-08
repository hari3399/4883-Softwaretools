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

def geting_total_cases(db, country=None, region=None, year=None):
    total_cases = 0

    for row in db:
        if (country and row['Country'] == country) or (region and row['WHO_region'] == region):
            if year and row['Date_reported'].startswith(str(year)):
                total_cases += int(row['New_cases'])
            elif not year:
                total_cases += int(row['New_cases'])
        elif not country and not region:
            if year and row['Date_reported'].startswith(str(year)):
                total_cases += int(row['New_cases'])
            elif not year:
                total_cases += int(row['New_cases'])

    return total_cases



def geting_total_deaths(db, country=None, region=None, year=None):
    total_deaths = 0

    for row in db:
        if (country and row['Country'] == country) or (region and row['WHO_region'] == region):
            if year and row['Date_reported'].startswith(str(year)):
                total_deaths += int(row['New_deaths'])
            elif not year:
                total_deaths += int(row['New_deaths'])
        elif not country and not region:
            if year and row['Date_reported'].startswith(str(year)):
                total_deaths += int(row['New_deaths'])
            elif not year:
                total_deaths += int(row['New_deaths'])

    return total_deaths

def finding_country_with_highest_deaths(db):
    country_deaths = {}

    for row in db:
        country = row['Country']
        deaths = int(row['New_deaths'])

        if country in country_deaths:
            country_deaths[country] += deaths
        else:
            country_deaths[country] = deaths

    highest_deaths = max(country_deaths.values())
    country_with_highest_deaths = [country for country, deaths in country_deaths.items() if deaths == highest_deaths]

    return country_with_highest_deaths[0], highest_deaths


def find_country_with_minimum_deaths(db):
    country_deaths = {}

    for row in db:
        country = row['Country']
        deaths = int(row['New_deaths'])

        if country in country_deaths:
            country_deaths[country] += deaths
        else:
            country_deaths[country] = deaths

    minimum_deaths = min(country_deaths.values())
    country_with_minimum_deaths = [country for country, deaths in country_deaths.items() if deaths == minimum_deaths]

    return country_with_minimum_deaths[0], minimum_deaths


def calculate_average_deaths(db, country=None, start_date=None, end_date=None):
    filtered_data = db

    if country:
        filtered_data = [row for row in filtered_data if row['Country'] == country]

    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        filtered_data = [row for row in filtered_data if
                         datetime.strptime(row['Date_reported'], '%Y-%m-%d').date() >= start_date]

    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        filtered_data = [row for row in filtered_data
                         if datetime.strptime(row['Date_reported'], '%Y-%m-%d').date() <= end_date]

    total_deaths = sum(int(row['New_deaths']) for row in filtered_data)
    num_days = len(filtered_data)
    average_deaths = total_deaths / num_days if num_days > 0 else 0

    return average_deaths



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


@app.get("/cases")
async def get_cases(
    country: str = Query(None, description=" country name"),
    region: str = Query(None, description="who code"),
    year: int = Query(None, description="year")
):
   ''' this route gives total cases in the country ,region and year according to input provided.add.
     
     input paramenters :   - Country name 
                           - WHO region code 
                           - year 
                           
                           
    returns :  
    
     - if no input in provided it will return total cases for all the avilable countries
     
     -  if country name prvided it wil return total cases in that country
     
     -  if region is provided it will return total cases in that region 
     
     - if country name or  region provided along with year it will return total cases for that country or region in that particular year will return 

    '''
    
    total_cases = geting_total_cases(db, country, region, year)
    
    return {"total_no_of _cases": total_cases}


@app.get("/deaths")
async def get_deaths(
    country: str = Query(None, description=" country name"),
    region: str = Query(None, description="who code"),
    year: int = Query(None, description="year")
):

      ''' this route gives total deaths in the country ,region and year according to input provided.
     
     input paramenters :   - Country name 
                           - WHO region code 
                           - year 
                           
                           
    returns :  
    
     - if no input in provided it will return total deaths for all the avilable countries
     
     -  if country name prvided it wil return total deaths in that country
     
     -  if region is provided it will return total deaths  in that region 
     
     - if country name or  region provided along with year it will return total deaths for that country or region in that particular year will return 

    '''

    total_deaths = geting_total_deaths(db, country, region, year)
    
    return {"total_no_of_deaths": total_deaths }


@app.get("/highest_deaths")
async def geting_highest_deaths():
    country, deaths = finding_country_with_highest_deaths(db)

    return {
        
        "country": country,
        "deaths": deaths
    }
    
    


@app.get("/minimum_deaths")
async def get_minimum_deaths():
    country, deaths = find_country_with_minimum_deaths(db)

    return {
        
        "country": country,
        "deaths": deaths
    }



@app.get("/average_deaths")
async def get_average_deaths(
    
    country: str = Query(None, description="Country name"),
    start_date: str = Query(None, description="Start date YYYY-MM-DD"),
    end_date: str = Query(None, description="End date YYYY-MM-DD")
):
    average_deaths = calculate_average_deaths(db, country, start_date, end_date)

    return {
        "country": country,
        "start_date": start_date,
        "end_date": end_date,
        "average_deaths": average_deaths
    }

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True)
    
