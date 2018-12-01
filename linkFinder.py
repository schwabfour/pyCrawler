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
    #initializer. the base_url is required for incomplete or relative urls
    def __init__(self, base_url, page_url):
        #initialize the super class
        HTMLParser.__init__(self)
        self.base_url=base_url
        self.page_url=page_url
        self.links=set()
    #override the default hand_starttag method
    def handle_starttag(self, tag, attrs):
        #if the tag is an anchor or links only
        if tag=='a':
            #store the attribute in a tuple
            for (attribute, value) in attrs:
                #we only want the url
                if(attribute=='href'):
                    #not all hrefs have full, usable urls aka relative urls, so check that
                    url=parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    #inherit this abstract method to ensure there's some error handling
    def error(self, message):
        pass
#create a linkfinder instance aka the html parser
finder = LinkFinder() 
#runs all of the functions on the feed arg; just a test ok
finder.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')
    