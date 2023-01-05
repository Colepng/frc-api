import requests

from .config import BASEURL, Config
from .fun import season_check


class MatchResults:
    def __init__(self, season: int = 2023) -> None:
        self.SEASON = season
        self.headers = {'Authorization': f'Basic {Config.api_key}'}
        self.payload = {}

    def score_details(self, event: str, match_level: str,
                      match_number: int = None, team_number: int = None,
                      start: int = None, end: int = None,
                      season: int = None) -> dict:
        """
        This function returns the score details for a given match.

        MatchLevel: If u want either a qual match or playoff.

        match_number: If u want the results for a specific match.

        TeamNumber: If u want the results for a specific team.

        Start: The start of the matches u want.

        End: The end of the matches u want.
        """
        season = season_check(season, self.SEASON)

        url_args = f"&match_number={match_number}&teamNumber={team_number}&start={start}&end={end}"  # noqa: E501
        url = f"{BASEURL}{season}/scores/{event}/{match_level}?{url_args}"
        if match_number and team_number:
            raise ValueError("You can't specify both match_number and team_number")  # noqa: E501

        if match_number and any([start, end]):
            raise ValueError("You can't specify both match_number and start or end")  # noqa: E501

        response = requests.request(
            "GET", url, headers=self.headers, data=self.payload)
        print(url)
        return response.json()

    def EventMatchResults(self, Event: str, MatchLevel: str = None, TeamNumber: int = None, match_number: int = None, Start: int = None, End: int = None, season: int = None):
        """
        This fucntion returns the general details about a single or multiple matches.
        MatchLevel: If u want either qual, playoff, or leave blank for all.
        TeamNumber: If u want the results for a specific team.
        match_number: If u want the results for a specific match.
        Start: The start of the matches u want.
        End: The end of the matches u want.
        """
        if match_number or Start or End:
            if MatchLevel:
                if match_number and Start or match_number and End:
                    raise ValueError("You can't specify both match_number and Start or End")
            else:
                raise ValueError("MatchLevel is required if match_number, Start, or End is specified")
        elif match_number and TeamNumber:
            raise ValueError("You can't specify both match_number and TeamNumber")

        url = f"https://frc-api.firstinspires.org/v3.0/{self.SEASON if not season else season}/matches/{Event}?tournamentLevel={MatchLevel}&match_number={match_number}&teamNumber={TeamNumber}&start={Start}&end={End}"
      
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        if match_number:
            MatchNumPos = response.text.find(f'"match_number":{match_number},')
            MatchStart = response.text[0:MatchNumPos].rindex('{"isReplay"')
            MatchEnd = response.text.find("}]},", MatchNumPos,)
            return response.text[MatchStart:MatchEnd + 4]
        else:
           return response.json()