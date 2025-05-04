import requests
from bs4 import BeautifulSoup

class element_crawl:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.soup = None
    
    def _load_page(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            if response.status_code == 200:
                self.soup = BeautifulSoup(response.text, 'html.parser')
                return True
            else:
                print(f"❌ Failed to load page ({response.status_code})")
        except Exception as e:
            print(f"❌ Error loading page: {e}")
        return False

    def get_hotel_id(self):
        if not self.soup and not self._load_page():
            return None
        input_tag = self.soup.find('input', {'name': 'hotel_id'})
        return input_tag.get('value') if input_tag else None

    def get_hotel_dest_ID(self):
        if not self.soup and not self._load_page():
            return None
        input_tag = self.soup.find('input', {'name': 'dest_id'})
        return input_tag.get('value') if input_tag else None

    def get_hotel_rating(self):
        if not self.soup and not self._load_page():
            return None
        rating_tag = self.soup.find('div', class_='f63b14ab7a dff2e52086')
        return rating_tag.text.strip().replace('Scored', '').strip() if rating_tag else None


if __name__ == "__main__":
    url = 'https://www.booking.com/hotel/vn/bens-premier-amp-apartment-hanoi-center.en-gb.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEEB-AEDiAIBqAIDuALDuLTABsACAdICJGNkYmFhNTE4LTdkYmItNGZjYS05ZmY0LWM2ZDAwNzFlM2RkOdgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=25&hpos=25&keep_landing=1&no_rooms=1&req_adults=2&req_children=0&sb_price_type=total&sr_order=popularity&srepoch=1745689706&srpvid=b5fd7d21708811b1&type=total&ucfs=1&'
    
    element = element_crawl(url=url)
    print(element.get_hotel_rating())
    print(element.get_hotel_id())
    print(element.get_hotel_dest_ID())



