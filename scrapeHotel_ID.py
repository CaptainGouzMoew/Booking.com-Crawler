import requests
import json

url = "https://www.booking.com/c360/v1/track"

payload = json.dumps({
  "events": [
    {
      "action_name": "location.sr_map_opened",
      "action_version": "1.0.0",
      "content": {
        "content": {
          "source": "entry_point"
        }
      },
      "context": {
        "local": {
          "language": "en-us"
        },
        "page": {
          "page_referrer": "https://www.booking.com/",
          "page_url": "https://www.booking.com/searchresults.html?ss=Hanoi&ssne=Hanoi&ssne_untouched=Hanoi&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAK-ieK_BsACAdICJGYxMmJiNDQ3LTY3Y2YtNGI4Zi1hNmIwLWM1OTkyNTU1MDNiMdgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-3714993&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
          "page_title": "Booking.com: Hotels in Hanoi. Book your hotel now!"
        },
        "web": {
          "browser_language": "en-US"
        }
      },
      "tracker": {
        "tracker_name": "C360ReactTracker",
        "tracker_type": "Client",
        "tracker_version": "0.1.1"
      }
    },
    {
      "action_name": "accommodation.sr_page_composition",
      "action_version": "1.1",
      "content": {
        "page_view_id": "427b3695c7b70318",
        "active_view": "list",
        "items": [
          {
            "item_id": 10958124,
            "item_column": 0,
            "item_row": 0
          },
          {
            "item_id": 13672022,
            "item_column": 0,
            "item_row": 1
          },
          {
            "item_id": 9327485,
            "item_column": 0,
            "item_row": 2
          },
          {
            "item_id": 11421502,
            "item_column": 0,
            "item_row": 3
          },
          {
            "item_id": 13926856,
            "item_column": 0,
            "item_row": 4
          },
          {
            "item_id": 13298498,
            "item_column": 0,
            "item_row": 5
          },
          {
            "item_id": 12407967,
            "item_column": 0,
            "item_row": 6
          },
          {
            "item_id": 12932371,
            "item_column": 0,
            "item_row": 7
          },
          {
            "item_id": 334136,
            "item_column": 0,
            "item_row": 8
          },
          {
            "item_id": 9555365,
            "item_column": 0,
            "item_row": 9
          },
          {
            "item_id": 651457,
            "item_column": 0,
            "item_row": 10
          },
          {
            "item_id": 13228852,
            "item_column": 0,
            "item_row": 11
          },
          {
            "item_id": 10203649,
            "item_column": 0,
            "item_row": 12
          },
          {
            "item_id": 632733,
            "item_column": 0,
            "item_row": 13
          },
          {
            "item_id": 3235187,
            "item_column": 0,
            "item_row": 14
          },
          {
            "item_id": 11830130,
            "item_column": 0,
            "item_row": 15
          },
          {
            "item_id": 236959,
            "item_column": 0,
            "item_row": 16
          },
          {
            "item_id": 12817245,
            "item_column": 0,
            "item_row": 17
          },
          {
            "item_id": 9659534,
            "item_column": 0,
            "item_row": 18
          },
          {
            "item_id": 287397,
            "item_column": 0,
            "item_row": 19
          },
          {
            "item_id": 1106054,
            "item_column": 0,
            "item_row": 20
          },
          {
            "item_id": 12539449,
            "item_column": 0,
            "item_row": 21
          },
          {
            "item_id": 8706083,
            "item_column": 0,
            "item_row": 22
          },
          {
            "item_id": 9844929,
            "item_column": 0,
            "item_row": 23
          },
          {
            "item_id": 11038850,
            "item_column": 0,
            "item_row": 24
          }
        ]
      },
      "context": {
        "local": {
          "language": "en-us"
        },
        "page": {
          "page_referrer": "https://www.booking.com/",
          "page_url": "https://www.booking.com/searchresults.html?ss=Hanoi&ssne=Hanoi&ssne_untouched=Hanoi&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAK-ieK_BsACAdICJGYxMmJiNDQ3LTY3Y2YtNGI4Zi1hNmIwLWM1OTkyNTU1MDNiMdgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-3714993&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
          "page_title": "Booking.com: Hotels in Hanoi. Book your hotel now!"
        },
        "web": {
          "browser_language": "en-US"
        }
      },
      "tracker": {
        "tracker_name": "C360ReactTracker",
        "tracker_type": "Client",
        "tracker_version": "0.1.1"
      }
    },
    {
      "action_name": "room_selection.sr_card_only_x_left_viewed",
      "action_version": "1.0.0",
      "content": {
        "hotel": {
          "travel_product_id": 10958124
        },
        "block": {
          "id": "1095812401_382781342_0_1_0"
        }
      },
      "context": {
        "local": {
          "language": "en-us"
        },
        "page": {
          "page_referrer": "https://www.booking.com/",
          "page_url": "https://www.booking.com/searchresults.html?ss=Hanoi&ssne=Hanoi&ssne_untouched=Hanoi&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAK-ieK_BsACAdICJGYxMmJiNDQ3LTY3Y2YtNGI4Zi1hNmIwLWM1OTkyNTU1MDNiMdgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-3714993&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
          "page_title": "Booking.com: Hotels in Hanoi. Book your hotel now!"
        },
        "web": {
          "browser_language": "en-US"
        }
      },
      "tracker": {
        "tracker_name": "C360ReactTracker",
        "tracker_type": "Client",
        "tracker_version": "0.1.1"
      }
    },
    {
      "action_name": "room_selection.sr_card_only_x_left_viewed",
      "action_version": "1.0.0",
      "content": {
        "hotel": {
          "travel_product_id": 13672022
        },
        "block": {
          "id": "1367202201_411314970_2_0_0"
        }
      },
      "context": {
        "local": {
          "language": "en-us"
        },
        "page": {
          "page_referrer": "https://www.booking.com/",
          "page_url": "https://www.booking.com/searchresults.html?ss=Hanoi&ssne=Hanoi&ssne_untouched=Hanoi&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAK-ieK_BsACAdICJGYxMmJiNDQ3LTY3Y2YtNGI4Zi1hNmIwLWM1OTkyNTU1MDNiMdgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-3714993&dest_type=city&group_adults=2&no_rooms=1&group_children=0",
          "page_title": "Booking.com: Hotels in Hanoi. Book your hotel now!"
        },
        "web": {
          "browser_language": "en-US"
        }
      },
      "tracker": {
        "tracker_name": "C360ReactTracker",
        "tracker_type": "Client",
        "tracker_version": "0.1.1"
      }
    }
  ]
})
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
  'content-type': 'application/json',
  'origin': 'https://www.booking.com',
  'priority': 'u=1, i',
  'referer': 'https://www.booking.com/searchresults.html?ss=Hanoi&ssne=Hanoi&ssne_untouched=Hanoi&label=gen173nr-1FCAEoggI46AdIM1gEaPQBiAEBmAExuAEXyAEM2AEB6AEB-AECiAIBqAIDuAK-ieK_BsACAdICJGYxMmJiNDQ3LTY3Y2YtNGI4Zi1hNmIwLWM1OTkyNTU1MDNiMdgCBeACAQ&aid=304142&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-3714993&dest_type=city&group_adults=2&no_rooms=1&group_children=0',
  'sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
  'x-booking-aid': '304142',
  'x-booking-csrf': 'undefined',
  'x-booking-et-seed': 'undefined',
  'x-booking-label': 'undefined',
  'x-booking-language-code': 'en-us',
  'x-booking-pageview-id': 'undefined',
  'x-booking-platform': '',
  'x-booking-session-id': 'undefined',
  'x-booking-sitetype-id': 'undefined',
  'Cookie': 'pcm_consent=analytical%3Dtrue%26countryCode%3DVN%26consentId%3D544a7693-c673-46e1-a596-a7eeb9d319e9%26consentedAt%3D2025-04-09T06%3A36%3A18.621Z%26expiresAt%3D2025-10-06T06%3A36%3A18.621Z%26implicit%3Dtrue%26marketing%3Dtrue%26regionCode%3DHN%26regulation%3Dnone%26legacyRegulation%3Dnone; pcm_personalization_disabled=0; cors_js=1; bkng_sso_session=e30; bkng_sso_ses=e30; _gid=GA1.2.1841103093.1744180583; BJS=-; _gcl_au=1.1.948819525.1744180584; bkng_prue=1; FPID=FPID2.2.n0UCXgbJlAwYKlGx7PqJVBOzVJpRhbjJccVGYlDqYZM%3D.1744180583; FPAU=1.1.948819525.1744180584; _yjsu_yjad=1744180585.162f545b-0ebf-4ac7-b4dd-b79a63a9834d; _rdt_uuid=1744180725627.123ff162-7e54-4abc-9b7b-b1857923602c; _ga_PJSQX7HV9H=GS1.1.1744180725.1.1.1744180889.0.0.0; g_state={"i_p":1744188176938,"i_l":1}; explicit_language_preference=en-US; bkng_sso_auth=CAIQ0+WGHxpmeUJU0C4NDSs8fe9wyon+VdHDF5yTWh/rbErwqKFZxa4TcVcUIL8hg58BrhOlXaB9mKCaan3WBm1BrYZOWXW95qw+/RFtbPnhWOep30d0KGpZmrbaaTeBlCoAfAs1lco2QquEsKZ8; cgumid=oY01el9RU0RtamRUSUN6aXRXTzVRdVVXSVFLQkpNeE9DaEFYNEEwVHlFZjlCZjhPaXlUeXFmMUtyTXdFcWtFeFZBbkhKWEE4eWJpcGxVbkUlMkJtNXFBR2VsMmNRJTNEJTNE; FPLC=bw3NphcIY6Zo6AvmVDvum4vogDTNTQSG%2FTifL333v7Oi99uT3HJK05e1SMcP%2BJvlhhm0YtvRs3tgWBlXc6Ihbg2Z%2FArMARGwa6SOs%2FDY%2BUgE7TcJXk4u5doXRPDxPQ%3D%3D; __gads=ID=fdd047d6cb46d0a0:T=1744180585:RT=1744341944:S=ALNI_MZN-wkvYWjXxqm1M9lQ8ToxZO7X1w; __gpi=UID=0000109641273e07:T=1744180585:RT=1744341944:S=ALNI_MYQlCMNF7rcYyljo0131w0Vk9Dc0g; __eoi=ID=bcb4b1b74539936c:T=1744180585:RT=1744341944:S=AA-AfjY9wnPBz6_FcFdm-D6HODMP; cto_bundle=3v-d7l96WmU3ZWtCU09NTUFPVkg0JTJGSiUyRkFtYk9pQ1h0Q2NXUThhd1hpcFAlMkJZY25PNXolMkZ1b25PbUlpbGEzOHhDek94emlyZmM0a2RnWFZRbUVHdWZBOU93aFRHckhZNU10d1pXeDlmN3hyWUpHNGJFc0tJUjM4TTh2WUZZRHZEcmlEWmpM; aws-waf-token=74d088a2-61b8-4ead-9009-1fa85997f685:AAoAeOw1pYeHAQAA:T7isDLC1Hz5GVJLu9DSh0HfLQMvglW1JO1Vb21zKW9E5luDbCUJ1ugkRhEVvujg6u7uxNvHO1I4UrbUOl5NM1npuNta/o5a+k/tr9HEwuArKzK2ZakI7EaNbJAF2I3QmyyPsNRY3o8GOTrBEjJQsEJgiFpHKjJLHj97IgI966TbGxTvqjXiaqZtCQdshfEnWRPPrGvCSMHOhbFfDVO8kNspMTOEY5vp9QIpQ38xvC7NSrzYLfzw7uAyOYWgZG26/wJo=; _uetsid=f62b4680150c11f09ce1e30a0d6039e5; _uetvid=f62b5500150c11f091554b6b2d254434; _ga_A12345=GS1.1.1744357547.8.0.1744357547.0.0.272803723; lastSeen=1744357547748; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1744180581899&isGpcEnabled=0&datestamp=Fri+Apr+11+2025+14%3A45%3A50+GMT%2B0700+(Indochina+Time)&version=202501.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=3acef476-8d83-469d-a4cd-df95a4733d1c&interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _ga=GA1.2.454243668.1744180583; _gat=1; bkng=11UmFuZG9tSVYkc2RlIyh9Yaa29%2F3xUOLbVA9iGwA%2BUSzK9BhmDsoMc5mvBwvkRgJQWF4rFPaQdjWy%2FPl9%2FJHFeWkUEH9BDAfPagq3vRoRQm%2Bmpw9p88Rt9PTHL7C1FQW5BVu9D%2FX%2B7yXDkiBlDMpTcjxP2BY0Ri8GumF30dX7eSTe715ffz7agdenjjryWOJl5YRWjk7d9UM%3D; bkng=11UmFuZG9tSVYkc2RlIyh9YSvtNSM2ADX0BnR0tqAEmjvytXcXOj5IzLOywsHWhVnK8wzB%2BMMyG1SHa9G4tu9NXC3AtaULHjI%2FcFfssk%2BCbWF9NuZLH4EoTJ9E5st3q7q3oJq2rhrIwlYkcGNF8vcwTgWXmyq64iLNu%2BqFoP8RmmxyOgJrz32yXZxVzmOq6ytHzp7xHOGlDlS6abteqf4NTQ%3D%3D; bkng_sso_auth=CAIQ0+WGHxpmxEI9+hhUokiYLJOH9xWG4PcR9GROwXDMg3TDo3MtOMMnMmuQ5RevzC/VioFDddBLR7ch4XHhI4tFMj6e0b5rZz8jK4RdrbRCaHAEyl0QWxkYdw5bH91G7F5sqy6ouYwFDeGAH8WK'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text['item_id'])
