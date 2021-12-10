import pytest
from ..models import Address, Letting


@pytest.fixture
def add_data():
    address_1 = Address.objects.create(
        number=7217,
        street="Bedford Street",
        city="Brunswick",
        state="GA",
        zip_code=31525,
        country_iso_code="USA",
    )
    address_2 = Address.objects.create(
        number=4,
        street="Military Street",
        city="Willoughby",
        state="OH",
        zip_code=44094,
        country_iso_code="USA",
    )
    Letting.objects.create(
        title="Joshua Tree Green Haus /w Hot Tub",
        address=address_1,
    )
    Letting.objects.create(
        title="Oceanview Retreat",
        address=address_2,
    )
