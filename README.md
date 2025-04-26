# Booking.com Scraper
About
A scalable scraper which basically can extract all needed detail hotel informations from any city on Booking.com.
It is designed for research, data analysis, and personal projects requiring hotel data at scale.
Disclaimer: This tool is intended for educational and personal use only. Ensure you comply with Booking.com's Terms of Service before using it at scale.

Feature
✅ Extract reviews, hotel name, rating, location, and number of reviews,...
✅ Scroll and load more hotel results dynamically
✅ Scrape customer reviews via Booking.com's GraphQL API
✅ Dynamic cookie to avoid detection
✅ Modular, class-based design for easy maintenance

Installation
git clone https://github.com/CaptainGouzMoew/Booking.com-Crawler.git
pip install -r requirements.txt

Usage
To scrape hotel listings:
python scrape_hotels.py 

To scrape customer reviews for a specific hotel:
python scrape_comments.py --hotel_id 1234567

Configuration
Headers and cookies must be refreshed occasionally to avoid detection.
Destination IDs and Hotel IDs can be fetched dynamically during scraping.
Settings for pagination, scroll delays, and user-agent rotation can be adjusted inside the config file.

License
Distributed under the MIT License. See LICENSE for more information.

Contact
Dong Thanh Duong
GitHub: @CaptainGouzMoew
Email: dongthanhduong0312@gmail.com

Tips
scrape a city might take quite a while, you're better take a nap before taking the result
