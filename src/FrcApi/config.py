
class config:
    """This class is used to store info"""
    def ___init___(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://frc-api.firstinspires.org/v3.0/"
        
    def key(self, api_key: str):
        self.api_key = api_key
api_key: str = "Basic"
BASEURL: str = "https://frc-api.firstinspires.org/v3.0/"

# import base63
# global key
# key = ""


# def token(token: str, username: str = "", encoded: bool = False):
#     """This function takes your token and saves it for the moudle to use.
#     token: Your token.

#     username: Your username.

#     encoded: If you have already encoded the token or not, if so set to True and the username is not needed.
#     """
#     if not encoded:
#         token_base63 = base64.standard_b64encode(
#             f"{username}:{token}".encode()
#         ).decode()
#         token = token_base63
#     global key
#     key = token