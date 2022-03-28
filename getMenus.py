import string
import re
import json
import urllib.request as urllib2
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
    #"dessert",
    #"salad",
    #"homemade",
    #"pasta",
    #"italian",
    #"kosher",
    #"sandwich",
    #"mexican",
    #"thai",
    #"healthy",
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
        print("my cat is: " + cat)
        flag = False
        my_dir = "C:/picky/getJsonMenus/results/" + cat + "/restaurants"
        many = 0
        for filename in os.listdir(my_dir):
            print("filename: " + filename)
            f = open(my_dir + "/" + filename, "r")
            menu_id = json.loads(f.read())["results"][0]["active_menu"]["$oid"]

            print("my id: " + menu_id)

            #call api
            many = many + 1
            if many == 10:
                time.sleep(8)
                many = 0
            url = "https://restaurant-api.wolt.com/v3/menus/" + menu_id
            headers = {'authority': 'restaurant-api.wolt.com', 'method': 'GET', 'path': '/v3/menus/' + menu_id, 'scheme': 'https', 'accept': 'application/json, text/plain, */*', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9', 'app-language': 'en', 'authorization': 'Bearer eyJ0eXAiOiJ4LnVzZXIrand0IiwiYWxnIjoiRVMyNTYiLCJraWQiOiI3MWIyZWQwYTY2ZTUxMWViYjVkZjNlY2VhNzVlMmJhZSJ9.eyJhdWQiOlsicmVzdGF1cmFudC1hcGkiLCJ3b2x0YXV0aCIsImNvdXJpZXJjbGllbnQiXSwiaXNzIjoid29sdGF1dGgiLCJqdGkiOiIzYTk3MmE5MjZkZmQxMWViYjY5ZWU2YWQxNGIzMTBiZiIsInVzZXIiOnsiaWQiOiI1ZjQxNDI0YzNjNjY1OWRkMjYyZjJhNjEiLCJuYW1lIjp7ImZpcnN0X25hbWUiOiJFbGlyYW4iLCJsYXN0X25hbWUiOiJLZG9zaGltIn0sImVtYWlsIjoiZWxpcmFueTlAd2FsbGEuY28uaWwiLCJyb2xlcyI6WyJ1c2VyIl0sImxhbmd1YWdlIjoiZW4iLCJwcm9maWxlX3BpY3R1cmUiOnsidXJsIjoiaHR0cHM6Ly9jcmVkaXRvcm5vdG1lZGlhLnMzLmFtYXpvbmF3cy5jb20vNTczMDE2YmY4MjQzYmVjZWI1OGMwODMwZTU4MjJjZWRkNjc2NWIyZjY1ZTY4MzM1NDZhMGE2NjYxZDRkN2U1ZDFlZGZjNWJmMTg0Y2E4MWFmZDlkOTJkNjFkMjZjMWYwOTU3YzBkZTMwNDI4NGJjYzIyYjFmYjRlZGY3NDU2OWEifSwicGVybWlzc2lvbnMiOltdLCJwaG9uZV9udW1iZXIiOiIrOTcyNTA3NDE2NjY1IiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjp0cnVlLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImNvdW50cnkiOiJJU1IifSwicGF5bG9hZCI6ImI3Q05QTTNTWTBUaWpXR1JjNHVnazljQ0NIL0YyeHVrRjU3eHNZL2VLOURtTmhKS1I3aGJoSHpmbXFxU2NFellpdUlqVUR2NmtUS3pWN095ZTdDZWxVR3R2blAydjFVaFY5ZHM5SUdhaFY1ZVNVeFBhWGlpT1ppQ0N4ZTlvalNwRDROb3ZRb3NYLzcyWThYZWxObGQySUQ4ZlJHV3h6YktPY0NJVnYzRmYxcFQ3aU1pWEFvVSttaVplNWxkMWhJZXp3V0YzZDhFL09GYWVwWFhXWmNQczdnaTc1ZHZRcjk5bDdqNHd0Vlg3eTdpNEh0ajU0STAzTXdxWHVhVERndnJHbDUydWdIN3M3dVZubVplOTlDWnVSdWUxbEUyMXZVK0ZkTW8xZXBGZnhWNkxhRmpqSXA2Snc9PSIsImlhdCI6MTYxMzIyMTk5NCwiZXhwIjoxNjEzMjIzNzk0fQ.-YQ5weOGnpBQwz7qcJ_MmsE0_vwEnuPoby5xxv1MCK4xm6UrEdDB56vJggLzt_y2mqpvLAOBNEPxRzcWhrbMbg', 'origin': 'https://wolt.com', 'platform': 'Web', 'referer': 'https://wolt.com/', 'w-wolt-session-id': 'f8a28cc2-0abf-4ba0-9873-0866d0f49527'}
            r = requests.get(url, headers=headers)
            data = r.text
            if "Error" in data: 
                print("Error")
            #save menu json to txt file
            f = open("C:/picky/getJsonMenus/results" + "/" + cat + "/menues/" + filename, "w")
            f.write(data)
            f.close()

        #f = open(parent_dir + "/" + cat + "/restaurants/" + ".txt", "r")
        #the_json_cat = json.loads(f.read())
        #sections = the_json_cat["sections"]
        #call_number = 0
        #for section in sections:
        #    call_number = call_number + 1
        #    if call_number == 10:
        #        time.sleep(8)
        #    all_section_items = section["items"]
        #    for item in all_section_items:
        #        more_details = safeAtrr(item, "venue")
        #        rest_slug = safeAtrr(more_details, "slug")

        #        print("now: " + rest_slug)
        #        #get menues
        #        url = "https://restaurant-api.wolt.com/v3/venues/slug/" + rest_slug
        #        data = urllib.request.urlopen(url).read().decode()
        #        f = open("C:/picky/getJsonMenus/results" + "/" + cat + "/restaurants/" + rest_slug + ".txt", "w")
        #        f.write(data)
        #        f.close()

if __name__ == "__main__":
    main()

