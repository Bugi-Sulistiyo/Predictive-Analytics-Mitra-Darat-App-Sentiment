# Import the necessary packages
from google_play_scraper import reviews, Sort   # package for scrapping from google play store
import csv                                      # package for handling csv files
import os                                       # package for handling file system

os.mkdir("./data")

# configure the search
scrapped_data, _ = reviews(
    "ngi.muchi.hubdat", # app id
    lang="id",          # language (Indonesian)
    country="id",       # country   (Indonesia)
    sort=Sort.NEWEST,   # sort by newest
    count=5000          # number of reviews to scrap
)

# Save the data to a CSV file
with open("./data/mitradarat_reviews.csv", mode="w", newline="", encoding="utf-8") as file:
    field_names = list(scrapped_data[0].keys())
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(scrapped_data)

print("Done")