import base64
global key
key = "test"
def token(token : str, username : str = "", encoded : bool = False):
    """ This function takes your token and saves it for the moudle to use.
        token: Your token.

        username: Your username.

        encoded: If you have already encoded the token or not, if so set to True and the username is not needed.
        """
    if not encoded:
        token_base64 = base64.standard_b64encode(f"{username}:{token}".encode()).decode()
        token = token_base64
    global key
    key = token
