import string
import re
import json
import urllib.request
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import os.path
from os import path
import requests

categories_names = [
    #"burgers",
    #"sushi",
    #"hummus",
    #"asian",
    #"pizza",
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
    for cat in categories_names:
        parent_dir = "C:/picky/getJsonMenus/results"
        f = open(parent_dir + "/" + cat + "/" + cat + ".txt", "r")
        the_json_cat = json.loads(f.read())
        sections = the_json_cat["sections"]
        call_number = 0
        for section in sections:
            call_number = call_number + 1
            if call_number == 10:
                time.sleep(8)
            all_section_items = section["items"]
            for item in all_section_items:
                more_details = safeAtrr(item, "venue")
                rest_slug = safeAtrr(more_details, "slug")

                print("now: " + rest_slug)
                #get menues
                url = "https://restaurant-api.wolt.com/v3/venues/slug/" + rest_slug
                data = urllib.request.urlopen(url).read().decode()
                f = open("C:/picky/getJsonMenus/results" + "/" + cat + "/restaurants/" + rest_slug + ".txt", "w")
                f.write(data)
                f.close()

if __name__ == "__main__":
    main()


