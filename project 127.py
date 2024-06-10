from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars"  # URL of the NASA Exoplanet Catalog

browser = webdriver.Chrome()  # Initializing Chrome WebDriver
browser.get(START_URL)  # Opening the specified URL in the browser

time.sleep(2)  # Adding a delay to allow the page to fully load

scrap_data = []  # List to store extracted planet data

def scrape():
   
        

        # BeautifulSoup Object
    soup = BeautifulSoup(browser.page_source, "html.parser")  # Creating a BeautifulSoup object for the current page
    brightstartable=soup.find("table",attrs={"class","wikitable"})
    tableBody=brightstartable.find("tbody")
    tableRows=tableBody.find_all("tr")
    for row in tableRows:
        tableColumns=row.find_all("td")
        tempList=[]
        for colData in tableColumns:
            print(colData.text)
            data = colData.text.strip()
            tempList.append(colData)

        scrap_data.append(tempList)  
        print(scrap_data) 





       

# Calling the scraping method
scrape()
star_data=[]

for i in range(0,len(scrap_data)):
    Star_names = scrap_data[i][1]
    Distance = scrap_data[i][3]
    Mass = scrap_data[i][5]
    Radius = scrap_data[1][6]
    Lum = scrap_data[i][7]

    required_data = [Star_names,Distance, Mass, Radius, Lum]
    star_data.append(required_data)
# Define Header for DataFrame
headers = ["Star_names", "Distance", "Mass", "Radius", "Luminosity"]

# Create pandas DataFrame from the extracted data
star_df_1 = pd.DataFrame(star_data, columns=headers)

# Convert DataFrame to CSV and save to file
star_df_1.to_csv('scraped_data1.csv', index=True, index_label="id")  # Saving the DataFrame as a CSV file


