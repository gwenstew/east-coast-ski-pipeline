import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
import json
import time
import datetime
import random


base_url = "https://www.onthesnow.com"

PA_resorts = ["blue-mountain-ski-area", "bear-creek-mountain-resort", "big-boulder", "camelback-mountain-resort",
              "elk-mountain-ski-resort", "montage-mountain", "spring-mountain-ski-area", "jack-frost", "big-bear"]


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
}


def extract_resort_data(state, resort):

    full_url = f"{base_url}/{state}/{resort}/skireport"

    try:
        response = requests.get(full_url, headers=HEADERS)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find("script", id="__NEXT_DATA__")

        if script is None:
            print(f"No script data found for {resort}")
            return None
        
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
            "snowfall_72h": resort_data["snow"]["last72"]
        }

        return resort_info
    
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"Failed to access page for {resort}. Error: {e}")
        return None


def main():
    results = []
    failed_resorts = []

    for resort in PA_resorts:
        data = extract_resort_data("pennsylvania", resort)

        if data:
            #add meta data
            data['resort_name'] = resort
            data['state'] = "pennsylvania"
            data['scraped_at'] = datetime.now()
            results.append(data)
        else:
            failed_resorts.append(resort)
        
        # mimic user behavior to avoid getting blocked
        time.sleep(random.uniform(1,5))

    print(f"\nSuccessfully scraped: {len(results)} resorts")
    if failed_resorts:
        print(f"Failed resorts: {failed_resorts}")

    # TODO: load results into postgres
    # load_to_postgres(results)

    return results


if __name__ == "__main__":
    main()
