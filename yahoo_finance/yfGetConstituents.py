import urllib2
import re

# symbol = the yahoo ticker; the expected tickers of the
# components contain alphanumerical characters or dot or hyphen;
# if the yahoo format changes, nothing is returned
def getConstituentsOfAnIndexFromYahoo(symbol):
    url = 'http://finance.yahoo.com/q/cp?s=%s' % symbol
    p = re.compile('<td class=\"yfnc_tabledata1\"><b><a href=\"/q\?s=([A-Z0-9\.\-]*)\">')    
    components = []    
    pageIndex = 0
    finished = False
    while not finished:
        if pageIndex == 0: 
            actualUrl = url
        else:
            actualUrl = url + "&c=" + str(pageIndex)
        pageResults = p.findall(urllib2.urlopen(actualUrl).read())
        if len(pageResults) == 0:
            finished = True
        else:
            components.extend(pageResults)
            pageIndex+=1
    return components

if __name__ == "__main__":
    print getConstituentsOfAnIndexFromYahoo("^GDAXI")