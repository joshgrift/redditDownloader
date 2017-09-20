'''
Pass subreddit as single argument.
Ex: /r/EarthPorn/hot.json

Created by @dotjersh
'''

import json
import ssl
import sys
import urllib.error
import urllib.request


def getUrl(url):
    gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)  # Only for gangstars
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req, context=gcontext)
        return response.read()
    except urllib.error.URLError:
        return False


def saveImages(url, path):
    data = getUrl(url)

    if data != False:
        j = json.loads(data)

        for post in j["data"]["children"]:
            if post["data"]['url'].find(".jpg") > 0:
                contents = getUrl(post["data"]["url"])
                if contents:
                    im = open(path + post["data"]["id"] + '.jpg', "wb")
                    im.write(contents)
                    im.close()
                    print('Image Saved (' + post["data"]['url'] + ")")
                else:
                    print('Error: not saved (' + post["data"]['url'] + ")")

            else:
                print('Image Skipped (' + post["data"]['url'] + ")")

        print('Download Complete')
    else:
        print('Network Error')


path = ""

if(len(sys.argv) < 1):
    url = 'https://www.reddit.com/r/EarthPorn/hot.json'
else:
    url = 'https://www.reddit.com' + sys.argv[1]

print("Downloading images from " + url)
saveImages(url, path)
