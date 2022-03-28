import string
import re
import json
import urllib.request
import time
import os
import os.path
from os import path
import requests

categories_names = [
    "burgers",
    "sushi",
    "hummus",
    "asian",
    "pizza",
    "dessert",
    "salad",
    "homemade",
    "pasta",
    "italian",
    "kosher",
    "sandwich",
    "mexican",
    "thai",
    "healthy",
    "mediterranean",
    "vegetarian",
    "noodles",
    "breakfast",
    "vegan",
    "indian",
    "japanese",
    "soup",
    "cafe"
]

def safeAtrr(myObj, attName):
    try:
        val = myObj[attName]
        return val
    except:
        return "no such attribute"


def main():
    # download raw json object
    where = 1
    for cat in categories_names:
        parent_dir = "C:/picky/getJsonMenus/results"
        path = os.path.join(parent_dir, cat)
        if os.path.exists(path) is False:
            os.mkdir(path) 
            print("Directory '% s' created" % cat)

        url = "https://restaurant-api.wolt.com/v1/pages/venue-list/category-" + cat + ":tel-aviv"
        data = urllib.request.urlopen(url).read().decode()

        # parse json object
        obj = json.loads(data)

        f = open("C:/picky/getJsonMenus/results" + "/" + cat + "/" + cat + ".txt", "w")
        f.write(data)
        f.close()
        where = where + 1
        if where == 5:
            time.sleep(10)
            where = 1

    sections = obj['sections']
    for section in sections:
        all_section_items = section["items"]
        for item in all_section_items:
            rest_title = safeAtrr(item, "title") #needed as is
            more_details = safeAtrr(item, "venue")

            rest_address = safeAtrr(more_details, "address") #needed as is
            rest_city = safeAtrr(more_details, "city") #needed as is
            rest_currency = safeAtrr(more_details, "currency") #needed as is
            rest_isDelivering = safeAtrr(more_details, "delivers")
            rest_delivery_price = safeAtrr(more_details, "delivery_price")
            rest_estimate = safeAtrr(more_details, "estimate") #needed as is
            rest_estimate_range = safeAtrr(more_details, "estimate_range") #needed as is
            rest_location = safeAtrr(more_details, "location") #needed as is
            rest_name = safeAtrr(more_details, "name") #needed as is
            rest_short_description = safeAtrr(more_details, "short_description") #needed as is
            rest_slug = safeAtrr(more_details, "slug")
            rest_tags = safeAtrr(more_details, "tags")

            # download raw json object
            for cat in categories_names:

                url = "https://restaurant-api.wolt.com/v3/venues/slug/" + rest_slug
                data = urllib.request.urlopen(url).read().decode()

                # parse json object
                obj = json.loads(data)
                my_results = safeAtrr(obj, "results")
                relevant_result = my_results[0]
                item_delivery_enabled = safeAtrr(relevant_result, "delivery_enabled")
                print(obj)
                break
    f = open("burgers.txt", "r")
    print(json.loads(f.read())["show_map"])




if __name__ == "__main__":
    main()