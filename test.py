from geolocation.main import GoogleMaps
import j

with open('AI-Pixel/api_keys.json') as API:
    API = json.load(API)
    key = API['geocode']

### When registering
## ask user for: 
#   location
#   name
