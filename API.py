import requests
import json
api_key = "tOZcsPV3rSgL5zlnIFAXx4HTt4AhdxRJpLN6D9vsN5hm1jOP1skN_Dj26WpkVTe2iKoeoGD3HJiB1PgzgEo6rnmrtxrNp-R2joKST-oTSXLDUBowsWp15jiWKXuuYXYx"
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'

params = {}
params["type"] = input("Enter the type of business you want to search for (ex. 'coffee'): ")
params["location"] = input("Enter the location of where you want to search (ex. 'Charlottesville, Virginia'): ")

print()
print("Here are the search results for", params["type"], "businesses in", params["location"], "with a rating of 4.0 or higher: ")
print()

#making a get request to the API
request = requests.get(url, params = params, headers = headers)
data = json.loads(request.text)

#get list of businesses 
businesses = data["businesses"]
 
#print businesses' names, addresses, and phone number if they have a rating higher than 4.0
for business in businesses:
    if business["rating"] >= 4:
        print("Name:", business["name"])
        print("Address:", " ".join(business["location"]["display_address"]))
        print("Phone:", business["phone"])
        print("\n")