"""
place holder.

place holder.
place holder.
"""
import os
import json
import FrcApi

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.config.key(FrcApi.config, api_key=TOKEN)
seasondata = FrcApi.seasondata(season=2022, team_number=865, District="ONT")


# Faling test, need to investigate to figure out if
# It an issue the the weird cachters in the names or if it an code issue
class TestSeasonData:
    """Test Season Data."""

    def test_1_season_summary(self):
        """Test Season Summary."""
        with open(r"Tests\ProperOutput\SeasonSummary_test_1.json", "r") as f:
            assert seasondata.SeasonSummary(season=2022) == json.load(f)
