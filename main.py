import requests

url_template_main = 'https://wttr.in/{}'
# url_template_dvmn = 'http://wttr.dvmn.org/{}'

cities = ['London', 'SVO', 'Череповец']
payload = {
    "lang": "ru",
    "M": "",  # show wind speed in m/s. Not necessary using "m"
    "m": "",  # metric (SI) units
    "n": "",  # narrow version (only day and night)
    "q": "",  # quiet version
    "T": ""  # switch terminal sequences off (no colors)
}
for city in cities:
    url_place = url_template_main.format(city)

    response = requests.get(url_place, params=payload)
    response.raise_for_status()

    print(response.text)
