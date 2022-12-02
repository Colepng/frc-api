import src.FrcApi as FrcApi
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("Frc-api-token")

FrcApi.token(username="colepng", token=TOKEN, encoded = False)

SeasonData = FrcApi.SeasonData(season = 2022, team_number = 865, District = "ONT")

class TestSeasonData:
    def test_one_SeasonSummary(self):
        """Test the Season Summary function"""
        assert SeasonData.SeasonSummary(season = 2022) == open(r"Tests\Test returns\SeasonSummery_test.txt", "r").read()
        #Test is failing because of the way the ℠ is store in the file but otherwise there the same