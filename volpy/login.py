import requests
from omegaconf import DictConfig


def login(url: str, payload: DictConfig) -> bytes:
    """
    Login to the website.

    Args:
        url (str): The url to login to.
        payload (DictConfig): The payload to send.

    Returns:
        content (bytes): The content of the response.
    """
    session = requests.Session()
    response = session.post(url, payload)

    return response.content
