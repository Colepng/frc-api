import requests

from .config import BASEURL, Config
from .fun import season_check

class MatchResults:
    def __init__(self, season: int = 2022, team_number: int = None,
                 District: str = None):
        self.team_number = team_number
        self.season = season
        self.District = District
        self.headers = {'Authorization': f'Basic {FrcApi.config.key}'}
        self.payload = {}

    def ScoreDetails(self, Event: str, MatchLevel: str, MatchNumber: int = None,
                     TeamNumber: int = None, start: int = None,
                     end: int = None, season: int = None):
        """
        This function returns the score details for a given match.
        MatchLevel: If u want either a qual match or playoff.
        MatchNumber: If u want the results for a specific match.
        TeamNumber: If u want the results for a specific team.
        Start: The start of the matches u want.
        End: The end of the matches u want.
        """
        url = f"""https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/scores/{Event}/{MatchLevel}?MatchNumber={MatchNumber}&TeamNumber={TeamNumber}&start={start}&end={end}"""
        if MatchNumber and TeamNumber:
            raise ValueError("You can't specify both MatchNumber and TeamNumber")

        if MatchNumber and start or MatchNumber and end:
            raise ValueError("You can't specify both MatchNumber and Start or End")

        response = requests.request(
            "GET", url, headers=self.headers, data=self.payload)
        print(url)
        return response.text

    def EventMatchResults(self, Event: str, MatchLevel: str = None, TeamNumber: int = None, MatchNumber: int = None, Start: int = None, End: int = None, season: int = None):
        """
        This fucntion returns the general details about a single or multiple matches.
        MatchLevel: If u want either qual, playoff, or leave blank for all.
        TeamNumber: If u want the results for a specific team.
        MatchNumber: If u want the results for a specific match.
        Start: The start of the matches u want.
        End: The end of the matches u want.
        """
        if MatchNumber or Start or End:
            if MatchLevel:
                if MatchNumber and Start or MatchNumber and End:
                    raise ValueError("You can't specify both MatchNumber and Start or End")
            else:
                raise ValueError("MatchLevel is required if MatchNumber, Start, or End is specified")
        elif MatchNumber and TeamNumber:
            raise ValueError("You can't specify both MatchNumber and TeamNumber")

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/matches/{Event}?tournamentLevel={MatchLevel}&matchNumber={MatchNumber}&teamNumber={TeamNumber}&start={Start}&end={End}"
      
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        if MatchNumber:
            MatchNumPos = response.text.find(f'"matchNumber":{MatchNumber},')
            MatchStart = response.text[0:MatchNumPos].rindex('{"isReplay"')
            MatchEnd = response.text.find("}]},", MatchNumPos,)
            return response.text[MatchStart:MatchEnd + 4]
        else:
           return response.text