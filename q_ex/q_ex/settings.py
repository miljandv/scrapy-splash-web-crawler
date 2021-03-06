
BOT_NAME = 'q_ex'

SPIDER_MODULES = ['q_ex.spiders']
NEWSPIDER_MODULE = 'q_ex.spiders'

ROBOTSTXT_OBEY = False

SPLASH_URL = 'http://192.168.59.103:8050/'
#SPLASH_URL = 'http://localhost:8050'
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}
SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
