import pytest
from django.urls import reverse, resolve
from profiles.views import index


@pytest.mark.django_db
def test_index_url(client):
    url = reverse("profiles:profiles_index")
    assert resolve(url).view_name == "profiles:profiles_index"
    assert resolve(url).func, index


@pytest.mark.django_db
def test_display_template_index(client):
    response = client.get(reverse("profiles:profiles_index"))
    assert response.status_code == 200
    assert b"<title>Profiles</title>" in response.content


@pytest.mark.django_db
def test_display_no_profiles(client):
    response = client.get(reverse("profiles:profiles_index"))
    assert b"No profiles are available." in response.content


@pytest.mark.django_db
def test_display_profiles(client, add_data):
    response = client.get(reverse("profiles:profiles_index"))
    assert b"AirWow" in response.content
    assert b"4meRomance" in response.content


@pytest.mark.django_db
def test_profile_url_in_index(client, add_data):
    response = client.get(reverse("profiles:profiles_index"))
    assert b'<a href="/profiles/4meRomance/">' in response.content
