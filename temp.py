import requests
import json


#url = "https://www.booking.com/hotel/vn/advisor.en-gb.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAKImanABsACAdICJDBBkYzY4Y2E4LTc1OWUtNDNiNS1iZDgwLTQ0ZWIyYmU2N2I2NdgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=129&hpos=13&keep_landing=1&no_rooms=1&req_adults=2&req_children=0&sb_price_type=total&sr_order=popularity&srepoch=1745505436&srpvid=706e66c40e9505fa&type=total&ucfs=1&"
#url = 'https://www.booking.com/dml/graphql?label=gen173nr-1BCAEoggI46AdIM1gEaPQBiAEBmAEJuAEXyAEM2AEB6AEBiAIBqAIDuAL-t9W_BsACAdICJGNlNzdiZjY2LTIwMDktNDkyNy1iNDI4LWM2ZjIzNDNhZGMxNNgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&aid=304142&ucfs=1&arphpl=1&lang=en-gb'

url = "https://www.booking.com/dml/graphql?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAKImanABsACAdICJDBBkYzY4Y2E4LTc1OWUtNDNiNS1iZDgwLTQ0ZWIyYmU2N2I2NdgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=129&hpos=13&keep_landing=1&no_rooms=1&req_adults=2&req_children=0&sb_price_type=total&sr_order=popularity&srepoch=1745505436&srpvid=706e66c40e9505fa&type=total&ucfs=1&lang=en-gb"

