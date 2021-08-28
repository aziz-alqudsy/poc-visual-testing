from libs.config import configweb, browser
from libs.screenshot import Screenshot
from libs.analysis import Analysis

PRODUCTION_URL = "http://localhost:3000/register"
STAGING_URL = "http://localhost:3000/register/v2"

def test_register_page(browser):
    # open browser and save screenshot for production and staging
    Screenshot(browser).open(PRODUCTION_URL, 'ss_production')
    Screenshot(browser).open(STAGING_URL, 'ss_staging')

    # analysis grid image
    Analysis(browser).grid('grid_registerpage')
