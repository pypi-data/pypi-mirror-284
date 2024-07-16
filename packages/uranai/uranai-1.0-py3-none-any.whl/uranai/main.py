import json
import requests
from bs4 import BeautifulSoup

class Uranai():
    def __init__(self, proxy:dict = None):
        
        self.proxy = proxy

    def do(self):

        response = requests.get('https://www.asahi.com/uranai/12seiza/', proxies=self.proxy)
        soup = BeautifulSoup(response.content, 'html.parser')
        yotei = soup.find("ol", class_="UranaiRank")
        a_tags = yotei.find_all('a')
        count = 0
        seiza = ""
        uranai_result = {}

        for a_tag in a_tags:
            href = a_tag.text

            if "座" in href:
                count = count + 1
                seiza = href
                json_add = {href : None}
                uranai_result.update({f"{count}位" : json_add})

            elif href == "詳しく":
                href = a_tag.get('href')
                href = "https://www.asahi.com" + str(href)
                uranai_result[f"{count}位"].update({seiza : href})

        return uranai_result