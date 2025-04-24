import requests
from bs4 import BeautifulSoup


def get_hotel_id(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        hotel_id_input = soup.find('input', {'name': 'hotel_id'})
        
        if hotel_id_input:
            hotel_id = hotel_id_input.get('value')
            #print(f'Hotel ID: {hotel_id}')
            return hotel_id
        else:
            print('Cannot scrape hotel ID')
            return None
    else:
        print(f'Failed to load page, status code: {response.status_code}')
        return None


if __name__ == "__main__":
  url = 'https://www.booking.com/hotel/vn/king-palace-and-spa.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAKH8p7ABsACAdICJGM3MDA0MjU2LWM5NjAtNDUzNi05Y2NiLTJiNmY2NWUzNzY0YdgCBeACAQ&ucfs=1&arphpl=1&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=5f366e8334fb0418&srepoch=1745336621&from=searchresults'
  print(get_hotel_id(url))

  