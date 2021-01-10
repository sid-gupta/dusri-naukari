from flask import url_for

from tests.test_utils.route_to_view import route_from


def test_root_url_resolves_to_home_page_view():
    endpoint, args = route_from('/')
    assert endpoint == 'main.home'


def test_home_page_returns_correct_template(client, templates):
    client.get(url_for('main.home'))
    rendered_template, contexts = templates[0]
    assert rendered_template.name == 'index.html'
