import pytest
from django.urls import reverse, resolve
from lettings.views import letting


@pytest.mark.django_db
def test_index_url(client, add_data):
    url = reverse("lettings:letting", args=[1])
    assert resolve(url).view_name == "lettings:letting"
    assert resolve(url).func, letting


@pytest.mark.django_db
def test_display_template_letting(client, add_data):
    response = client.get(reverse("lettings:letting", args=[1]))
    assert response.status_code == 200
    assert b"<title>Joshua Tree Green Haus /w Hot Tub</title>" in response.content


@pytest.mark.django_db
def test_display_url_in_letting(client, add_data):
    response = client.get(reverse("lettings:letting", args=[1]))
    assert b'<a href="/lettings/">Back</a>' in response.content
    assert b'<a href="/">Home</a>' in response.content
    assert b'<a href="/profiles/">Profiles</a>' in response.content
