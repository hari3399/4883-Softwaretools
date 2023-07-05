# Web Scraping

this project create a Python program that scrapes weather data from a website and displays it using the PySimpleGUI library. The program will allow users to specify the date and location for which they want to retrieve the weather data.

## Full Description

1. used web scraping techniques to extract weather data from a website. The BeautifulSoup library is used to parse the HTML content, and the Selenium library is used to interact with the website and retrieve dynamic content if necessary.

2. The program will prompt the user to enter the date and location for which they want to retrieve the weather data. We created a GUI using PySimpleGUI to make it user-friendly. The GUI will include input fields for the date and a drop-down menu to select the location.

3. Once the user submits the form, the program will construct the URL with the provided date and location. This URL will be used to retrieve the weather data from the website.

4. The program will perform web scraping on the website, extracting the desired weather information such as high temperature, low temperature, average temperature, and precipitation etc.

5. The scraped weather data will be formatted and displayed in a table using PySimpleGUI.

## files

| No | file name                | Description                |
| :--| :------------------------| :------------------------- |
|  1 |[GenerateFamilyTreeDOT.py](./generateFamilyTreeDOT.py) | python file that creates dot file |
|  2 | `generateFamilyTreeCSV.py` | python file that creates input csv file| 
| 3  |   `family_tree.csv` | input family tree file|
|4| `family_tree.dot`| dot output file created by script|
|5| ` family_tree.png`| output familytree image|


## Program execution instructions
1. Install the required libraries: PySimpleGUI, BeautifulSoup, selenium. You can install them using pip, the package installer for Python. Open a command prompt or terminal and run the following commands:  pip install PySimpleGUI
                     pip install beautifulsoup4
                     pip install selenium

2. Make sure that all the provided  script files are placed in the same directory. If you're using a different name for the Chrome WebDriver executable file or the JSON file, you'll need to update the import statements accordingly.

3. Run the file named get_weather.py.

## Sample Url1 input&output screenshots

<img width="495" alt="url1_input" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/b4c836ac-58fe-48bf-ae1b-b4521d687b09">
  
<img width="832" alt="url1_output" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/96081bf1-3bff-4e1c-82c8-ddb0cea127da">

## Sample Url2 input&output screenshots

<img width="502" alt="url2_input" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/23931ce3-45e7-4259-ae23-3bacadc8863c">

<img width="816" alt="url2_output" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/9ae96089-98af-4f42-9338-31a9947f5adb">

## Sample Url3 input&output screenshots

<img width="506" alt="url3_input" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/7cf7b1e9-be56-4f74-a693-6f9fbe681fbc">

<img width="821" alt="url3_output" src="https://github.com/hari3399/4883-Softwaretools/assets/123417887/9c8e3f12-2477-4dbd-80fd-aa4df16185a6">


## Acknowledgements

 https://data.library.virginia.edu/getting-started-with-web-scraping-in-python/
 
 https://pysimplegui.trinket.io/demo-programs#/tables/the-table-element
 
 https://github.com/rugbyprof/4883-Software-Tools/blob/master/Assignments/A07/get_weather.py
  
 https://github.com/rugbyprof/4883-Software-Tools/blob/master/Assignments/A07/gui.py






