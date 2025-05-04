## Booking.com Scraper
## About
A scalable scraper that can extract all necessary hotel details from any city on Booking.com.
Designed for research, data analysis, and personal projects requiring hotel data at scale.

> **Disclaimer**: This tool is intended for educational and personal use only.  
> Please ensure you comply with [Booking.com](https://www.booking.com)'s Terms of Service before using this tool at scale or in production.

## Features
* **Extract hotel details**: reviews, name, rating, location, number of reviews, etc.
* Dynamically scroll and load more hotel results
* Scrape customer reviews via Booking.com's **GraphQL** API
* Dynamic cookie management to avoid detection
* Modular, class-based design for easy maintenance

## Installation
Clone the repository and install the dependencies:
```python 
git clone https://github.com/CaptainGouzMoew/Booking.com-Crawler.git
```
```python
cd Booking.com-Crawler
```
```python
pip install -r requirements.txt
```
## Usage
To scrape hotel listings:
```python
python main.py
```
To scrape customer reviews for a specific hotel:
```python
python scrape_comments.py --hotel_id 1234567
```
Update city list in ```city.py```:
```python
cities = [
    'ha noi'
    ,'ho-chi-minh'
    # ,'da-nang'
    # ,'da-lat'
    # ,'phu-quoc'
    # ,'ninh-binh'
    # ,'hue'
    # ,'quang-ninh'
    # ,'nha-trang'
    # ,'hoi-an'
]
```
## Configuration
* Headers and cookies must be refreshed periodically to avoid detection.
* Destination and hotel IDs are fetched dynamically during scraping.
* Pagination, scroll delays, and user-agent rotation can be adjusted in the config file.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) — see LICENSE for details.

## Contact
For questions, issues, or collaboration inquiries, please feel free to open an issue on GitHub.

## Tips
Scraping multiple cities might take some time. You’re better off taking a nap while it works its magic and returns the results!
