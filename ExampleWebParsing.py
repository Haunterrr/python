from urllib import request, parse
import sys

myUrl = "https://www.google.com/search?"
value = {'q': 'Disturbed'}

myheader = {}
myheader['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'

try:
    mydata = parse.urlencode(value)
    print(mydata)
    myUrl = myUrl + mydata
    req = request.Request(myUrl, headers=myheader)
    answer = request.urlopen(req)
    answer = answer.readlines()
    for line in answer:
        print(line)
except Exception:
    print("Error occuried during web request!!!")
    print(sys.exc_info()[1])
