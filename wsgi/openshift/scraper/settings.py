#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os,tempfile

ON_OPENSHIFT = False
DJANGO_APP_NAME = 'openshift'
TMP_DIR = '/tmp'
IMAGES_STORE = os.path.join( os.path.dirname(__file__), 'images')
if os.environ.has_key('OPENSHIFT_REPO_DIR'):
    ON_OPENSHIFT = True
    TMP_DIR = os.environ['OPENSHIFT_TMP_DIR']
    IMAGES_STORE = os.environ['OPENSHIFT_DATA_DIR']+'images/'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{0}.settings".format(DJANGO_APP_NAME)) #Changed in DDS v.0.3

SPIDER_MODULES = ['dynamic_scraper.spiders', 'openshift.scraper',]
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11' 


ITEM_PIPELINES = [
        'dynamic_scraper.pipelines.DjangoImagesPipeline',
        'dynamic_scraper.pipelines.ValidationPipeline',
        ]

IMAGES_THUMBS = {
        'small': (170, 170),
        }

EXTENSIONS = {
        'scrapy.webservice.WebService':None,
        'scrapy.telnet.TelnetConsole':None,
        }

LOG_FILE = tempfile.mkstemp(dir=TMP_DIR, prefix=DJANGO_APP_NAME)[1]
