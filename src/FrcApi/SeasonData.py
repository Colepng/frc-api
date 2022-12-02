import requests
import sys
sys.path.append(r"C:\Users\gamin\OneDrive\Documents\GitHub\frc-api\src\FrcApi")
import src.FrcApi as FrcApi
import json

class SeasonData:
    def __init__(self, season: int = 2022, team_number: int = None,
                 District: str = None):
        self.team_number = team_number
        self.season = season
        self.District = District
        self.headers = {'Authorization': f'Basic {FrcApi.config.key}'}
        self.payload = {}   
    
    def SeasonSummary(self, season: int):
        """
        The season summary API returns a high level glance of a particular FRC season.

        """
        url = f"{FrcApi.BASEURL}{season}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        return response.text