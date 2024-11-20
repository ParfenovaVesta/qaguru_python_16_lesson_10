import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_options():
    browser.config.base_url = "https://github.com/"

    yield

    browser.quit()
