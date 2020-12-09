from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import sys
import json

gye = "gyevha"
wong = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36'}
r = requests.get("https://www.smule.com/"+gye+"/performances/json")
data = json.loads(r.text)
web = data["list"][2-1] #ini no oc nya jika ingin menggunakan perintah tinggal buat def nama bebas contoh def nama //bangsat //web = data["list"][bangsat-1]
if 'video' in web['type']:
    link = str(web["web_url"])
    url = "https://www.smule.com{}".format(link)
    soup = BeautifulSoup(urlopen(Request(url,headers=wong)), "lxml")
    collab_link = soup.find(attrs={"name": "twitter:player:stream"})['content']
    print(collab_link)#sendVideoWithURL
else:
    link = str(web["web_url"])
    url = "https://www.smule.com{}".format(link)
    soup = BeautifulSoup(urlopen(Request(url,headers=wong)), "lxml")
    collab_link = soup.find(attrs={"name": "twitter:player:stream"})['content']
    print(collab_link)#;else:try:#sendAudioWithURL
    r = requests.get("https://www.smule.com/"+gye+"/performances/json")
    data = json.loads(r.text)
    mc = ""
    b = 0
    asw = 'Smule List:\n\n'
    for web in data["list"]:
        b = b + 1
        end = "\n"
        title = web["title"]
        mc += (str(b)+ ". "+ title+ "\n")
    print(asw + mc)#self.client.sendMessage
