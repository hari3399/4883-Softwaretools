from bs4 import BeautifulSoup
import PySimpleGUI as sg

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

# Convert data dictionaries to list of values with error handling
table_data = [[row.get(key, '') for key in table_headings] for row in data[1:]]

# Create the layout with the table element
layout = [
    [sg.Table(
        headings=table_headings,
        values=table_data,
        max_col_width=25,
        auto_size_columns=True,
        justification='center',
        display_row_numbers=True,
        num_rows=min(25, len(data) - 1)
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