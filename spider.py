#spiderboi
#grabs all of the links from the linkfider and adds the files to the waiting list
#then it takes the data from the waiting list (aka queue)and puts it into the crawled list
#the plan is to make a bunch of instances of the spider

#allos you to connect to web pages 
from urllib2 import urlopen
#link finder
from linkFinder import LinkFinder
#not sure why this is needed
from general import *

class Spider:
    #class variables (Shared among all instances)
    
    #user will pas this in
    project_name = ''
    base_url = ''
    domain_name= ''
    queue_file = ''
    crawled_file = ''
    queue = set() # the set will help avoid writing to a file each time a url is found
    crawled = set()

    #initializer
    ##domain functions will help ensure we're at a real site
    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('Initial Spider', Spider.base_url) 
        #spider 1 doesn't require a thread. The rest tho..

    #it would be best to make this static..?
    @staticmethod
    def boot(self):
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        if(page_url not in Spider.crawled):
            print(thread_name+' crawling '+ page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled '+ str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
    
    @staticmethod
    def gather_links(page_url):
        #need to convert the bytes from the sites back to human readable.
        html_string = ''
        try:
            #connect to the page and store teh response here in byte data
            response = urlopen(page_url)
            if response.getheader('Content-Type')=='text/html':
                html_bytes = response.read()
                #convert bytes to string english human readable encoding
                html_string = html_bytes.decode("utf-8")
            #create a link finder object and pass it the two requried args
            finder = LinkFinder(Spider.base_url, page_url)
            #call feed to pass in the html data for parsing
            finder.feed(html_string)
        except:
            print('Error: cannot crawl page due to some internet issue')
            #return an empty set because we need to deliver something.
            return set()
        return finder.page_links()

    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
