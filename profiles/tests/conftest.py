import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.fixture
def add_data():
    user_1 = User.objects.create(
        username="4meRomance",
        password="azerty",
        first_name="John",
        last_name="Rodriguez",
        email="coemperor@famemma.net",
        is_active=True,
    )

    user_2 = User.objects.create(
        username="AirWow",
        password="azerty",
        first_name="Ada",
        last_name="Paul",
        email="flocation.vam4@glendenningflowerdesign.com",
        is_active=True,
    )

    Profile.objects.create(user=user_1, favorite_city="Berlin")
    Profile.objects.create(user=user_2, favorite_city="Budapest")
