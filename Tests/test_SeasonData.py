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
seasondata = FrcApi.SeasonData(season=2022, team_number=865, district="ONT")


# Faling test, need to investigate to figure out if
# It an issue the the weird cachters in the names or if it an code issue
class TestSeasonData:
    """Test Season Data."""

    # def test_1_season_summary(self):
    #     """Test Season Summary."""
    #     with open(r"Tests\ProperOutput\SeasonSummary_test_1.json", "r") as f:
    #         assert seasondata.season_summary(season=2022) == json.load(f)

    def event_listing_error_test_1(self):
        """Test Event Listing."""
        # with open(r"Tests\ProperOutput\EventListing_test_1.json", "r") as f:
        #     assert seasondata.EventListing(season=2022) == json.load(f)
        try:
            print(seasondata.event_listing(season=2023, event_code="onnob"))
        except ValueError:
            assert "passed" == "passed"
        else:
            assert "passed" == "failed"


# print(seasondata.event_listing(season=2022))
# print(seasondata.event_listing(team_number=2056, season=2023)["Events"][0]["address"])
print(seasondata.event_listing(season=2023, tournamentype="regional"))
