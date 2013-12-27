import os
import celery
from scrapy.settings import CrawlerSettings
from scrapy.crawler import CrawlerProcess

# configure tasks by using celeryconfig module
app = celery.Celery()
app.config_from_object('celeryconfig')

scrapy_settings = os.environ.get('OPENSHIFT_SCRAPY_SETTINGS')

@app.task
def addtest(x, y):
    return x + y

@app.task
def run_spiders(name, **kwargs):
    """
    @param name: spider name
    """
    prs = CrawlerProcess( CrawlerSettings(scrapy_settings) )
    crawler = prs.create_crawler()
    for spdname, spd in crawler.spiders._spiders.iteritems():
        if name == spdname:
            spidercls = spd
    crawler.crawl( spidercls(**kwargs) )
    prs.start()
