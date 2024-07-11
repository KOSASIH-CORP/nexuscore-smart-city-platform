import requests
from typing import Tuple

def geocode(address: str) -> Tuple[float, float]:
    """
    Geocode an address using the geocoding API.

    Args:
        address (str): Address to geocode

    Returns:
        Tuple[float, float]: Latitude and longitude coordinates
    """
    response = requests.get(GEOCODING_API, params={"address": address, "api_key": GEOCODING_API_KEY})
    data = response.json()
    lat = data["results"][0]["geometry"]["location"]["lat"]
    lon = data["results"][0]["geometry"]["location"]["lng"]
    return lat, lon

def reverse_geocode(lat: float, lon: float) -> str:
    """
    Reverse geocode a latitude and longitude coordinate using the geocoding API.

    Args:
        lat (float): Latitude coordinate
        lon (float): Longitude coordinate

    Returns:
        str: Address corresponding to the latitude and longitude coordinates
    """
    response = requests.get(GEOCODING_API, params={"latlng": f"{lat},{lon}", "api_key": GEOCODING_API_KEY})
    data = response.json()
    address = data["results"][0]["formatted_address"]
    return address
