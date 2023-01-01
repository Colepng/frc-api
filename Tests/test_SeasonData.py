"""
place holder.

place holder.
place holder.
"""
import os
import FrcApi
from dotenv import load_dotenv
import json

load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.Config.encode_key(FrcApi.Config, api_key=TOKEN, username="colepng")
season_data = FrcApi.SeasonData(team_number=865, district="ONT")


class TestSeasonData:
    """Test Season Data."""

    # The api changed the number of teams from 3213 to 4577 so the file was swapped with one uptodate # noqa: E501
    def test_1_season_summary(self):
        """Test Season Summary."""
        with open(r"Tests\ProperOutput\SeasonSummary_test_1.json", "r",
                  encoding="utf-8") as f:
            assert season_data.season_summary(season=2022) == json.load(f)

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

    def test_event_listing_1(self):
        """Test Event Listing."""
        with open(r"Tests\ProperOutput\event_listings_test_1.json", "r") as f:
            assert season_data.event_listing(event_code="onwat") == json.load(f)  # noqa: E501

    def test_event_listing_2(self):
        """Test Event Listing."""
        with open(r"Tests\ProperOutput\event_listings_test_2.json", "r") as f:
            assert season_data.event_listing(team_number=2022) == json.load(f)

    def test_event_listing_3(self):
        """Test Event Listing."""
        with open(r"Tests\ProperOutput\event_listings_test_3.json", "r") as f:
            assert season_data.event_listing(district_code="ONT") == json.load(f)  # noqa: E501

    # Test is properly setup but the api changed the number of event in the 2022 season so the file was swapped with one more uptodate # noqa: E501
    def test_event_listing_4(self):
        """Test Event Listing."""
        with open(r"Tests\ProperOutput\event_listings_test_4.json", "r",
                  encoding="utf-8") as f:
            assert season_data.event_listing(season=2022) == json.load(f)  # noqa: E501

    def test_event_listing_5(self):
        """Test Event Listing."""
        with open(r"Tests\ProperOutput\event_listings_test_5.json", "r") as f:
            assert season_data.event_listing(week_number="4", exclude_district=True, season=2018) == json.load(f)  # noqa: E501

    # Test is propeoly setup but the api is not filtering tournament type and removed some events from the list  # noqa: E501
    # def test_event_listing_6(self):
    #     """Test Event Listing."""
    #     with open(r"Tests\ProperOutput\event_listings_test_6.json", "r",
    #               encoding="utf-8") as f:
    #         assert season_data.event_listing(season=2022, tournamentype="OffSeason") == json.load(f)  # noqa: E501
