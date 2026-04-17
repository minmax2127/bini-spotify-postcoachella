import scraper
import helper
from datetime import date
import os
import time
import pandas as pd
from tqdm import tqdm

## CONSTANTS
start_date = date(2026, 1, 1)
end_date = date(2026, 4, 17)
dates = helper.get_dates(start_date, end_date)

base_url = "https://charts.spotify.com/charts/view"
chart = "viral-global-daily"

def get_ranking(soup):
    '''collect the ranking per chart'''
    songs_table = soup.find("table")
    
    songs = []
    for i, tr in enumerate(songs_table.find_all("tr")):
        try:
            cells = tr.find_all(attrs={"data-encore-id": "tableCell"})
            main = cells[2].find_all(attrs={"data-encore-id":"overlayTrigger"})

            songs.append({
                "ranking": cells[1].find(attrs={"aria-label":"Current position"}).text,
                "title" : main[0].text,
                "artist" : main[1].text,
                "peak" : cells[3].text,
                "prev" : cells[4].text,
                "streak" : cells[5].text
            })

            
        except Exception as e:
            print("")

    return songs

def main():
    # create a folder of the csv
    directory = f"data/{chart}"
    os.makedirs(directory, exist_ok = True)

    # get record for each daily ranks
    for date in tqdm(dates):
        time.sleep(2) # Pause for every run to avoid being detected by the site
        driver = scraper.login_using_cookies()

        try: 
            url = os.path.join(base_url, chart, str(date))

            # get the page source
            soup = scraper.get_page_soup(url, driver = driver)

            # scrape the source for the ranking
            df = pd.DataFrame(get_ranking(soup))

            # save to csv
            df.to_csv(f"{directory}/{str(date)}.csv")
        except Exception as e:
            print(f"No data for {date}")

main()