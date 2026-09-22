import requests
from config import WEATHER_API_KEY, CITY, STATE, COUNTRY


def get_weather():
    """
    Gets the current weather from OpenWeatherMap
    and returns it as formatted text for the smart mirror.
    """

    # Check if API key has been configured
    if not WEATHER_API_KEY or WEATHER_API_KEY == "YOUR_API_KEY_HERE":
        return "Weather API key not configured."

    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": f"{CITY},{STATE},{COUNTRY}",
        "appid": WEATHER_API_KEY,
        "units": "imperial"
    }

    try:
        response = requests.get(
            url,
            params=parameters,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        # Get weather information
        temperature = round(data["main"]["temp"])
        feels_like = round(data["main"]["feels_like"])
        humidity = data["main"]["humidity"]

        description = (
            data["weather"][0]["description"]
            .title()
        )

        # Format information for the mirror
        weather_text = (
            f"{CITY}, {STATE}\n\n"
            f"{temperature}°F\n"
            f"{description}\n\n"
            f"Feels Like: {feels_like}°F\n"
            f"Humidity: {humidity}%"
        )

        return weather_text

    except requests.exceptions.Timeout:
        return "Weather request timed out. Try again later Pelon."

    except requests.exceptions.ConnectionError:
        return "Unable to connect to weather service. Fix your shit"

    except requests.exceptions.HTTPError:
        return "Weather service returned an error."

    except (KeyError, TypeError, ValueError):
        return "Unable to read weather data."

    except requests.exceptions.RequestException:
        return "Unable to retrieve weather."