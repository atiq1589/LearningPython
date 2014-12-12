import urllib2
from urllib2 import urlopen
import re
import cookielib
import xlwt
from cookielib import CookieJar


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

def GetSourceCode(page):
    try:
        sourceCode = opener.open(page).read()
        return sourceCode
    except Exception, e:
        print str(e)
        print "Failed in 1st Try [GetSourceCode]"

def ParseICSData(sourceCode):
    colList = []
    #cols = raw_input("Please Enter Columns separeted by coma(,): ")
    #cols = cols.split(',')
    #numberOfCol = 0
    #for col in cols:
    #    colList.append(col)
    #    numberOfCol += 1

    data = re.split('\(?(.*?)\)?',sourceCode)
    i = 0
    #book = xlwt.Workbook()
    #sh = book.add_sheet("abalone")
    #for col in colList:
        #sh.write(0, i, col)
    #    i += 1
    i = 0
    for d in data:
    #    col = i % numberOfCol
    #    row = i / numberOfCol
        print d
        #sh.write(row + 1, col, d)
        i += 1

    #book.save("Abalone.xls")
def main():
    #page = raw_input("Please Input The Url: ")
    page = "http://archive.ics.uci.edu/ml/machine-learning-databases/university/university.data"
    sourceCode = GetSourceCode(page)
    ParseICSData(sourceCode)




main()