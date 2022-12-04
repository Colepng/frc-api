"""
place holder.

place holder.
place holder.
"""
import requests

from .config import BASEURL, Config


class SeasonData:
    """place holder."""

    def __init__(self, season: int = 2022, team_number: int = None,
                 district: str = None):
        """Place holder."""
        self.team_number = team_number
        self.season = season
        self.district = district
        self.headers = {'Authorization': f'Basic {Config.api_key}'}
        self.payload = {}

    def season_summary(self, season: int):
        """
        Return info about a season.

        Examples: The number of events or the number of teams that season.
        """
        url = f"{BASEURL}{season}"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)

        return response.json()

    def event_listing(self, season: int):
        """
        Place holder.

        place holder.
        """
        url = f"{BASEURL}events"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)

        return response.json()
