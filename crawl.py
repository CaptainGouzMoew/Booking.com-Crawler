from pathlib import Path
import pandas as pd
import pandas as pd
from scrapeComments import ReviewScrape
from hotel_nameCrawl import BookingScraper
from crawl_element import get_hotel_dest_ID, get_hotel_id, get_hotel_rating
from city import cities


output_dir = Path("output_reviews")
output_dir.mkdir(exist_ok=True)

hotel_list_dir = Path("hotel_list") 
hotel_list_dir.mkdir(exist_ok=True)  


for city in cities:
    print(f"\n📍 Processing city: {city}")

    city_filename = output_dir / f"{city.replace(' ', '_')}.csv"
    hotel_filename = hotel_list_dir / f"{city.replace(' ', '_')}.csv"

    # Load previously saved reviews (if any)
    if city_filename.exists():
        existing_df = pd.read_csv(city_filename)
        processed_links = set(existing_df['Country'].unique())
        print(existing_df.head())