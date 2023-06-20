""" 
Name : harikrishna mundra
Class : CS-4883 Software tools
Assignment : Assignment 7
Date : 06/20/2023
Description : This program scrapes the data from the website and saves it in a csv file.
professor : Dr. griffin 
"""

import PySimpleGUI as sg
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import json

# Function to get the current date
def currentDate(returnType='tuple'):
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)  # Add the year value
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]  # Add the year value
    else:
        return {
            'day': datetime.now().day,
            'month': datetime.now().month,
            'year': datetime.now().year
        }

     # Function to generate the  url for Scraping   
def genarateURL(month = None,day = None ,year = None,airportcode = None,filter = None):
    
    current_month,current_day,current_year = currentDate("tuple")
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

  # Load airport codes from JSON file
    with open('airport_better.json') as json_file:
        airport_codes = json.load(json_file)

    # Create the GUI's layout using drop-down boxes for user input
    layout = [
    [sg.Text('Month')],
    [sg.DropDown(list(range(1, 13)), default_value=month, size=(15, 5))],  
    [sg.Text('Day')],
    [sg.DropDown(list(range(1, 32)), default_value=day, size=(15, 5))],  
    [sg.Text('Year')],
    [sg.DropDown(list(range(2000, 2024)), default_value=year, size=(15, 5))],  
    [sg.Text('Code')],
    [sg.DropDown([code['icao'] for code in airport_codes], size=(15, 5))],  
    [sg.Text('Daily / Weekly / Monthly')],
    [sg.DropDown(['daily', 'weekly', 'monthly'], size=(10, 5))],  
    [sg.Submit(), sg.Cancel()]
]
# Create the window
    window = sg.Window('Weather Scraper', layout,size=(500,300))
# Create an event loop

    # Read the event that occurs Scraper', layout)
    event, values = window.read()   
    # End the program if the user closes the window or presses the Cancel button
    event, values = window.read()
    window.close()
    # Get the user input
    month = int(values[0]) 
    day = int(values[1])
    year = int(values[2])
    airportcode = values[3]
    filter = values[4]

    sg.popup(
    'You entered',
    f"Month: {month}, Day: {day}, Year: {year}, Code: {airportcode}, Filter: {filter}"
    
)
    return f"https://www.wunderground.com/history/{filter}/{airportcode}/date/{year}-{month:02d}-{day:02d}"

# Function to render the webpage using Selenium
def rendering(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)
    rawhtml = driver.page_source
    soup = BeautifulSoup(rawhtml, 'html.parser')
    return soup
#scraping the data using redering function
search_url = genarateURL()
weather_soup = rendering(search_url)
soup_container = weather_soup.find('lib-city-history-summary')
weather_data = soup_container.find_all('tbody', class_='ng-star-inserted')

# Write data to CSV file
outfile = 'temperature.csv'
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    
    # Write column headers
    writer.writerow(['date',
                     'actual_high_temp', 'histavg_high_temp', 'record_high_temp',
                     'actual_low_temp', 'histavg_low_temp', 'record_low_temp',
                     'actual_avg_temp', 'histavg_avg_temp', 'record_avg_temp',
                     'actual_precip', 'histavg_precip', 'record_precipitation'])
    
    row = []
    for dat in weather_data:
        # Loop through Actual, Historic Avg., Record
        for d in dat.find_all('tr', class_='ng-star-inserted'):
            # Loop through High Temp, Low Temp, etc.
            for k in d.find_all('td', class_='ng-star-inserted'):
                tmp = k.text.strip()  # Remove extra spaces
                row.append(tmp)
    
    # Write the date and temperature/precipitation data
    writer.writerow(['2020-12-31'] + row[:12])

# Read data from CSV file
filename = 'temperature.csv'
data = []
with open(filename, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
    print(data)

# Create GUI layout using table
layout = [
    [
        sg.Table(
            values=[['High Temp', data[1][1], data[1][2], data[1][3]],
                    ['Low Temp', data[1][4], data[1][5], data[1][6]],
                    ['Day Average Temp', data[1][7], data[1][8], data[1][9]],
                    ['Precipitation', data[1][10], data[1][11], data[1][12]]],
            font=('Arial', 20),
            headings=['temparature and precipitation', 'Actual', 'Historic Avg.', 'Record'],
            max_col_width=25,
            display_row_numbers=True,
            auto_size_columns=True,
            justification='center',
            num_rows=20,
            enable_events=True,
            key='-TABLE1-'
            
        )
    ],
    [sg.Button('Exit')]
]



# Create the window
window = sg.Window('CSV Data Viewer', layout, size=(500, 300))

# Event loop
while True:
    event, _ = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

# Close the window
window.close()

# References 
# https://data.library.virginia.edu/getting-started-with-web-scraping-in-python/
# https://pysimplegui.trinket.io/demo-programs#/tables/the-table-element
# https://github.com/rugbyprof/4883-Software-Tools/blob/master/Assignments/A07/get_weather.py
# https://github.com/rugbyprof/4883-Software-Tools/blob/master/Assignments/A07/gui.py


 

    




       
    



        
        
    







