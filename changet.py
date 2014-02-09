import requests
from bs4 import BeautifulSoup
import sys
import os

r = requests.get("http://boards.4chan.org/%s/res/%s" % (sys.argv[1],sys.argv[2]))
if r.status_code == 404:
    print("Couldn't find thread!")
    exit(-1)
folderName = sys.argv[1] + '-' + sys.argv[2]
try:
    os.mkdir(folderName)
except OSError:
    pass
os.chdir(folderName)
soup = BeautifulSoup(r.text)
imgUrls = ['http:' + r['href'] for r in soup.findAll(class_ = "fileThumb")]

template= "<img src='%s'><br>%d<br>"
pfile = open("index.html","a")
for n,image in enumerate(imgUrls):
    print(image)
    fname = image.split("/")[-1]
    if os.path.exists(fname):
        continue
    r = requests.get(image)
    f  = open(fname,"wb")
    f.write(r.content)
    f.close()
    pfile.write(template % (fname,n))
pfile.close()