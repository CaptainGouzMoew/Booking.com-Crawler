import pandas as pd
from scrapeComments import ReviewScrape
from hotel_nameCrawl import BookingScraper
from crawl_element import get_hotel_dest_ID, get_hotel_id, get_hotel_rating
from city import cities
from pathlib import Path


output_dir = Path("output_reviews")
output_dir.mkdir(exist_ok=True)

for city in cities:
    print(f"\n📍 Processing city: {city}")
    city_filename = output_dir / f"{city.replace(' ', '_')}.xlsx"
    
    if city_filename.exists():
        existing_df = pd.read_excel(city_filename)
        processed_links = set(existing_df['referal'].unique())
        df_all = [existing_df]
        print(f"✅ Found existing data for city: {len(processed_links)} hotels already saved.")
    else:
        processed_links = set()
        df_all = []
    
    hotel_scrape = BookingScraper(city= city)
    df = hotel_scrape.get_hotel_info()
    df_all = []
    
    refers = df['Page link']
    for refer in refers:
        hotel_rating = get_hotel_rating(refer)  #['9.8', '9.4']
        hotel_ID = get_hotel_id(refer) #['10859941', '3244605']
        dest_ID = get_hotel_dest_ID(refer) #['-3714993', '-3714993'] 

        
        review_scraper = ReviewScrape(referal=refer, hotel_ID=hotel_ID, dest_ID=dest_ID, hotel_rating=hotel_rating)
        df = review_scraper.scrapeReview()
        
        df_all.append(df)

    final_df = pd.concat(df_all, ignore_index=True)
    final_df.to_excel('test.xlsx', index= False)
    #print(final_df.to_markdown())
