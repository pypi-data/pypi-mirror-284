import requests

class XBRLAPIClient:
    def __init__(self, api_key: str, base_url: str = "https://xbrlapi.vercel.app"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_data(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}, {response.text}")
        return response.json()
