# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup as bs
# import pandas as pd
# import time

# def is_number(s):
#     if s[0] == '<':
#         return True
#     try:
#         float(s)
#         return True
#     except:
#         return False


# # Set up Chrome options to run in headless mode
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Enable headless mode
# chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
# chrome_options.add_argument("--no-sandbox")  # Bypass OS security model (useful for running in Docker)
# chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# # Initialize the Selenium WebDriver with options
# driver = webdriver.Chrome(options=chrome_options)

# # Initialize the Selenium WebDriver (e.g., Chrome)
# driver = webdriver.Chrome()  # Make sure you have the appropriate WebDriver installed

# # Open the webpage
# url = 'https://fdc.nal.usda.gov/fdc-app.html#/food-details/1750340/nutrients'
# driver.get(url)

# # Wait for the page to load dynamically
# time.sleep(5)  # Adjust time based on your internet speed and the complexity of the page

# # Get the rendered HTML content
# html = driver.page_source

# # Parse the HTML with BeautifulSoup
# soup = bs(html, 'html.parser')

# # Find the table
# table = soup.find('table', {'id': 'nutrients-table'})  # Adjust the attributes as needed

# if table:
#     table_data = []

#     # Iterate through table rows
#     for row in table.find_all('tr'):
#         # Extract cell data (td elements)
#         cells = row.find_all('td')
#         # Extract text from each cell and store only the first three columns
#         row_data = [cell.text.strip() for cell in cells[:3]]
#         table_data.append(row_data)

#     # Convert the data to a pandas DataFrame
#     df = pd.DataFrame(table_data)

#     # Remove rows where any of the columns is NaN (typically the first row is header or empty)
#     df = df[~((df[1] == '0') | ("FA" in df[0]) | (is_number(df[0]))| (df[2].isin(['kJ'])))]
#     df.dropna(axis=0, how='any', inplace=True)

#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', None)
#     pd.set_option('display.max_colwidth', None)
#     pd.set_option('display.expand_frame_repr', False)
#     print(df)
# else:
#     print("Table not found!")

# # Close the browser
# driver.quit()

import requests

# Perform a GET request
response = requests.get('https://api.nal.usda.gov/fdc/v1/food/######?api_key=DEMO_KEY')

# Print the response status code
print(f"Status Code: {response.status_code}")

# Print the response content
print(response.text)