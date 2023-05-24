from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
import pytest
import os
driver = None

@pytest.fixture(scope="function", autouse=True)
def fisrstone(request):
    global driver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(10)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        extra.append(pytest_html.extras.url("https://riindia.co.in/"))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="{}" alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'.format(file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "my report"












