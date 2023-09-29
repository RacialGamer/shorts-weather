import requests
from os import system
from time import sleep

WEATHERBIT_API_KEY = 'YOUR_API_KEY'


# Gets the ip address for the ip api.
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address


def main():
    # Sends request to ip api to get location and country.
    ip_location = requests.get(f'https://ipapi.co/{get_ip_address()}/json/').json()
    location_data_and_api_key = {
        'city': ip_location.get('city'),
        'country': ip_location.get('country_name'),
        'key': WEATHERBIT_API_KEY
    }
    # Sends request to weatherbit api to get the temperature and description. Then parses the json response.
    api_response = requests.get("https://api.weatherbit.io/v2.0/forecast/daily", params=location_data_and_api_key)
    if api_response.status_code == 200:
        data = api_response.json()
        temperature = data['data'][0]['temp']
        description = data['data'][0]['weather']['description']
        print("24 HOURS FROM NOW")
        print("--------------------------------")
        print("Temperature:", temperature)
        print("Description:", description)
        print("--------------------------------")
        print("Can I wear shorts?")
        # You can customize the temperature, but generally its 20 celsius.
        if temperature > 20:
            print("Yes! :)")
        else:
            print("Nope :(")
    else:
        print("Failed to retrieve weather data. Status code:", api_response.status_code, "\nTrying again...")
        # Why does python not have a clear() function 💀?
        sleep(1)
        system('cls')
        main()


if __name__ == '__main__':
    main()
