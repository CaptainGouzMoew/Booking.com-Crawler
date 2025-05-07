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

def slugify_city_name(city):
    return city.lower().replace(' ', '-')

cities = [slugify_city_name(city) for city in cities]
# print(cities)