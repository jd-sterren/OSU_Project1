<h1>OSU AI & Machine Learning: First Project of the Program</h1>

## Overview
The project is designed to analyze crime patterns and trends using python in Jupyter
Notebook.  The data used is comprised of weather data, crime reports, and calls for service
(CFS) for the area of Canton, Ohio.  The analysis concludes by using the Prophet module
to predict future trends for allocated resources to be deployed appropriately.

<h2>Features</h2>
<p><b>Data Integration:</b> Integrates weather, crime, CFS, and demographic 
information specific to Canton, Ohio.<br/>
<b>Predictive Analytics:</b> Uses Prophet module to automate forecasts in 
overall crime, domestic violence, theft, and overdoses.<br/>
<b>Customizable Parameters:</b> Allows selection and weighting of different data points for tailored analysis.</p>

<p><b><i>Important Notes in Using weather_scraper.py</i></b></p>
<p>Weather Data Timeframe: The data abstracted only includes the time for the search date. Due to daylight savings, 
times are shifted (11:51 PM marks the start of the day during daylight savings, and 12:51 AM outside of it).
Data Processing: Use small data chunks, preferably one or two months at a time, to avoid issues 
with website pop-ups that can freeze the driver.</p>
<p><b>Selenium module is required using the following install</b></p>
<ul>
    <li>pip install selenium</li>
    <li>pip install selenium --upgrade</li>
    <li>pip install --upgrade webdriver-manager</li>
</ul>


<h3>References</h3>

Weather Data: [Canton, Ohio Police Department]
Crime Data: [Canton, Ohio Police Department]
Demographic Data: [Canton, Ohio Police Department]
