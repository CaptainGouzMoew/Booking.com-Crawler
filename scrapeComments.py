import requests
import json
import pandas as pd
import re

from crawl_element import get_hotel_dest_ID, get_hotel_id, get_hotel_rating

def get_dynamic_headers(referer):
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    })

    response = session.get(referer)
    cookies = session.cookies.get_dict()

    # Extract csrf token from page content
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

    # Add cookies as a string
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

    # Get fresh headers dynamically
    self.headers = get_dynamic_headers(referal)

    # self.url = "https://www.booking.com/dml/graphql?label=gen173nr-1BCAEoggI46AdIM1gEaPQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAL-t9W_BsACAdICJGNlNzdiZjY2LTIwMDktNDkyNy1iNDI4LWM2ZjIzNDNhZGMxNNgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&aid=304142&ucfs=1&arphpl=1&lang=en-gb"
    # self.referal = 'https://www.booking.com/hotel/vn/my-sg-hn.en-gb.html?aid=304142&label=gen173nr-1FCAQoggJCEnNlYXJjaF9oby1jaGktbWluaEgzWARo9AGIAQGYAQm4ARfIAQzYAQHoAQH4AQOIAgGoAgO4AqrZ778GwAIB0gIkN2IxN2QyMjUtZjE2ZS00Mjc0LWE4MDYtOTM5MjVlZjc0YWM42AIF4AIB&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=2&hpos=2&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&srepoch=1744563495&srpvid=706e7715825a0160&type=total&ucfs=1&'
    # self.hotel_ID = '13230638'
    # self.dest_ID = '-3730078'
    # self.hotel_rating = '8.3'

    # self.headers = {
    #   'accept': '*/*',
    #   'accept-language': 'en,vi;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    #   'apollographql-client-name': 'b-property-web-property-page_rust',
    #   'apollographql-client-version': 'ZDLDAfJQ',
    #   'content-type': 'application/json',
    #   'origin': 'https://www.booking.com',
    #   'priority': 'u=1, i',
    #   'referer': self.referal,
    #   'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    #   'sec-ch-ua-mobile': '?0',
    #   'sec-ch-ua-platform': '"Windows"',
    #   'sec-fetch-dest': 'empty',
    #   'sec-fetch-mode': 'cors',
    #   'sec-fetch-site': 'same-origin',
    #   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    #   'x-apollo-operation-name': 'ReviewList',
    #   'x-booking-context-action': 'hotel',
    #   'x-booking-context-action-name': 'hotel',
    #   'x-booking-context-aid': '304142',
    #   'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTc0NTA3NzkwOCwiZXhwIjoxNzQ1MTY0MzA4fQ.bDBkvGj5EvYEAsPxUSoihlTkrCX--bf0Gm_YORJU16cBDKw4boGuhWkFoDtwGhI3ex-fzqLqUuwyuBhMFqhY-A',
    #   'x-booking-dml-cluster': 'rust',
    #   'x-booking-et-serialized-state': 'EZXl8NdUdenRTEjSK-YA-Hpw5JqYEDw4eEyrc2orucoPD8dwwkHDFV08z130hkMdv',
    #   'x-booking-pageview-id': '947b6f8a2d9603bf',
    #   'x-booking-site-type-id': '1',
    #   'x-booking-timeout-ms': '4000',
    #   'x-booking-topic': 'capla_browser_b-property-web-property-page',
    #   'x-envoy-upstream-rq-timeout-ms': '4000',
    #   'Cookie': 'pcm_consent=analytical%3Dtrue%26countryCode%3DVN%26consentId%3D04c8f8bd-8d7e-4e3b-9a16-7532e33cc523%26consentedAt%3D2025-04-05T18%3A06%3A21.709Z%26expiresAt%3D2025-10-02T18%3A06%3A21.709Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DHN%26regulation%3Dnone%26legacyRegulation%3Dnone; pcm_personalization_disabled=0; cors_js=1; bkng_sso_session=e30; bkng_sso_ses=e30; _gcl_au=1.1.1859679353.1743876532; bkng_prue=1; _yjsu_yjad=1743876532.a0b8d342-5254-4298-908e-598394fdfdcf; FPID=FPID2.2.DVvilDyUm6DUoucz%2Fo1XFDMkxW0C4KkmIq%2FP5HeiOaA%3D.1743876531; FPAU=1.1.1859679353.1743876532; _gid=GA1.2.2113731798.1744891616; BJS=-; bkng_sso_auth=CAIQ0+WGHxpmopGHvb8OATXTDC/OfIeCbY9zaZN1Y6v+kRvx/jnPcTymadsyER8tscfrKPpZzflVQMKhDGlawere8yyA45HEEj2h7VkGWCczJhJa3EwFQeA0X9N4lin6O5REw091uTH9lRBr9vOI; FPLC=bNJoGz6iInI9i1XBPU1ZPl5VM4UkmVCMDKNOOqTaA%2FGf03sXezlEIlbd%2BGflgpIsSYnwYGF4cDmIyxiOc1p1yeRGPAynqLSbtqSTWRixzYKqUxpUw1XhWznib838vA%3D%3D; cgumid=gw264l9vd2FaNFJwTEowUDVzSEZhbGFoeW5kdEMxSGliN21yNkVHam9Bam1NeHRJJTNE; _gat=1; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Apr+19+2025+22%3A51%3A50+GMT%2B0700+(Indochina+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=01263043-5400-4024-a287-1f2f6e644ea4&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&implicitConsentCountry=nonGDPR&implicitConsentDate=1743876531633&AwaitingReconsent=false; _ga=GA1.1.801626595.1743876531; cto_bundle=T3lUN19mb1JUZFp2dEg0T2UlMkJaTUNFczRBM1AzT0hvd3dZJTJGcWhwSHpNOVhzVXdtT2YycmlXeUpZbkolMkZJSVBJV0xrMkklMkZYMm5pdSUyRnREVVVTQzJkZFR1c2t2JTJGU2YlMkZOWnpRdE5iQjVza0J1R2pIUFNJNE1ZQVdaTUY5QjhaejJyZk9BMnB6MlBpa1lzZTNnRW1XazVLYjBkcXBWUSUzRCUzRA; _uetsid=79bf11e01b8411f0b931f7ce15b296ae; _uetvid=07fdd2a0124911f0bab44371390af731; _ga_A12345=GS1.1.1745075877.35.1.1745077919.0.0.1232883723; aws-waf-token=ea022f85-7f0b-45b8-a089-fa4f44a803fa:AAoAlANuvVUjAQAA:VV0UPx+zutaImmWhIcPDS6hsykT2ugC4v8CQboUltf6Phi0XJaReKReIzpY+sWUvmcASQo0xw87djwwzSikQ3G5/6+Qy3NAPjKvBHhjQ/KVLzSrk27pTJfyVVyvq2AU78lxqbZztJO2HfZzT2+M4w+cc/jGYsKWsOrx0JPqOf30PrT9ZLip7A3Jr5bhlkLNpJcqPaTRs+b/lEYEGpv7GHlyzBPlXdXRe06FmkvYPQv4mPS9VG2kivt/0/9C7sPJFY9A=; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbKE7bjkbYWznaKBDrc%2FwooL%2B%2BUuQf8Xik%2BBIxIkWPp75dbhWs4fkwQREh1CXDRUNm84mMOygAalj32ks5pHNnwRHpO%2B4ojHbJn799WvLuyPWFjCvqQknDVW%2B2tcOD5nIlr0Xq%2FfB0hQK7eh7Lr4M6P3IQe6Feeg0bP5Y0U%2FNtuUI%3D; lastSeen=0; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmjs4YuftXBlOYi%2Fz%2BGAxPpCvpF2e5uDGBnDLD7MPNM3b6xYVgT7m%2FtB5%2FuqA80TqLTWpeFzd3oDwDnWon9M8Giw%2Bxd69FtEjLFwcPOlmRUJTay1EizaooY9%2FRmT8yHAOfBEyw9qLzQ261l8ImISz4d5ubwYia30AmeK7OMo6JKBqhg%3D%3D; bkng_sso_auth=CAIQ0+WGHxpmxEI9+hhUokiYLJOH9xWG4PcR9GROwXDMg3TDo3MtOMMnMmuQ5RevzC/VioFDddBLR7ch4XHhI4tFMj6e0b5rZz8jK4RdrbRCaHAEyl0QWxkYdw5bH91G7F5sqy6ouYwFDeGAH8WK; pcm_personalization_disabled=0'
    # }

  def getReviews(self, page_number, limit=10):
    skip = (page_number - 1) * limit

    payload = json.dumps({
      "operationName": "ReviewList",
      "variables": {
        "shouldShowReviewListPhotoAltText": True,
        "input": {
          "hotelId": int(self.hotel_ID), # hotel_ID - 13230638
          "ufi": int(self.dest_ID), # dest_ID  -3730078
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
            "destId": int(self.dest_ID), # dest_ID  -3730078
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
      POS_review_text = review['textDetails']['positiveText']
      NEG_review_text = review['textDetails']['negativeText']
      
      if (POS_review_text and POS_review_text.strip()) or (NEG_review_text and NEG_review_text.strip()):
        extracted_data.append({
            'Name': name,
            'Country': country,
            'Rating': rating,
            'Pos_Review': POS_review_text,
            'Neg_Review': NEG_review_text,
            'Page link' : self.referal
        })
    return pd.DataFrame(extracted_data)
  
  def scrapeReview(self):
    reviews = self.fetchReviews()
    df = self.to_dataframe(reviews)
    return df

if __name__ == "__main__":
  #scrape = ReviewScrape()
  refer = 'https://www.booking.com/hotel/vn/h-l-art-hanoi.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAL73bTABsACAAdICJDQ0N2YyMTYzLWFkNjAtNDY1MS05ZDEwLWI2YjAwNTkzZDM0ZNgCBeACAQ&ucfs=1&arphpl=1&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=4e3b867dd67f0b5a&srepoch=1745694499&from=searchresults'
  scrape = ReviewScrape(
    referal = refer
    ,hotel_ID = get_hotel_id(refer)
    ,dest_ID = get_hotel_dest_ID(refer)
    ,hotel_rating = get_hotel_rating(refer)
  )


  df =  scrape.scrapeReview()
  #df.to_csv('hotelReview.csv', index=False)
  print(df)
  



