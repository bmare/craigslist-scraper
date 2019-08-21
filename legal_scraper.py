import scrapy 
from scrapy.crawler import CrawlerProcess

class CLSpider( scrapy.Spider ):
    name = 'clspider'
    lgl_jobs=[]
    def start_requests ( self ):
        url = 'https://boston.craigslist.org/search/gbs/lgl'
        yield scrapy.Request( url = url, callback = self.parse )
    def parse ( self, response ):
        filename='craigslist_links.txt'
        with open(filename, 'wb') as f:
            f.write(response.css('a.result-title.hdrlink::text'))
        self.log('Saved file %s' % filename)
