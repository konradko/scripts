# yfGet.py
# Gets finance.yahoo.com historical stock data and appends output to a file
# Venue,Symbol,Date,OpenPrice,ClosePrice

import urllib
import datetime
import sys

def timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Returns "Date,OpenPrice,ClosePrice" from Yahoo Finance API
def yfGet(symbol, date):
    url = "http://ichart.yahoo.com/table.csv?s=%s&" % symbol + \
          "d=%s&" % str(int(date[4:6]) - 1) + \
          "e=%s&" % str(int(date[6:8])) + \
          "f=%s&" % str(int(date[0:4])) + \
          "g=d&" + \
          "a=%s&" % str(int(date[4:6]) - 1) + \
          "b=%s&" % str(int(date[6:8])) + \
          "c=%s&" % str(int(date[0:4])) + \
          "ignore=.csv"
    lines = urllib.urlopen(url).readlines()
    data = [line[:-2].split(",") for line in lines]
    return data[1][0].replace("-","") + "," + data[1][1] + "," + data[1][4]

def output(text, outputFile):
    with open(outputFile, 'a') as dest:
        dest.write(text + "\n")

def log(text, logFile="yfGet.log"):
    with open(logFile, "a") as dest:
        dest.write('%s: %s\n' % (timestamp(), text))


if __name__ == "__main__":
    # IFS to Yahoo symbol mapping
    symbols = ("VOD.L",
               "BMW.DE",
               "UCG.MI",
               "NESN.VX",
               "REP.MC",
               "FRO.OL",
               "FLS.CO",
               "ERIC-B.ST",
               "WIE.VI")

    priceDate  = (datetime.date.today()-datetime.timedelta(1)).strftime("%Y%m%d")

    log("yfGet.py starting...")

    for symbol in symbols:
        try:
            log("Downloading Yahoo prices for %s" % symbol)
            output(yfGet(symbol, priceDate))
        except Exception:
            log("Download failed for %s!" % symbol)
            sys.exc_clear()

    log("yfGet.py finished!")