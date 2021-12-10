import pytest
from django.urls import reverse, resolve
from oc_lettings_site.views import index


@pytest.mark.django_db
def test_index_url(client):
    url = reverse("index")
    assert resolve(url).view_name == "index"
    assert resolve(url).func, index


@pytest.mark.django_db
def test_display_template_profile(client):
    response = client.get(reverse("index"))
    print(response.content.decode())
    assert response.status_code == 200
    assert b"<title>Holiday Homes</title>" in response.content


@pytest.mark.django_db
def test_display_url_in_letting(client):
    response = client.get(reverse("index"))
    assert b'<a href="/profiles/">Profiles</a>' in response.content
    assert b'<a href="/lettings/">Lettings</a>' in response.content
