from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd


class BookingScraper:
    def __init__(self, city):
        self.driver = webdriver.Chrome()
        self.city = city
        self.url = f"https://www.booking.com/searchresults.html?ss={city}"

    def scroll_to_bottom(self, pause_time=1):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print("✅ Reached the bottom of the page.")
                break
            last_height = new_height

    def click_all_load_more(self, max_clicks=10):
        clicks = 0
        while clicks < max_clicks:
            self.scroll_to_bottom(pause_time=1)
            try:
                button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Load more results")]'))
                )
                button.click()
                clicks += 1
                print(f"🔁 Clicked 'Load more results' button ({clicks})")
                time.sleep(2)
            except:
                print("❌ No more 'Load more results' button found.")
                break
        print(f"🔢 Total 'Load more results' button clicks: {clicks}")

    def close(self):
        self.driver.quit()

    def get_hotel_info(self):
        self.driver.get(self.url)
        self.scroll_to_bottom()
        self.click_all_load_more()

        property_cards = self.driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="property-card"]')

        link_list, rating_list = [], []

        for property in property_cards:
            try:
                # name = property.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]').text.strip()
                link = property.find_element(By.CSS_SELECTOR, 'a[data-testid="title-link"]').get_attribute('href')
                review_block = property.find_element(By.CSS_SELECTOR, 'div[data-testid="review-score"]').text.strip()

                lines = review_block.split('\n')
                num_reviews = int(lines[-1].split()[0])

                if num_reviews < 10:
                    continue

                rating = lines[0] if lines else "N/A"

                # name_list.append(name)
                link_list.append(link)
                rating_list.append(rating)
                # num_reviews_list.append(num_reviews)

            except Exception:
                continue

        self.driver.quit()

        df = pd.DataFrame({
            "Page link": link_list,
            "Rating": rating_list
        })
        return df

if __name__ == "__main__":
    cities = ["ha-noi"]
    for city in cities:
        try:
            scraper = BookingScraper(city)
            df = scraper.get_hotel_info()
            df.to_csv('hanoi.csv', index= False)
            print(df.to_markdown())
        except Exception as e:
            print(f"❌ Failed for {city}: {e}")


