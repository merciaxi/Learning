from urllib import request
from requests_html import HTMLSession


s = HTMLSession()
city = ["Aberdeen", "Abilene", "Akron", "Albany", "Albuquerque", "Alexandria", 
        "Allentown", "Amarillo", "Anaheim", "Anchorage", "Ann Arbor", "Antioch"]



for element in range(len(city) - 1):
    print(city[element])
    url = 'https://www.google.com/search?q=weather+' + city[element] 

    req = s.get(url, headers={'User-Agent': 'Add your user agent')
    weather = req.html.find('div.vk_bk.TylWce.SGNhVe span#wob_tm', first=True).text
   

    Weathers_dict = [city].append(weather)
