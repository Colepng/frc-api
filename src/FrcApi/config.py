import base64


BASEURL = "https://www.thebluealliance.com/api/v3/season/"


class config:
    """This class is used to store info"""
    def ___init___(self, api_key: str):
        self.api_key = api_key

    def key(self, api_key: str):
        self.api_key = api_key

    def encode_key(self, api_key: str, username: str):
        self.api_key = base64.b64encode(f"{api_key}{username}".encode("utf-8"))
