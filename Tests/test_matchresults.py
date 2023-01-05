import FrcApi
import json

from os import getenv
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()
TOKEN = getenv("Frc-api-token")
PROPEROUTPUT = Path("Tests/ProperOutput")

# Set up the api
FrcApi.Config.encode_key(FrcApi.Config, api_key=TOKEN, username="colepng")
match_results = FrcApi.MatchResults()


class TestMatchResults:
    """Class to contain the tests for the MatchResults class."""

    def test_score_details_1(self):
        """Test the score_details function."""
        with open(PROPEROUTPUT / "score_details_test_1.json", "r") as f:
            assert match_results.score_details(event_code="on305", match_level="playoff", season=2022) == json.load(f)  # noqa: E501

    def test_score_details_2(self):
        """Test the score_details function."""
        with open(PROPEROUTPUT / "score_details_test_2.json", "r") as f:
            assert match_results.score_details(event_code="on305", match_level="qual", team_number=865, season=2022) == json.load(f)  # noqa: E501

    def test_score_details_3(self):
        """Test the score_details function."""
        with open(PROPEROUTPUT / "score_details_test_3.json", "r") as f:
            assert match_results.score_details(event_code="on305", match_level="qual", match_number=1, season=2022) == json.load(f)  # noqa: E501

    def test_score_details_4(self):
        """Test the score_details function."""
        with open(PROPEROUTPUT / "score_details_test_4.json", "r") as f:
            assert match_results.score_details(event_code="on305", start=5, end=10, match_level="playoff", season=2022) == json.load(f)  # noqa: E501

    def test_event_match_results_1(self):
        """Test the event_match_results function."""
        with open(PROPEROUTPUT / "event_match_results_test_1.json", "r") as f:
            assert match_results.event_match_results(event_code="on305", season=2022) == json.load(f)  # noqa: E501

    def test_event_match_results_2(self):
        """Test the event_match_results function."""
        with open(PROPEROUTPUT / "event_match_results_test_2.json", "r") as f:
            assert match_results.event_match_results(event_code="on305", match_level="qual", match_number=1, season=2022) == json.load(f)  # noqa: E501

    def test_event_match_results_3(self):
        """Test the event_match_results function."""
        with open(PROPEROUTPUT / "event_match_results_test_3.json", "r") as f:  # noqa: E501
            assert match_results.event_match_results(event_code="on305", team_number=865, season=2022) == json.load(f)  # noqa: E501

    def test_event_match_results_4(self):
        """Test the event_match_results function."""
        with open(PROPEROUTPUT / "event_match_results_test_4.json", "r") as f:
            assert match_results.event_match_results(event_code="on305", start=5, end=10, match_level="qual", season=2022) == json.load(f)  # noqa: E501
