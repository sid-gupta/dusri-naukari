import pytest
from selenium import webdriver

from app.app import create_app
from app.extensions import db
from tests.test_utils.capture_template import captured_template


@pytest.fixture(scope="session", autouse=True)
def app():
    naukari_app = create_app('testing')
    with naukari_app.app_context():
        # db.drop_all()
        # db.create_all()
        pass
    yield naukari_app


@pytest.fixture()
def browser():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()


@pytest.fixture()
def templates(app):
    with captured_template(app) as rendered_templates:
        yield rendered_templates
