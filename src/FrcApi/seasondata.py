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

        elif district_code:
            url_args += f"&districtCode={district_code}"
            if exclude_district:
                raise ValueError("If you specify a district code you cannot specify an event code or exclude district")  # noqa: E501

        url_args += f"&teamNumber={team_number}&excludeDistrict={str(exclude_district).lower()}&weekNumber={week_number}&tounamentType={tournamentype}"  # noqa: E501
        url = f"{BASEURL}{season_check(season, self.season)}/events?{url_args}"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)
        print(url)
        return response.json()

    def district_listings(self, season: int = None) -> dict:
        """Place holder."""
        url = f"{BASEURL}{season_check(season, self.season)}/districts"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)
        return response.json()

    def team_listings(self, team_number: int = None, event_code: str = None,
                      district_code: str = "", season: int = None,
                      state: str = "", page: int | list = "all",
                      page_min: int = 1, page_max: int = None) -> dict | list:  # noqa: E501
        """Place holder."""
        season = season_check(season, self.season)
        url_args = ""
        if event_code:
            url_args += f"&eventCode={event_code}"
            if team_number:
                raise ValueError("cannot specify team number and event code")
        if district_code:
            url_args += f"&districtCode={district_code}"
            if team_number:
                raise ValueError("cannot specify team number and district code")  # noqa: E501

        url_args += f"&teamNumber={team_number}&state={state}"

        if type(page) == int:
            url_args += f"&page={page}"

        elif type(page) == str:
            data = []
            if page_max is None:
                url = f"{BASEURL}{season}/teams?{url_args}&page=1"
                response = requests.request("GET", url, headers=self.headers,
                                            data=self.payload)
                page_max = response.json()["pageTotal"]
                if page_max == 1:
                    return response.json()

            for page in range(page_min, page_max + 1):
                url = f"{BASEURL}{season}/teams?{url_args}&page={page}"
                response = requests.request("GET", url, headers=self.headers,
                                            data=self.payload)
                data.append(response.json())
            return data

        elif type(page) == list:
            data = []
            for i in page:
                url = f"{BASEURL}{season}/teams?{url_args}&page={i}"
                response = requests.request("GET", url, headers=self.headers,
                                            data=self.payload)
                data.append(response.json())
            return data

        else:
            raise TypeError("page must be an int, str, or list")

        url = f"{BASEURL}{season}/teams?{url_args}"
        response = requests.request("GET", url, headers=self.headers,
                                    data=self.payload)
        return response.json()
