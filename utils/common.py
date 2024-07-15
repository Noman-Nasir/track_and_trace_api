"""
Common api utilities
"""
import re

from constants import COUNTRY_NAME_TO_CODE


def is_valid_address(address: str) -> bool:
    """
    Check whether the given address is in valid format like
    `Street 10, 75001 Paris, France`

    Args:
        address
    Returns:
        True if address is valid else False
    """
    # Regular expression pattern to match the specified address format
    # ^[A-Za-z\s\d]+: Matches the street name or number (one or more letters, digits, and spaces).
    # , \d+: Matches a comma followed by a space and more than one digit (the zip code).
    # [A-Za-z\s]+: Matches the city name (one or more letters and spaces).
    # , [A-Za-z\s]+$: Matches a comma followed by the country name (one or more letters and spaces) at the end
    pattern = r'^[A-Za-z\s\d]+, \d+ [A-Za-z\s]+, [A-Za-z\s]+$'

    # Use the full match method to check if the entire string matches the pattern
    match = re.fullmatch(pattern, address)

    return match is not None


def parse_address(address: str) -> (str, str):
    """
    A utility to parse an address and return zipcode and country code.
    Country code will be ISO 3166-1 alpha-2 format.

    Args:
        address: Address in format like `Street 10, 75001 Paris, France`
    Return:
        zipcode, country_code
    """
    _, zip_city, country = address.split(',')
    # Remove unnecessary spaces and extract zipcode
    zipcode = str(zip_city).strip().split(' ')[0]
    # Remove unnecessary spaces and map country name to country code
    country_code = COUNTRY_NAME_TO_CODE[country.strip().capitalize()]

    return zipcode, country_code
