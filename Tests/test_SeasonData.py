import FrcApi
import os
import json

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.config.key(FrcApi.config, api_key=TOKEN)
SeasonData = FrcApi.SeasonData(season=2022, team_number=865, District="ONT")


# Faling test, need to investigate to figure out if
# It an issue the the weird cachters in the names or if it an code issue
class TestSeasonData:
    def test_one_SeasonSummary(self):
        """Test the Season Summary function"""
        with open(r"Tests\ProperOutput\SeasonSummary_test_1.json", "r") as f:
            assert SeasonData.SeasonSummary(season=2022) == json.load(f)

