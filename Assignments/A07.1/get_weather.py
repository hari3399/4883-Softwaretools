"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""


import json  
from generate_url import generateURL                                  
import PySimpleGUI as sg
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from datetime import datetime
import functools                                         # used to create a print function that flushes the buffer




flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
        """Returns the page source HTML from a URL rendered by ChromeDriver.
        Args:
            url (str): The URL to get the page source HTML from.
        Returns:
            str: The page source HTML from the URL.
            
        Help:
        https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
        """
        
       
        driver = webdriver.Chrome()  # run ChromeDriver
        flushprint("Getting page...")
        driver.get(url)                                             # load the web page from the URL
        flushprint("waiting 3 seconds for dynamic data to load...")
        time.sleep(3)                                               # wait for the web page to load
        flushprint("Done ... returning page source HTML")
        render = driver.page_source                                 # get the page source HTML
        driver.quit()                                               # quit ChromeDriver
        return render                                               # return the page source HTML
    
if __name__=='__main__':
    # Could be a good idea to use the buildWeatherURL function from gui.py
    url = generateURL()

    # Get the page source HTML from the URL
    page = asyncGetWeather(url)

    # Parse the HTML
    soup = BeautifulSoup(page, 'html.parser')

    # Find the appropriate tag that contains the weather data
    history = soup.find('lib-city-history-observation')

    # Write the parsed HTML to a file
    with open('parsed_weather.html', 'w') as file:
        file.write(history.prettify())

    # Print the parsed HTML
    print("Parsed HTML written to 'parsed_weather.html' file.")
    
    def parse_html_data():
      with open('parsed_weather.html') as f:
        table = f.read()
        soup = BeautifulSoup(table, 'html.parser')

        rows = soup.find_all('tr')
        head = soup.find_all('th')

        allData = []

        for row in rows:
            row_data = row.find_all('td')
            data = {}
            for i, td in enumerate(row_data):
                key = head[i].text.strip().replace(' ', '').replace('\n', '')
                value = td.text.strip().replace(' ', '').replace('\n', '')
                data[key] = value
            allData.append(data)

        return allData

# Get the parsed data
data = parse_html_data()

# Get table headings from the keys of the first non-empty dictionary
table_headings = list(data[1].keys())

# Convert data dictionaries to list of values
table_data = [[row.get(key, '') for key in table_headings] for row in data[1:]]

# Calculate the number of rows and columns in the table
num_rows = len(table_data)
num_cols = len(table_headings)

# Calculate the desired height and width of the table
table_height = min(num_rows + 1, 25)  
table_width = min(num_cols * 15, 500) 

# Create the layout with the adjusted table element
layout = [
    [sg.Table(
        headings=table_headings,
        values=table_data,
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        display_row_numbers=True,
        num_rows=table_height,
        col_widths=[15] * num_cols,  # Adjust the column widths as needed
        size=(table_width, table_height * 25)  # Adjust the size as needed
    )]
]

# Create the window
window = sg.Window('Weather data', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

# Close the window
window.close()


    

    


   