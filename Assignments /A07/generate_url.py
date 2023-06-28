import json
import PySimpleGUI as sg
from datetime import datetime


def currentDate(returnType='tuple'):
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


# Function to generate the URL for Scraping
def generateURL(month=None, day=None, year=None, airportcode=None, filter=None):
    current_month, current_day, current_year = currentDate("tuple")
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
    window = sg.Window('Weather Scraper', layout, size=(500, 300))

    # Create an event loop
    event, values = window.read()

    # End the program if the user closes the window or presses the Cancel button
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        window.close()
        sys.exit()

    # Get the user input
    month = int(values[0])
    day = int(values[1])
    year = int(values[2])
    airportcode = values[3]
    filter = values[4]

    # Print the values entered by the user
    print("You entered:")
    print(f"Month: {month}, Day: {day}, Year: {year}, Code: {airportcode}, Filter: {filter}")

    # Close the window
    window.close()

    return f"https://www.wunderground.com/history/{filter}/{airportcode}/date/{year}-{month:02d}-{day:02d}"



