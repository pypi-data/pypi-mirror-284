"""
Utils
"""

from __future__ import annotations

from urllib.parse import urlparse

from restfly.errors import RestflyException


def url_validator(url: str, validate: list[str] | None = None) -> bool:
    """
    Validates that the required URL Parts exist within the URL string.

    Args:
        url (string):
            The URL to process.
        validate (list[str], optional):
            The URL parts to validate are non-empty.

    Examples:
        >>> url_validator('https://google.com') # Returns True
        >>> url_validator('google.com') #Returns False
        >>> url_validator(
        ...     'https://httpbin.com/404',
        ...     validate=['scheme', 'netloc', 'path'])
            # Returns True
    """
    if not validate:
        validate = ["scheme", "netloc"]
    resp = urlparse(url)._asdict()
    for val in validate:
        if val not in resp or resp[val] == "":
            return False
    return True


class FileDownloadError(RestflyException):
    """
    FileDownloadError is thrown when a file fails to download.

    Attributes:
        msg (str):
            The error message
        filename (str):
            The Filename or file id that was requested.
        resource (str):
            The resource that the file was requested from (e.g. "scans")
        resource_id (str):
            The identifier for the resource that was requested.
    """

    def __init__(self, resource: str, resource_id: str, filename: str):
        self.resource = str(resource)
        self.resource_id = str(resource_id)
        self.filename = str(filename)
        self.msg = f"resource {resource}:{resource_id} " f"requested file {filename} and has failed."
