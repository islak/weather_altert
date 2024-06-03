import requests

def check_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return weather, temperature
    else:
        print("Failed to fetch weather data.")
        return None, None

def main():
    api_key = "369f6448dfc3601def7afa4ac2a8227b"
    city = "Houston"

    weather, temperature = check_weather(api_key, city)

    if weather:
        if "rain" in weather.lower():
            print("There's a chance of rain today in Houston.")
        elif "thunderstorm" in weather.lower():
            print("A thunderstorm is expected today in Houston. Stay indoors.")
        else:
            print("No severe weather alerts for Houston today.")

if __name__ == "__main__":
    main()
