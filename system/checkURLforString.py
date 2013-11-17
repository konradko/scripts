# Checks if url object contains the specified string and returns value for Hostmonitor
import urllib


def checkURLforString(url, stringToFind):
    if stringToFind in urllib.urlopen(url).read():
        return "'%s' found in %s" % (stringToFind, url)
    else:
        return "'%s' not found in %s" % (stringToFind, url)

if __name__ == "__main__":
    print checkURLforString("http://lists.korzel.com", "Start")