payload = json.dumps({
  "operationName": "ReviewList",
  "variables": {
    "shouldShowReviewListPhotoAltText": True,
    "input": {
      "hotelId": 245838,
      "ufi": -3714993,
      "hotelCountryCode": "vn",
      "sorter": "MOST_RELEVANT",
      "filters": {
        "text": ""
      },
      "skip": 0,
      "limit": 10,
      "hotelScore": 8.4,
      "upsortReviewUrl": "",
      "searchFeatures": {
        "destId": -3714993,
        "destType": "CITY"
      }
    }
  },
  "extensions": {},
  "query": "query ReviewList($input: ReviewListFrontendInput!, $shouldShowReviewListPhotoAltText: Boolean = false) {\n  reviewListFrontend(input: $input) {\n    ... on ReviewListFrontendResult {\n      ratingScores {\n        name\n        translation\n        value\n        ufiScoresAverage {\n          ufiScoreLowerBound\n          ufiScoreHigherBound\n          __typename\n        }\n        __typename\n      }\n      topicFilters {\n        id\n        name\n        isSelected\n        translation {\n          id\n          name\n          __typename\n        }\n        __typename\n      }\n      reviewScoreFilter {\n        name\n        value\n        count\n        __typename\n      }\n      languageFilter {\n        name\n        value\n        count\n        countryFlag\n        __typename\n      }\n      timeOfYearFilter {\n        name\n        value\n        count\n        __typename\n      }\n      customerTypeFilter {\n        count\n        name\n        value\n        __typename\n      }\n      reviewCard {\n        reviewUrl\n        guestDetails {\n          username\n          avatarUrl\n          countryCode\n          countryName\n          avatarColor\n          showCountryFlag\n          anonymous\n          guestTypeTranslation\n          __typename\n        }\n        bookingDetails {\n          customerType\n          roomId\n          roomType {\n            id\n            name\n            __typename\n          }\n          checkoutDate\n          checkinDate\n          numNights\n          stayStatus\n          __typename\n        }\n        reviewedDate\n        isTranslatable\n        helpfulVotesCount\n        reviewScore\n        textDetails {\n          title\n          positiveText\n          negativeText\n          textTrivialFlag\n          lang\n          __typename\n        }\n        isApproved\n        partnerReply {\n          reply\n          __typename\n        }\n        positiveHighlights {\n          start\n          end\n          __typename\n        }\n        negativeHighlights {\n          start\n          end\n          __typename\n        }\n        editUrl\n        photos {\n          id\n          urls {\n            size\n            url\n            __typename\n          }\n          kind\n          mlTagHighestProbability @include(if: $shouldShowReviewListPhotoAltText)\n          __typename\n        }\n        __typename\n      }\n      reviewsCount\n      sorters {\n        name\n        value\n        __typename\n      }\n      __typename\n    }\n    ... on ReviewsFrontendError {\n      statusCode\n      message\n      __typename\n    }\n    __typename\n  }\n}\n"
})
headers = {
  'accept': '*/*',
  'accept-language': 'en,vi;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6',
  'apollographql-client-name': 'b-property-web-property-page_rust',
  'apollographql-client-version': 'ZDLDAfJQ',
  'content-type': 'application/json',
  'origin': 'https://www.booking.com',
  'priority': 'u=1, i',
  'referer': 'https://www.booking.com/hotel/vn/advisor.en-gb.html?aid=304142&label=gen173nr-1FCAQoggJCDXNlYXJjaF9oYS1ub2lIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AEDiAIBqAIDuAKImanABsACAdICJDBBkYzY4Y2E4LTc1OWUtNDNiNS1iZDgwLTQ0ZWIyYmU2N2I2NdgCBeACAQ&sid=f27c5041020bbd59f79966347bb1646d&dist=0&group_adults=2&group_children=0&hapos=129&hpos=13&keep_landing=1&no_rooms=1&req_adults=2&req_children=0&sb_price_type=total&sr_order=popularity&srepoch=1745505436&srpvid=706e66c40e9505fa&type=total&ucfs=1&',
  'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
  'x-apollo-operation-name': 'ReviewList',
  'x-booking-context-action': 'hotel',
  'x-booking-context-action-name': 'hotel',
  'x-booking-context-aid': '304142',
  'x-booking-csrf-token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJjb250ZXh0LWVucmljaG1lbnQtYXBpIiwic3ViIjoiY3NyZi10b2tlbiIsImlhdCI6MTc0NTUwODY4MiwiZXhwIjoxNzQ1NTk1MDgyfQ.iSpjrkldLSoiqagsmdb_62k6mgV2Mj3SFRSamuF2cDr4jkC9edIyW5IhNA0NV-k2FQ8op54pTktlXbQNr8zKKQ',
  'x-booking-dml-cluster': 'rust',
  'x-booking-et-serialized-state': 'EiidyiththmjBim5JVtOZcqaJ4ypMlde3iLRZLwdZ96aTcHQWz7o9Cy4YUOUvxi7B',
  'x-booking-pageview-id': '03ce6d25664206d5',
  'x-booking-site-type-id': '1',
  'x-booking-timeout-ms': '4000',
  'x-booking-topic': 'capla_browser_b-property-web-property-page',
  'x-envoy-upstream-rq-timeout-ms': '4000',
  'Cookie': 'pcm_consent=analytical%3Dtrue%26countryCode%3DVN%26consentId%3D04c8f8bd-8d7e-4e3b-9a16-7532e33cc523%26consentedAt%3D2025-04-05T18%3A06%3A21.709Z%26expiresAt%3D2025-10-02T18%3A06%3A21.709Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DHN%26regulation%3Dnone%26legacyRegulation%3Dnone; pcm_personalization_disabled=0; cors_js=1; bkng_sso_session=e30; bkng_sso_ses=e30; _gcl_au=1.1.1859679353.1743876532; bkng_prue=1; _yjsu_yjad=1743876532.a0b8d342-5254-4298-908e-598394fdfdcf; FPID=FPID2.2.DVvilDyUm6DUoucz%2Fo1XFDMkxW0C4KkmIq%2FP5HeiOaA%3D.1743876531; FPAU=1.1.1859679353.1743876532; bkng_sso_auth=CAIQ0+WGHxpmgm+RurQqrU1kl9UatpZ96qSNMDHnRhG6xt8iKmwIG5IUSBZ9BLkNiRDI1gZAw49Mob83QmgcFIMZXaTLidCNEKE7WvygtGMGCtrYoi5AXWdpzlq9m+0c6+0361f+NTA8xANbROiL; _gid=GA1.2.939834137.1745506493; BJS=-; cgumid=OUed7V9vd2FaNFJwTEowUDVzSEZhbGFoeW5kVjRsVUd4V3d6UCUyRndkQkdSZVR0QVklM0Q; FPLC=ZQAe1vnS4%2BouWpj8frZUzBPivyhlNtOCg%2F01SClPr696larWdq%2FpRoshjksNb07YIE4i48yRoOz30hwFxo0RFC3ZcI0YFimfCffgXuEbObdjurLN9TN89JaF%2FoOZpg%3D%3D; _gat=1; aws-waf-token=d53a611b-99c3-459b-8261-b174d78900f3:AAoAYj5rrE5AAgAA:5xlrIRkdFzgBLJTK7WsuHYB/nB+06EOhgT+cWpHj4jfhwh8keq/AzYnse/3pW+5+8T3qPEShEcTyOgbpfjzcjCwU3+2lrl7sa9xuG6DkYaRsFYy//VxtZH4ouAdJj/o0XYjy5xIKlng2mToyrX1l0uZlNjGeo7VdfP5PqeUdnLfcIWgA1wLRoQ+OEmzvjgtW4UJQWImkXqRctUeRVvFGRqI9Lz4IF3lMmEobuw8UuUSYlTNqEznJjuCGDqVjTKGoU5M=; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Apr+24+2025+22%3A31%3A25+GMT%2B0700+(Indochina+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=01263043-5400-4024-a287-1f2f6e644ea4&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&implicitConsentCountry=nonGDPR&implicitConsentDate=1743876531633&AwaitingReconsent=false; lastSeen=0; bkng=11UmFuZG9tSVYkc2RlIyh9YXSgTtYpR%2F1WOjMvuuinviGT3RmVvTxqMgEQ7fcphknPm0Nf13Us7ALeduuT5uH5Ebg3a66tCHEpGY1LgNOW0t5WxWN3Amk401wiB3kXcjcOhUQHEfGMWEgJZ720KGWW%2FUmqEmoe2f1Ig4HJQRGbVI8c0rXziGnJFplc%2FX6KBORrpVQ8VuB%2BmYqDIxXTz44z2A%3D%3D; _ga_A12345=GS1.1.1745506494.44.1.1745508686.0.0.96466397; _ga=GA1.1.801626595.1743876531; cto_bundle=0o7iJV9QZVQzT2dvbjBmJTJCVXFpSmlucFF4QlhOOUJ3QXRxQldsJTJCNU0xSXpudnlONDclMkZaJTJCQmFMVzA5eFQzMGRBZXc3U3p2SDkxRVR1SHZQbWFwTlRLeHFLWnQ1VmdadHdtTjdOYlZWSWluSE8zdHRVQ2Y4eUVIcEtnWDZTbXlPMmlpMVRoVVVBWnh2QUVLUlBST1ZZZkxtQkFCdyUzRCUzRA; _uetsid=1536e0d0211c11f090ae8fe7050fdb6c; _uetvid=07fdd2a0124911f0bab44371390af731; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmjuWdy5KhNt%2BT3sAHH2JfJkEdtqmmHWQi4dLdcT7b1FDVoNPty%2BhChO1zUrCcSreY4R6u7Fr1URyYiT%2BwdJ1oI3svr5r8g83KUDLoKURnkpeJ3aQCyHAc4WN1kpZki9pFLb%2FaTS%2FAIxlg0Vec0kxAsGuiIPx6O1C7O35jrcnIqFbAA%3D%3D; bkng_sso_auth=CAIQ0+WGHxpmxEI9+hhUokiYLJOH9xWG4PcR9GROwXDMg3TDo3MtOMMnMmuQ5RevzC/VioFDddBLR7ch4XHhI4tFMj6e0b5rZz8jK4RdrbRCaHAEyl0QWxkYdw5bH91G7F5sqy6ouYwFDeGAH8WK; pcm_personalization_disabled=0'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
