import requests
import json
import pandas as pd
import re
import argparse

from scr.booking_scraper.crawl_element import element_crawl
class headerBuilder:  
  def get_dynamic_headers(self,referer):
      session = requests.Session()
      session.headers.update({
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
      })

      response = session.get(referer)
      cookies = session.cookies.get_dict()

      csrf_token = None
      match = re.search(r'"csrfToken":"(.*?)"', response.text)
      if match:
          csrf_token = match.group(1)

      if not csrf_token:
          print("⚠️ CSRF token not found. Will use a fallback token.")

      headers = {
          'accept': '*/*',
          'accept-language': 'en,vi;q=0.9',
          'content-type': 'application/json',
          'origin': 'https://www.booking.com',
          'referer': referer,
          'user-agent': session.headers['User-Agent'],
          'x-booking-csrf-token': csrf_token if csrf_token else 'fallback-token',
      }

      cookie_header = '; '.join([f"{k}={v}" for k, v in cookies.items()])
      headers['cookie'] = cookie_header

      return headers

class ReviewScrape():
  
  url = 'https://www.booking.com/dml/graphql?label=gen173nr-1BCAEoggI46AdIM1gEaPQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAL-t9W_BsACAdICJGNlNzdiZjY2LTIwMDktNDkyNy1iNDI4LWM2ZjIzNDNhZGMxNNgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&aid=304142&ucfs=1&arphpl=1&lang=en-gb'

  def __init__(self, referal, hotel_ID, dest_ID, hotel_rating):
    #self.url = 'https://www.booking.com/dml/graphql?label=gen173nr-1BCAEoggI46AdIM1gEaPQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAL-t9W_BsACAdICJGNlNzdiZjY2LTIwMDktNDkyNy1iNDI4LWM2ZjIzNDNhZGMxNNgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&aid=304142&ucfs=1&arphpl=1&lang=en-gb'
    
    self.referal = referal
    self.hotel_ID = int(hotel_ID)
    self.dest_ID = int(dest_ID)
    self.hotel_rating = float(hotel_rating)

    dynamic = headerBuilder()
    self.headers = dynamic.get_dynamic_headers(referal) # dynamic

  def getReviews(self, page_number, limit=10):
    skip = (page_number - 1) * limit

    payload = json.dumps({
      "operationName": "ReviewList",
      "variables": {
        "shouldShowReviewListPhotoAltText": True,
        "input": {
          "hotelId": int(self.hotel_ID),  
          "ufi": int(self.dest_ID),  
          "hotelCountryCode": "vn",
          "sorter": "MOST_RELEVANT",
          "filters": {
            "text": ""
          },
          "skip": skip,
          "limit": limit,
          "hotelScore": int(self.hotel_rating),
          "upsortReviewUrl": "",
          "searchFeatures": {
            "destId": int(self.dest_ID),  
            "destType": "CITY"
          }
        }
      },
      "extensions": {},
      "query": "query ReviewList($input: ReviewListFrontendInput!, $shouldShowReviewListPhotoAltText: Boolean = false) {\n  reviewListFrontend(input: $input) {\n    ... on ReviewListFrontendResult {\n      ratingScores {\n        name\n        translation\n        value\n        ufiScoresAverage {\n          ufiScoreLowerBound\n          ufiScoreHigherBound\n          __typename\n        }\n        __typename\n      }\n      topicFilters {\n        id\n        name\n        isSelected\n        translation {\n          id\n          name\n          __typename\n        }\n        __typename\n      }\n      reviewScoreFilter {\n        name\n        value\n        count\n        __typename\n      }\n      languageFilter {\n        name\n        value\n        count\n        countryFlag\n        __typename\n      }\n      timeOfYearFilter {\n        name\n        value\n        count\n        __typename\n      }\n      customerTypeFilter {\n        count\n        name\n        value\n        __typename\n      }\n      reviewCard {\n        reviewUrl\n        guestDetails {\n          username\n          avatarUrl\n          countryCode\n          countryName\n          avatarColor\n          showCountryFlag\n          anonymous\n          guestTypeTranslation\n          __typename\n        }\n        bookingDetails {\n          customerType\n          roomId\n          roomType {\n            id\n            name\n            __typename\n          }\n          checkoutDate\n          checkinDate\n          numNights\n          stayStatus\n          __typename\n        }\n        reviewedDate\n        isTranslatable\n        helpfulVotesCount\n        reviewScore\n        textDetails {\n          title\n          positiveText\n          negativeText\n          textTrivialFlag\n          lang\n          __typename\n        }\n        isApproved\n        partnerReply {\n          reply\n          __typename\n        }\n        positiveHighlights {\n          start\n          end\n          __typename\n        }\n        negativeHighlights {\n          start\n          end\n          __typename\n        }\n        editUrl\n        photos {\n          id\n          urls {\n            size\n            url\n            __typename\n          }\n          kind\n          mlTagHighestProbability @include(if: $shouldShowReviewListPhotoAltText)\n          __typename\n        }\n        __typename\n      }\n      reviewsCount\n      sorters {\n        name\n        value\n        __typename\n      }\n      __typename\n    }\n    ... on ReviewsFrontendError {\n      statusCode\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
    })
  
    response = requests.request("POST", self.url, headers=self.headers, data=payload)
  
    #print(f"Status Code: {response.status_code}")
    #print(f"Response Text: {response.text[:500]}")
    
    if response.status_code == 200:
      try:
          return response.json().get('data', {}).get('reviewListFrontend', {}).get('reviewCard', [])
      except json.JSONDecodeError:
          print("Error decoding JSON response.")
          return []
    else:
      print(f"Error: {response.status_code}")
      return []
  
  def fetchReviews(self):
    all_reviews = []
    page_number = 1
    
    while True:
      reviews = self.getReviews(page_number=page_number)
      
      if not reviews:
        break
      
      all_reviews.extend(reviews)
      page_number += 1

      # time.sleep(1)
    return all_reviews

  def to_dataframe(self, reviews):
    extracted_data = []
    for review in reviews:
      name = review['guestDetails']['username']
      country = review['guestDetails']['countryName']
      rating = review['reviewScore']
      POS_review_text = str(review['textDetails'].get('positiveText', '') or '')
      NEG_review_text = str(review['textDetails'].get('negativeText', '') or '')
      
      if (POS_review_text and POS_review_text.strip()) or (NEG_review_text and NEG_review_text.strip()):
        extracted_data.append({
            'Name': name
            ,'Country': country
            ,'Rating': rating
            ,'Pos_Review': POS_review_text
            ,'Neg_Review': NEG_review_text
            #,'Page link' : self.referal
        })
    return pd.DataFrame(extracted_data)
  
  def finished_hotel(self):
    done_hotel = []
    done_hotel. append({
      'Page link' : self.referal
    })
    df = pd.DataFrame(done_hotel)
    return df

  def scrapeReview(self):
    reviews = self.fetchReviews()
    df = self.to_dataframe(reviews)
    return df

