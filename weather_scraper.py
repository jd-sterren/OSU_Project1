# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 01:30:30 2023
@author: James Dreussi

NOTES: The data abstracted only has the time for the search date.  The time is
affected by daylight savings and as such, will return 11:51 PM as the start to
the day.  Outside the savings time, the data will show 12:51 as the start to
the day.
If you haven't installed selenium use pip install selenium, else, use updates

pip install selenium --upgrade
pip install --upgrade webdriver-manager

-- USE SMALL DATA CHUNKS PERHAPS ONE OR TWO MONTHS AT A TIME --
The website likes to create pop up ads which can cause the driver to freeze.
"""
# Import the need modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime
import time

# Initiate webdriver
driver = webdriver.Chrome()

# Initiate Date to search and DataFrame
weather_df = pd.DataFrame()

# This file works backwards to download data.
search_date = '2022-10-31' # Start Date of going backward
end_date = '2022-08-01'
excel_file_name = f"Resources/weather_data_{end_date}_{search_date}.xlsx"
base_url = "https://www.wunderground.com/history/daily/us/oh/green/KCAK/date/"

# Create the definition to loop over
def gather_weather(base_url, search_date):
    # Go to the page
    driver.get(base_url + search_date)

    time.sleep(2)
    # Gather the data by xpath
    # Look for the element by xpath found through the inspect tool of the browser
    weather_data = driver.find_element(By.XPATH,'//*[@id="inner-content"]/div[2]/div[1]/div[5]/div[1]/div/lib-city-history-observation/div/div[2]/table')

    # Returns outterHTML attribute so pd.read_html can recognize html
    formatted = weather_data.get_attribute('outerHTML')
    formatted = pd.read_html(formatted)

    # Create the dataframe to work with
    df = pd.DataFrame(formatted[0]).dropna().reset_index(drop=True)

    # Degree sign needs removed from all fields
    df = df.apply(lambda x: x.str.replace("°",""))

    # Rename Time column to ds so we can add the search_date
    df = df.rename(columns={"Time":"ds"})

    # Add search date to the time and then convert to datetime
    df['ds'] = search_date + ' ' + df['ds'].astype(str)
    df = df.astype({"ds":"datetime64[ns]"}, errors='raise')

    return df


# Start Loop Here
while search_date >= end_date:
    df2 = gather_weather(base_url, search_date)
    if weather_df.shape[0] == 0:
        weather_df = df2
    else:
        weather_df = pd.concat([weather_df, df2], axis="rows", join="inner").reset_index(drop=True)

    # Sequence day minus 1 by taking current string of date and converting to dt
    # Then subtracting it by 1 day followed by converting back to string for url
    search_date = datetime.strptime(search_date,f"%Y-%m-%d") - pd.Timedelta(days=1)
    search_date = search_date.strftime(f"%Y-%m-%d")
    print(search_date)

# Export the dataframe to an excel document for preservation
weather_df.to_excel(excel_file_name, index=False, header=True)

# Quit the Driver
driver.close()
