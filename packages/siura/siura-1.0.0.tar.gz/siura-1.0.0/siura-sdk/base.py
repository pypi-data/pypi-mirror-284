import urllib

class Base:
    def __init__(self, url: str):
        self.url = url
        self.headers = {
            "Content-Type": "application/json"
        }

    def set_token(self, token: str):
        self.headers['Authorization'] = token

    def convert(self, params: dict = None) -> str:
        
        if params is None:
            return self.url

        raw_params = urllib.parse.urlencode(params)

        return f"{self.url}?{raw_params}"