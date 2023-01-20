# Weather App
Know live weather conditions on a single click

# The Problem
Users can get too busy at work or at home to check the current weather conditions for severe weather. Many of the free weather software programs have too many pop ups or unwanted software tied to them like weather bug.Getting confusing information on weather warnings from inaccurate sources.Also every application has different information of weather of the same location at the same time.The reason is that there are many sources such as newspaper,television,radio,etc which provide weather updates which often differ. One cannot rely on a particular source. Also, information such as humidity,wind speed ,pressure is seldom provided on these sources. If a user needs information on above mentioned parameters then he/she needs to visit various sources for that, which is a tedious job.

# The Solution
Our responsive website "The Weather Detector", which:
- Provides users with accurate information regarding the climate of the city they input.
- Displayed climate parameters includes temperature, humidity, wind speed, pressure, sunrise time, sunset time, co-ordinates and country-code of the location.
- Accurately shows the weather of a given region.

# Technologies used:
- HTML
- CSS
- Python
- Django
- sqlite3
- pip

# API used to fetch weather information
[Open Weather API](https://openweathermap.org/api)

# Challenges we ran into
- Displaying time in readable format - Used "datetime" module to convert json timestamp

# Getting Started

## Prerequisites
- Install Python - Refer to https://www.python.org/downloads/ to install python

## Cloning the repository locally
- Clone the project on localhost
```bash
git clone https://github.com/Devang-Shah-49/weather-app-django.git
```
- Move to the project directory
```bash
cd .\weather-app-django\
```
- Install required python packages
```bash
pip install numpy pandas matplotlib django pillow pathlib datetime
```
## Running the website locally
- When you have all the dependencies installed, run the migration to create tables for the app in the new database.
```bash
python manage.py migrate
```
- When the migrations complete, run the project.
```bash
python manage.py runserver
```
-  Open http://127.0.0.1:8000/ in a web browser.


# Screenshots of the website
![image](https://user-images.githubusercontent.com/80088008/213724537-cf8d952c-bfca-4b3b-8ecc-d6226f462e2c.png)
![image](https://user-images.githubusercontent.com/80088008/213724603-f193076b-540e-4100-9c69-3f6d9255f26a.png)
![image](https://user-images.githubusercontent.com/80088008/213724792-11b9be74-908a-4666-b9cd-915baf0f67bf.png)


# Bug Reporting/Feature Request
- Feel free to [open an issue](https://github.com/Devang-Shah-49/weather-app-django/issues) on GitHub if you find any bug or to request any additional features.
- Connect with me on [LinkedIn](https://www.linkedin.com/in/devang-shah-63a29b210). I would love ❤️️ to help!
