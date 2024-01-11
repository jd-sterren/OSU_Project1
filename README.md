<h1>OSU AI Machine Learning: First Project of the Program</h1>

## Overview
The project is designed to analyze crime patterns and trends using python in Jupyter
Notebook.  The data used is comprised of weather data, crime reports, and calls for service
(CFS) for the area of Canton, Ohio.  The analysis concludes by using the Prophet module
to predict future trends for allocated resources to be deployed appropriately.
<h2>Features</h2>
Data Integration: Integrates weather data, crime data, and demographic information specific to Canton, Ohio.
Predictive Analytics: Uses supervised machine learning algorithms to show crime occurrences based on weather conditions.
Customizable Parameters: Allows selection and weighting of different data points for tailored analysis.
User-Friendly Interface: Designed for ease of use among those with basic programming and data analysis knowledge.
Important Notes
Data Timeframe: The data abstracted only includes the time for the search date. Due to daylight savings, 
times are shifted (11:51 PM marks the start of the day during daylight savings, and 12:51 AM outside of it).
Data Processing: Use small data chunks, preferably one or two months at a time, to avoid issues 
with website pop-ups that can freeze the driver.
## Selenium Requirement: The program requires Selenium for web scraping. Install or update Selenium as follows:

pip install selenium
pip install selenium --upgrade
pip install --upgrade webdriver-manager

Data Sources
Weather Data: [Canton, Ohio Police Department]
Crime Data: [Canton, Ohio Police Department]
Demographic Data: [Canton, Ohio Police Department]
