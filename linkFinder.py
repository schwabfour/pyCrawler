#html parser to sift through websites
##html parsing libraries
#generic html parser class
from HTMLParser import HTMLParser
try:
    from urllib.parse import parse
except ImportError:
    from urlparse import urlparse

#create a class from parent; inherit from html parser with additional functionality

class LinkFinder(HTMLParser):
    #initializer
    def __init__(self):
        #initialize the super class
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        print (tag)
    

    #inherit this to ensure there's some error handling
    def error(self, message):
        pass
#create a linkfinder instance
finder = LinkFinder()
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

    