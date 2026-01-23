#steps for scraping OnTheSnow for resort data/ snow reports

# use requests to get a response object response.text will hold the html content as a string
#   will need to use a User-Agent as a header for access probably

# use the beautiful soup html parser to parse through the html content

#to extract the data i will need to determine the names for the divs/sections that the data is stored in
import requests
from bs4 import BeautifulSoup
import json


base_url = "https://www.onthesnow.com/vermont/killington-resort/skireport"

PA_resorts = ["blue-mountain-ski-area", "bear-creek-mountain-resort", "big-boulder", "camelback-mountain-resort",
              "elk-mountain-ski-resort", "montage-mountain", "spring-mountain-ski-area", "jack-frost", "big-bear"]


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(base_url, headers=HEADERS)

soup = BeautifulSoup(response.text, 'html.parser')

script = soup.find("script", id="__NEXT_DATA__")

data = json.loads(script.string)

resort_data = data["props"]["pageProps"]["fullResort"]


resort_info = {
    "lifts_open": resort_data["lifts"]["open"],
    "lifts_total": resort_data["lifts"]["total"],
    "runs_open": resort_data["runs"]["open"],
    "runs_total": resort_data["run"]["total"],
    "base_depth_cm": resort_data["snow"]["base"],
    "summit_depth_cm": resort_data["snow"]["summit"],
    "snowfall_24h": resort_data["snow"]["last24"],
    "snowfall_72h": resort_data["snow"]["last72"],

}

