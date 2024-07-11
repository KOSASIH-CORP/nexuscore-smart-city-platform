import re
from typing import List

def normalize_string(s: str) -> str:
    """
    Normalize a string by removing special characters and converting to lowercase.

    Args:
        s (str): Input string

    Returns:
        str: Normalized string
    """
    s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
    s = s.lower()
    return s

def tokenize_string(s: str) -> List[str]:
    """
    Tokenize a string into individual words.

    Args:
        s (str): Input string

    Returns:
        List[str]: List of tokens
    """
    tokens = s.split()
    return tokens
