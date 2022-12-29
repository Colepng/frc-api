"""
place holder.

place holder.
place holder.
"""
import os
import FrcApi
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.Config.encode_key(FrcApi.Config, api_key=TOKEN, username="colepng")
season_data = FrcApi.SeasonData(team_number=865, district="ONT")


# Faling test, need to investigate to figure out if
# It an issue the the weird cachters in the names or if it an code issue
class TestSeasonData:
    """Test Season Data."""

    # def test_1_season_summary(self):
    #     """Test Season Summary."""
    #     with open(r"Tests\ProperOutput\SeasonSummary_test_1.json", "r") as f:
    #         assert seasondata.season_summary(season=2022) == json.load(f)

    def test_event_listing_error_1(self):
        """Test Event Listing event_code and any thing else error."""
        try:
            season_data.event_listing(event_code="onnob", team_number=865)
        except ValueError:
            assert "passed" == "passed"
        else:
            assert "passed" == "failed"

    def test_event_listing_error_2(self):
        """Test Event Listing error district_code and exclude_district."""
        try:
            season_data.event_listing(district_code="ONT", exclude_district=True)  # noqa: E501
        except ValueError:
            assert "passed" == "passed"
        else:
            assert "passed" == "failed"