if __name__ == "__main__":
  # refer = 'https://www.booking.com/hotel/vn/h-l-art-hanoi.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAL73bTABsACAAdICJDQ0N2YyMTYzLWFkNjAtNDY1MS05ZDEwLWI2YjAwNTkzZDM0ZNgCBeACAQ&ucfs=1&arphpl=1&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=4e3b867dd67f0b5a&srepoch=1745694499&from=searchresults'
  # element = element_crawl(url=refer)
  # scrape = ReviewScrape(
  #   referal = refer
  #   ,hotel_ID = element.get_hotel_id()
  #   ,dest_ID = element.get_hotel_dest_ID()
  #   ,hotel_rating = element.get_hotel_rating()
  # )

  # df =  scrape.scrapeReview()
  # #df.to_csv('hotelReview.csv', index=False)
  # print(df)
  
  parser = argparse.ArgumentParser(description='Scrape Booking.com hotel reviews.')
  parser.add_argument('--url', type=str, required=True, help='Hotel URL to scrape')

  args = parser.parse_args()
  refer = args.url

  element = element_crawl(url=refer)
  scrape = ReviewScrape(
      referal=refer,
      hotel_ID=element.get_hotel_id(),
      dest_ID=element.get_hotel_dest_ID(),
      hotel_rating=element.get_hotel_rating()
  )

  df = scrape.scrapeReview()
  print(df)