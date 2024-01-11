<h1>OSU AI & Machine Learning: First Project of the Program</h1>

## Overview
<p><img src="https://github.com/jd-sterren/OSU_Project1/blob/main/Resources/img/output2-resampled.png" style="float: left; height:150px; margin: 5px; border: 1px;" alt="Prediction Analysis">
The project is designed to analyze crime patterns and trends using python in Jupyter
Notebook.  The data used is comprised of weather data, crime reports, and calls for service
(CFS) for the area of Canton, Ohio.  The analysis concludes by using the Prophet module
to predict future trends for allocated resources to be deployed appropriately.</p>

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

<h3>Summary Findings</h3>
<p>Overall crime trends are showing a decline, however, that doesn't mean specific types of crime are declining. There were outliers in 2021 near the beginning of the year were reported crime dropped dramatically then spiked just as dramatically months later.  Afternoons from 12:00 to 18:00 hours show to be the highest time of reported criminal activity and calls for service.</p>
<p>Focusing on specific crime, Domestic Violence appears to have some correlation to temperature as stated in a CNN article (Christensen, 2023).  There is a major decline in Domestic Violence for the months of February and November during the timeframe of the dataset however, the overall Domestic Violence trend is showing a slight increase into 2024 and 2025.</p>
<p>Covid-19 shut down may have stunted Theft reports in 2020 however, the following year jumped with a slow decline into 2023.  The month of June was the most reported thefts for 2022 followed by May and Aug.  The overall trend for Thefts is showing a decline into 2024.</p>
<p>Most overdoses to occur in the timeframe of the dataset was in 2022.  The months of July, May, and June were the highest months for people to overdose during the hours of 16:00 and 03:00.  While there is a slow decline into 2024, we can expect a monthly increase as we approach April 2024 based on Prophet’s predictions.</p>

<h4>References</h4>
<p>Pandas Categorical. (n.d.). Pandas. https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html</p>
<p>Canton Ohio Weather. (2023). OpenWeather. [Canton_Ohio_Weather.csv]. https://openweathermap.org/</p>
<p>Canton Crime Reports. (2023). Canton, Ohio Police Department. [reported_crime.xlsx]</p>
<p>Canton Calls for Service. (2023). Canton, Ohio Police Department. [cfs_data_Canton.xlsx]</p>
<p>Christensen, J. (2023). Hot under the collar? Heat can make you angry and even aggressive, research finds. <i>CNN Health</i>. https://www.cnn.com/2023/09/05/health/heat-anger-wellness/index.html#:~:text=In%20fact%2C%20research%20shows%20that,when%20temperatures%20climb%2C%20studies%20show.</p>