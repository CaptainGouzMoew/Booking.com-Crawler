import requests
from bs4 import BeautifulSoup


def get_hotel_dest_ID(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')  
        hotel_id_input = soup.find('input', {'name': 'dest_id'})    
        
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
    
def get_hotel_rating(url):
    headers = {'User-Agent': 'Mozilla/5.0'}  
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        hotel_id_input = soup.find('div', class_ = 'ac4a7896c7')
        score_text = hotel_id_input.text.strip().replace('Scored', '').strip()
        
        return score_text

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
    url = 'https://www.booking.com/hotel/vn/bens-premier-amp-apartment-hanoi-center.en-gb.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEEB-AEDiAIBqAIDuALDuLTABsACAdICJGNkYmFhNTE4LTdkYmItNGZjYS05ZmY0LWM2ZDAwNzFlM2RkOdgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=25&hpos=25&keep_landing=1&no_rooms=1&req_adults=2&req_children=0&sb_price_type=total&sr_order=popularity&srepoch=1745689706&srpvid=b5fd7d21708811b1&type=total&ucfs=1&'
    print(get_hotel_rating(url))
    print(get_hotel_id(url))
    print(get_hotel_dest_ID(url))



