import pytest
from django.urls import reverse, resolve
from profiles.views import profile


@pytest.mark.django_db
def test_index_url(client, add_data):
    url = reverse("profiles:profile", args=["4meRomance"])
    assert resolve(url).view_name == "profiles:profile"
    assert resolve(url).func, profile


@pytest.mark.django_db
def test_display_template_profile(client, add_data):
    response = client.get(reverse("profiles:profile", args=["4meRomance"]))
    print(response.content.decode())
    assert response.status_code == 200
    assert b"<title>4meRomance</title>" in response.content


@pytest.mark.django_db
def test_display_url_in_letting(client, add_data):
    response = client.get(reverse("profiles:profile", args=["4meRomance"]))
    assert b'<a href="/profiles/">Back</a>' in response.content
    assert b'<a href="/">Home</a>' in response.content
    assert b'<a href="/lettings/">Lettings</a>' in response.content


@pytest.mark.django_db
def test_display_url_in_letting(client, add_data):
    response = client.get(reverse("profiles:profile", args=["4meRomance"]))
    assert b"First name: John" in response.content
    assert b"Last name: Rodriguez" in response.content
    assert b"Email: coemperor@famemma.net" in response.content
    assert b"Favorite city: Berlin" in response.content
