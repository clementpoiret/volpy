from bs4 import BeautifulSoup
from bs4.element import Tag


def get_upload_form(soup: BeautifulSoup) -> Tag:
    """
    Get the upload form from the soup.

    Args:
        soup (BeautifulSoup): The soup to search in.

    Returns:
        form (Tag): The upload form.
    """
    form = soup.find(id="upload_form")

    if form is None:
        raise Exception("No upload form found, login probably failed.")

    return form
