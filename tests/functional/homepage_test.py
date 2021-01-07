import pytest
from flask import url_for


@pytest.mark.functional
def test_new_user_visit(browser, live_server):
    browser.get(url_for('main.home', _external=True))

    assert 'Dusri Naukari' in browser.title