import urllib.request
from xml.dom import minidom


def parse_valute():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    webFile = urllib.request.urlopen(url)
    data = webFile.read()
    UrlSplit = url.split("/")[-1]
    ExtSplit = UrlSplit.split(".")[1]
    FileName = UrlSplit.replace(ExtSplit, "xml")
    with open(FileName, "wb") as localFile:
        localFile.write(data)
    webFile.close()


def get_valute(val='USD'):
    parse_valute()
    doc = minidom.parse("XML_daily.xml")
    valute_array = doc.getElementsByTagName("Valute")
    for each_Val in valute_array:
        value = each_Val.getElementsByTagName("Value")[0]
        name = each_Val.getElementsByTagName("CharCode")[0]
        if name.firstChild.data == val:
            # print(name.firstChild.data, " = ", value.firstChild.data)
            return value.firstChild.data
