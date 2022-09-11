from __future__ import unicode_literals
from newsapp.service.content_filtering import preProcessing as tokenize
import requests
import codecs
import nltk
nltk.download('punkt')
from nltk import word_tokenize
class location(object):
    def __init__(self):
        pass
    def getLocation(self):
        URL = 'http://maps.googleapis.com/maps/api/geocode/json'
        URL1 = 'https://www.googleapis.com/geolocation/v1/geolocate'
        keys = 'AIzaSyABW87Cm0g6vwp1Lc7Fw5JI_DBygA4XcOk'
        PARAM = {'key': keys}
        rs = requests.post(url=URL1, params = PARAM)
        data = rs.json()

        latitude = data['location']['lat']
        longitude = data['location']['lng']
        str_list =[]
        str_list.append(str(latitude))
        str_list.append(str(longitude))
        latlng = ','.join(str_list)
        PARAM = {'latlng':latlng}

        r = requests.get(URL, params=PARAM)
        data = r.json()
        fomatted_address = data['results'][0]['address_components'][4]['long_name']
        print(fomatted_address)
        return fomatted_address

    def getLatitude(self):
        URL = 'http://maps.googleapis.com/maps/api/geocode/json'
        URL1 = 'https://www.googleapis.com/geolocation/v1/geolocate'
        #keys = 'AIzaSyABW87Cm0g6vwp1Lc7Fw5JI_DBygA4XcOk'
        keys = 'AIzaSyCV5kvNwepFshSFFlaYYA8sfRVN4b4iGGI'
        PARAM = {'key': keys}
        rs = requests.post(url=URL1, params=PARAM)
        data = rs.json()

        latitude = data['location']['lat']
        print(latitude)
        return str(latitude)

    def getLongitude(self):
        URL = 'http://maps.googleapis.com/maps/api/geocode/json'
        URL1 = 'https://www.googleapis.com/geolocation/v1/geolocate'
        keys = 'AIzaSyABW87Cm0g6vwp1Lc7Fw5JI_DBygA4XcOk'
        PARAM = {'key': keys}
        rs = requests.post(url=URL1, params=PARAM)
        data = rs.json()

        longitude = data['location']['lng']
        print(longitude)
        return str(longitude)

    def calculate_top_documents(self):
        location = self.getLocation()

    def setNewsLocation(self,top_news):
        tokenize = lambda doc: doc.lower().split(" ")
        with codecs.open('C:/Users/aditi/Desktop/atlas.txt', 'r', encoding='utf-8', errors='ignore') as fdata:
            for s in fdata:
                s = s.strip()
                city_list = s.split(',');
                for city in city_list:
                    city = city.strip()
                    for news in top_news:
                        tokenized = tokenize(news.desc)
                        for token in tokenized:
                            loc_token = ''.join(c for c in token if c.isalpha())
                            if loc_token.lower() == city.lower():
                                print(loc_token)


