import selenium.webdriver
import pytest
import json

@pytest.fixture
def configweb(scope='session'):
    # read config file json
    with open('libs/configweb.json') as config_file:
        configweb = json.load(config_file)

    # validate value that acceptable
    assert configweb['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(configweb['implicit_wait'], int)
    assert configweb['implicit_wait'] > 0

    return configweb

@pytest.fixture
def browser(configweb):
    # setup webdriver instance
    if configweb['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif configweb['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif configweb['browser'] == 'Headless Chrome':
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception('Browser {0} is not supported'.format(configweb['browser']))

    driver.implicitly_wait(configweb['implicit_wait'])

    yield driver

    # teardown
    driver.quit()
