"""
Test the Rankings class of the FrcApi warpper.

Covers the following functions:

    - qual_preformance_points
    - alliance_selection_points
    - playoff_advancement_points
    - event_rankings
    - district_rankings
"""
import os
import FrcApi
import json

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Load environment variables
TOKEN = os.getenv("Frc-api-token")
PROPEROUTPUT = Path("Tests/ProperOutput")

# Set up the api
FrcApi.Config.encode_key(FrcApi.Config, TOKEN, "colepng")
rankings = FrcApi.Rankings()


class TestRankings():
    """Class to contain the tests for the Rankings class."""
    def test_event_rankings_1(self):
        """Test the event_rankings function."""
        with open(PROPEROUTPUT / "event_rankings_test_1.json", "r") as f:
            assert rankings.event_rankings(event_code="on305", season=2022) == json.load(f)  # noqa: E501

    def test_event_rankings_2(self):
        """Test the event_rankings function."""
        with open(PROPEROUTPUT / "event_rankings_test_2.json", "r") as f:
            assert rankings.event_rankings(event_code="on305", top=5, season=2022) == json.load(f)  # noqa: E501

    def test_event_rankings_3(self):
        """Test the event_rankings function."""
        with open(PROPEROUTPUT / "event_rankings_test_3.json", "r") as f:
            assert rankings.event_rankings(event_code="on305", team_number=865, season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_1(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_1.json", "r") as f:
            assert rankings.district_rankings(district_code="ONT", season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_2(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_2.json", "r") as f:
            assert rankings.district_rankings(district_code="ONT", top=10, season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_3(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_3.json", "r") as f:
            assert rankings.district_rankings(team_number=865, season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_4(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_4.json", "r") as f:
            assert rankings.district_rankings(district_code="ONT", page=[2], season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_5(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_5.json", "r") as f:
            assert rankings.district_rankings(district_code="ONT", page=1, season=2022) == json.load(f)  # noqa: E501

    def test_district_rankings_6(self):
        """Test the district_rankings function."""
        with open(PROPEROUTPUT / "district_rankings_test_6.json", "r") as f:
            assert rankings.district_rankings(district_code="ONT", page_min=1, page_max=2, season=2022) == json.load(f)  # noqa: E501
