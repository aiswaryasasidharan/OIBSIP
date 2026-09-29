import requests

API_KEY = "5de72d572aa49c9f8e4f0b5c9dd08b9e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather():
    city = input("Enter city name: ").strip()

    if not city:
        print("Error: City name cannot be empty.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 401:
            print("Error: Invalid API key.")
            return

        if response.status_code == 404:
            print("Error: City not found.")
            return

        response.raise_for_status()

        data = response.json()

        temperature_c = data["main"]["temp"]
        temperature_f = (temperature_c * 9 / 5) + 32
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n--- Weather Information ---")
        print(f"City: {data['name']}")
        print(f"Temperature: {temperature_c:.1f} °C")
        print(f"Temperature: {temperature_f:.1f} °F")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {condition.title()}")
        print(f"Wind Speed: {wind_speed} m/s")

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the weather service.")

    except requests.exceptions.RequestException:
        print("Error: Unable to fetch weather information.")


if __name__ == "__main__":
    get_weather()