import scrapy 
#from scrapy.crawler import CrawlerProcess

class CLSpider( scrapy.Spider ):
    name = 'clspider'
    start_urls = [
                'https://boston.craigslist.org/search/gbs/lgl',
    ]
    def parse ( self, response):
        for job in response.css('a.result-title.hdrlnk'):
            yield {
                    'title': job.css('::text').get(),
                    'link': job.css('::attr(href)').get(),
            }


    #def parse ( self, response ):
        #filename="clegal_jobs.txt"
        #with open(filename, 'wb') as f:
        #    for job in response.css('a.result-title.hdrlnk'):
        #        f.write(job.css('::text').get())
