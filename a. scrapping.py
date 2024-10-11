# Import the necessary packages
from google_play_scraper import reviews, Sort
import csv
import os

os.mkdir("./data")

# configure the search
scrapped_data, _ = reviews(
    "ngi.muchi.hubdat",
    lang="id",
    country="id",
    sort=Sort.NEWEST,
    count=5000
)

# Save the data to a CSV file
with open("./data/mitradarat_reviews.csv", mode="w", newline="", encoding="utf-8") as file:
    field_names = list(scrapped_data[0].keys())
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(scrapped_data)

print("Done")