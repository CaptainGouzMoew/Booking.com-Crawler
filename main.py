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
        processed_links = set(existing_df['Page link'].unique())
        df_all = [existing_df]
        print(f"✅ Found existing data for city: {len(processed_links)} hotels already saved.")
    else:
        processed_links = set()
        df_all = []

    hotel_scrape = BookingScraper(city=city)
    df = hotel_scrape.get_hotel_info()
    refers = df['Page link']

    for i, refer in enumerate(refers): # Hotel part
        if refer in processed_links:
            print(f"⏩ Already processed: {refer}")
            continue

        try:
            hotel_rating = get_hotel_rating(refer)
            hotel_ID = get_hotel_id(refer)
            dest_ID = get_hotel_dest_ID(refer)

            if None in [hotel_rating, hotel_ID, dest_ID]:
                print(f"⚠️ Skipping (missing data): {refer}")
                continue

            review_scraper = ReviewScrape(
                referal=refer,
                hotel_ID=hotel_ID,
                dest_ID=dest_ID,
                hotel_rating=hotel_rating
            )

            df_reviews = review_scraper.scrapeReview()
        
            if not df_reviews.empty:
                df_all.append(df_reviews)
                print(f"✅ Scraped: {refer}")
            else:
                print(f"⚠️ No reviews found: {refer}")

            # Save immediately after each hotel
            pd.concat(df_all, ignore_index=True).to_csv(city_filename, index=False)

        except Exception as e:
            print(f"❌ Error scraping hotel at {refer}: {e}")
            continue
