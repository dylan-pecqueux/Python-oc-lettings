import pytest
from django.urls import reverse, resolve
from lettings.views import index


@pytest.mark.django_db
def test_index_url(client):
    url = reverse("lettings:lettings_index")
    assert resolve(url).view_name == "lettings:lettings_index"
    assert resolve(url).func, index


@pytest.mark.django_db
def test_display_template_index(client):
    response = client.get(reverse("lettings:lettings_index"))
    assert response.status_code == 200
    assert b"<title>Lettings</title>" in response.content


@pytest.mark.django_db
def test_display_no_lettings(client):
    response = client.get(reverse("lettings:lettings_index"))
    assert b"No lettings are available." in response.content


@pytest.mark.django_db
def test_display_lettings(client, add_data):
    response = client.get(reverse("lettings:lettings_index"))
    assert b"Joshua Tree Green Haus /w Hot Tub" in response.content
    assert b"Oceanview Retreat" in response.content


@pytest.mark.django_db
def test_letting_url_in_index(client, add_data):
    response = client.get(reverse("lettings:lettings_index"))
    assert b'<a href="/lettings/1/">' in response.content
