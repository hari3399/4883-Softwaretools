
# Fast Api with Covid Data

**Description:** The COVID-19 Statistics API is a web API built with FastAPI that provides information about COVID-19 statistics for different countries and regions. The API retrieves data from a CSV file and offers various endpoints to access and filter the data based on specific criteria.

The main features of the API include:

1. Retrieving Total Cases and Deaths: The API allows users to retrieve the total number of COVID-19 cases and deaths for a given country, region, and year. Users can specify the country name, region code, and year as query parameters to filter the data and get the desired statistics.

2. Getting Unique Countries and Regions: The API provides endpoints to retrieve a list of unique countries and regions available in the dataset. This functionality helps users explore the available options and make informed queries.

3. Finding Country with Most Deaths: The API includes an endpoint that finds the country with the most deaths within a specific date range. Users can provide a minimum date and a maximum date to define the range. The API then searches the dataset and returns the country with the highest number of deaths within that period.

4. Finding Country with Least Deaths: Similarly, the API includes an endpoint to find the country with the least deaths within a given date range. Users can provide the minimum and maximum dates, and the API will return the country with the lowest number of deaths during that period.

5. Calculating Average Deaths per Day: The API also provides an endpoint to calculate the average number of deaths per day within a specified date range and country. Users can provide the country name, minimum date, and maximum date, and the API will calculate the average number of deaths per day based on the provided criteria.

## Endpoints and usage
The API provides the following endpoints:

#### Get Unique Countries
Endpoint: /countries/

Description: Returns a list of unique countries.

#### Get Unique Regions
Endpoint: /regions/

Description: Returns a list of unique regions.

#### Get Total Cases

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
    
#### Get Total Deaths


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
    

#### Get Country with maximum Deaths


    Finds the country with the most deaths.

    Parameters:
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - If `min_date` and `max_date` are provided, returns the country with the most deaths between the given date range.
    - If no date range is provided, returns the country with the most deaths overall.
    
#### Get Country with Minimum Deaths


    Finds the country with the least deaths.

    Parameters:
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - If `min_date` and `max_date` are provided, returns the country with the least deaths between the given date range.
    - If no date range is provided, returns the country with the least deaths overall.
    

#### Get Average Deaths

 
    Finds the average number of deaths per day within the provided date range and country.

    Parameters:
    - `country`: The name of the country (optional).
    - `min_date`: The minimum date to consider (optional).
    - `max_date`: The maximum date to consider (optional).

    Returns:
    - The average number of deaths per day within the date range and country
    
## Instructions

**clone the repository:**

- https://github.com/hari3399/4883-Softwaretools.git

**Navigate to the project directory:**

- cd A08

**Install the dependencies:**

- pip install -r requirements.txt

**Start the API server:**

- python api.py

- This will start the API server and make it available at http://localhost:5000.

**Access the API documentation:**

Open your web browser and go to http://localhost:5000/ to view the API documentation. The documentation provides detailed information about the available endpoints, parameters, and response formats.

**Interact with the API:**

- Refer to the API endpoints and their usage mentioned in the README file for examples and expected responses.For example, you can make a GET request to retrieve the total cases for a specific country:

- GET http://localhost:5000/cases?country=France You can modify the query parameters to retrieve data based on different criteria.

### References

- https://chat.openai.com/? used for some qutinons 
-

