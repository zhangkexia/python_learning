from urllib.request import urlopen
from xml.etree.ElementTree import parse


# download the rss feed and parse it
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

# extract and output tags of interest
for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()