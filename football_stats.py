from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request('https://www.cbssports.com/nfl/stats/playersort/nfl/year-2018-season-regular-category-touchdowns')
response = urllib2.urlopen(req)
the_page = response.read()

soup = BeautifulSoup(the_page, features="lxml")

final_link = soup.a
final_link.decompose()

trs = soup.find_all('tr')

for tr in trs:
    tds = tr.find_all("td")

    try:
        pos_0 = str(tds[0].get_text())
        pos_1 = str(tds[1].get_text())
        pos_6 = str(tds[6].get_text())
    except:
        #print "bad tr string"
        continue #

    print pos_0, pos_1, pos_6
