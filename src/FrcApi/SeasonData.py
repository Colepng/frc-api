"""
place holder.

place holder.
place holder.
"""
import requests

from .config import BASEURL, Config
from .fun import season_check


class SeasonData:
    """place holder."""

    def __init__(self, season: int = 2023, team_number: int = None,
                 district: str = None):
        """Place holder."""
        self.team_number = team_number
        self.season = season
        self.district = district
        self.headers = {'Authorization': f'Basic {Config.api_key}'}
        self.payload = {}

    def season_summary(self, season: int) -> dict:
        """
        Return info about a season.

        Examples: The number of events or the number of teams that season.
        """
        url = f"{BASEURL}{season}"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)

        return response.json()

    def event_listing(self, event_code: str = None, team_number: int = None,
                      district_code: str = "", exclude_district: bool = False,
                      week_number: int = None, tournamentype: str = "",
                      season: int = None) -> dict:
        """
        Place holder.

        place holder.
        """
        url_args = ""

        if event_code:
            url_args += f"&eventCode={event_code}"
            if any([team_number, district_code, exclude_district, week_number, tournamentype]):  # noqa: E501
                raise ValueError("cannot specify any optional args with event_code")  # noqa: E501

        elif district_code and exclude_district:
            raise ValueError("If you specify a district code you cannot specify an event code or exclude district")  # noqa: E501

        url_args += f"&teamNumber={team_number}&excludeDistrict={str(exclude_district).lower()}&weekNumber={week_number}&tounamentType={tournamentype}"  # noqa: E501
        url = f"{BASEURL}{season_check(season, self.season)}/events?{url_args}"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)
        return response.json()
