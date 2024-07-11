import math
from typing import Tuple

def get_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the distance between two points on the Earth's surface using the Haversine formula.

    Args:
        lat1 (float): Latitude of the first point
        lon1 (float): Longitude of the first point
        lat2 (float): Latitude of the second point
        lon2 (float): Longitude of the second point

    Returns:
        float: Distance between the two points in kilometers
    """
    radius = 6371  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c
    return distance

def get_distance_matrix(points: list[Tuple[float, float]]) -> list[list[float]]:
    """
    Calculate the distance matrix for a list of points.

    Args:
        points (list[Tuple[float, float]]): List of points with latitude and longitude coordinates

    Returns:
        list[list[float]]: Distance matrix where each element [i][j] represents the distance between points i and j
    """
    distance_matrix = [[0.0 for _ in range(len(points))] for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance_matrix[i][j] = get_distance(points[i][0], points[i][1], points[j][0], points[j][1])
            distance_matrix[j][i] = distance_matrix[i][j]
    return distance_matrix
