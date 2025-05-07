from pathlib import Path
import pandas as pd
from scr.booking_scraper.scrapeComments import ReviewScrape
from scr.booking_scraper.hotel_nameCrawl import BookingScraper
from scr.booking_scraper.crawl_element import element_crawl
from scr.booking_scraper.city import cities


output_dir = Path("output_reviews")
output_dir.mkdir(exist_ok=True)

hotel_list_dir = Path("hotel_list") 
hotel_list_dir.mkdir(exist_ok=True)  

finished_list_dir = Path("processed_hotel") 
finished_list_dir.mkdir(exist_ok=True)  

MAX_HOTELS_PER_CITY = 200

for city in cities:
    print(f"\n📍 Processing city: {city}")

    city_filename = output_dir / f"{city.replace(' ', '_')}.csv"
    hotel_filename = hotel_list_dir / f"{city.replace(' ', '_')}.csv"

    # Load previously saved reviews (if any)
    if hotel_filename.exists():
        existing_df = pd.read_csv(hotel_filename)
        processed_links = set(existing_df['Page link'].unique())
        df_all = [existing_df]
        already_processed = len(processed_links)
        print(f"✅ Found existing data: {already_processed} hotels already saved.")
        if already_processed >= MAX_HOTELS_PER_CITY:
            print(f"🚫 Skipping city: {city} (already hit {MAX_HOTELS_PER_CITY})")
            continue
    else:
        processed_links = set()
        df_all = []
        already_processed = 0

    hotel_scrape = BookingScraper(city=city)
    df = hotel_scrape.get_hotel_info()
    refers = df['Page link']
    
    new_hotels_scraped = 0

    for i, refer in enumerate(refers): # Hotel part
        if refer in processed_links:
            print(f"⏩ Already processed: {refer}")
            continue

        ## 🔻 Stop when limit is reached
        if already_processed + new_hotels_scraped >= MAX_HOTELS_PER_CITY:
            print(f"🚫 Reached scraping limit ({MAX_HOTELS_PER_CITY}) for city: {city}")
            break

        try:
            element = element_crawl(url=refer)
            hotel_rating = element.get_hotel_rating()
            hotel_ID = element.get_hotel_id()
            dest_ID = element.get_hotel_dest_ID()

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
                new_hotels_scraped += 1  # 🔺 Count new hotel scraped
            else:
                print(f"⚠️ No reviews found: {refer}")

            # Save immediately after each hotel
            pd.concat(df_all, ignore_index=True).to_csv(city_filename, index=False)

        except Exception as e:
            print(f"❌ Error scraping hotel at {refer}: {e}")
            continue