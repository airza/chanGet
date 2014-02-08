import requests
from bs4 import BeautifulSoup
import sys
import os

folderName = sys.argv[1] + '-' + sys.argv[2]
os.mkdir(folderName)
r = requests.get("http://boards.4chan.org/%s/res/%s" % (sys.argv[1],sys.argv[2]))
soup = BeautifulSoup(r.text)
imgUrls = ['http:' + r['href'] for r in soup.findAll(class_ = "fileThumb")]
for image in imgUrls:
    print image
    fname = image.split("/")[-1]
    r = requests.get(image)
    f  = open(folderName + "/"  + fname,"w")
    f.write(r.content)
    f.close()