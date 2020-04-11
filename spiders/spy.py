import scrapy
from scrapy_splash import SplashRequest

class SpySpider(scrapy.Spider):
    name = 'spy'
    start_urls = ["http://example.com", "http://example.com/foo"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

    def parse(self, response):
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        # …
        pass