from requests import request
import re

def webScrape(url):
    webPath = open("webPath.txt","r")
    paths = webPath.read().split("\n")
    webPath.close()

    phNum = '\+?\d?\s?\(?\d{3}\)?\s?\-?\d{3}\s?\-?\d{4}'
    email = '\w+\@\w+\.?\w+\.\w{3}'
    for path in paths:
        response = request("GET", url+"/"+path)
        if response.status_code == 200:
            phoneNums = re.findall(phNum, str(response.content))
            emails = re.findall(email, str(response.content))
            print ('URL: ' + response.url + ' , HTTP Status Code: ' + str(response.status_code))
            print ('Phone Numbers Found: ' + str(phoneNums))
            print ('Emails Found: ' + str(emails))

webScrape('https://www.secdaemons.org')
