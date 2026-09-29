# Basic Weather App – Python

## Project Overview

This project is a simple command-line Weather Application developed as part of the Oasis Infobyte Python Programming Internship.

The application allows the user to enter a city name and fetches real-time weather information using the OpenWeatherMap API.

## Features

* Accepts city name from the user
* Validates empty city input
* Fetches real-time weather data
* Displays temperature in Celsius (°C)
* Displays temperature in Fahrenheit (°F)
* Displays humidity percentage
* Displays weather condition
* Displays wind speed
* Handles city-not-found errors
* Handles invalid API key errors
* Handles network connection errors
* Handles request timeout errors

## Technologies Used

* Python
* Requests
* JSON
* OpenWeatherMap API

## Installation

Install the required Python package:

```bash
pip install -r requirements.txt
```

## API Key Setup

This project requires an OpenWeatherMap API key.

Open `weather_app.py` and add your API key:

```python
API_KEY = "YOUR_API_KEY"
```

Do not share your API key publicly or upload it directly to a public GitHub repository.

## How to Run

Run the following command:

```bash
python weather_app.py
```

Enter a city name when prompted.

Example:

```text
Enter city name: Trivandrum
```

## Example Output

```text
--- Weather Information ---
City: Trivandrum
Temperature: XX.X °C
Temperature: XX.X °F
Humidity: XX%
Weather: Clear Sky
Wind Speed: X.X m/s
```

## Error Handling

The application handles the following errors:

* Empty city input
* City not found
* Invalid API key
* Network connection failure
* Request timeout

## Project Structure

```text
Python-Beginner-Task2-BasicWeatherApp/
│
├── weather_app.py
├── requirements.txt
└── README.md
```

## Privacy and API Note

The application sends the entered city name to the OpenWeatherMap API to retrieve weather information. An API key is required to access the weather service.

The API key should be kept private and should not be committed to a public repository.
