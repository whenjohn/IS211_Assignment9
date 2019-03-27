from bs4 import BeautifulSoup
import urllib2

req = urllib2.Request('https://www.nasdaq.com/symbol/aapl/historical')
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
        pos_4 = str(tds[4].get_text())
    except:
        #print "bad tr string"
        continue #

    print pos_0.strip(), pos_4.strip()
