import pytest

from utils.common import is_valid_address, parse_address


def test_is_valid_address():
    addresses = [
        ("Street 10, 75001 Paris, France", True),
        ("Street 20, 1000 Brussels, Belgium", True),
        ("Street 5, 28013 Madrid, Spain", True),
        ("Street 9, 1016 Amsterdam, Netherlands", True),
        ("Street 15, 1050 Copenhagen, Denmark", True),
        ("Street 1, Copenhagen, Denmark", False),
        ("Street 15, 1050 Copenhagen", False),
        ("28013 Copenhagen, Denmark", False),
        ("Street 9 1016 Amsterdam Netherlands", False),
    ]

    for address, is_valid in addresses:
        assert is_valid_address(address) == is_valid


def test_parse_address():
    addresses = [
        # (address, zipcode, countrycode)
        ("Street 10, 75001 Paris, France", '75001', 'FR'),
        ("Street 20, 1000 Brussels, Belgium", '1000', 'BE'),
        ("Street 5, 28013 Madrid, Spain", '28013', 'ES'),
        ("Street 9, 1016 Amsterdam, Netherlands", '1016', 'NL'),
        # test country name capitalization
        ("Street 15, 1050 Copenhagen, denMarK", '1050', 'DK'),
    ]

    for address, zipcode, country_code in addresses:
        assert parse_address(address) == (zipcode, country_code)


def test_parse_address_exception():
    address = "Street 10, 75001 Paris, XYZ"

    # When country name is incorrect raise an Exception
    with pytest.raises(KeyError):
        parse_address(address)
