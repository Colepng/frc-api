"""
place holder.

place holder.
place holder.
"""
import base64


BASEURL = "https://www.thebluealliance.com/api/v3/season/"


class Config:
    """This class is used to store info."""

    def key(self, api_key: str):
        """Set the api key."""
        self.api_key = api_key

    def encode_key(self, api_key: str, username: str):
        """Encode the api key."""
        self.api_key = base64.b64encode(f"{api_key}{username}".encode("utf-8"))
