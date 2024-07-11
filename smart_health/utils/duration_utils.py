import datetime
from typing import Tuple

def get_duration(start_time: datetime.datetime, end_time: datetime.datetime) -> int:
    """
    Calculate the duration between two timestamps.

    Args:
        start_time (datetime.datetime): Start timestamp
        end_time (datetime.datetime): End timestamp

    Returns:
        int: Duration in seconds
    """
    duration = (end_time - start_time).total_seconds()
    return int(duration)

def get_duration_matrix(points: list[Tuple[datetime.datetime, datetime.datetime]]) -> list[list[int]]:
    """
    Calculate the duration matrix for a list of points with start and end timestamps.

    Args:
        points (list[Tuple[datetime.datetime, datetime.datetime]]): List of points with start and end timestamps

    Returns:
        list[list[int]]: Duration matrix where each element [i][j] represents the duration between points i and j
    """
    duration_matrix = [[0 for _ in range(len(points))] for _ in range(len(points))]
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            duration_matrix[i][j] = get_duration(points[i][0], points[j][1])
            duration_matrix[j][i] = duration_matrix[i][j]
    return duration_matrix
