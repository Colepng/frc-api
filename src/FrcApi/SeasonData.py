import requests
import sys
# from . import BASEURL, KEY
from .config import BASEURL, config

class SeasonData:
    def __init__(self, season: int = 2022, team_number: int = None,
                 District: str = None):
        self.team_number = team_number
        self.season = season
        self.District = District
        self.headers = {'Authorization': f'Basic {config.api_key}'}
        self.payload = {}   
    
    def SeasonSummary(self, season: int):
        """
        The season summary API returns a high level glance of a particular FRC season.

        """
        url = f"{BASEURL}{season}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)

        return response.json()

    def test(self):
        print(config.api_key)
