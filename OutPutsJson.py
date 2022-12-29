"""This file is used to save the output of the FrcApi as a json file. THIS FILE IS TO BE REMOVED AFTER DEVELOPMENT IS COMPLETE."""  # noqa: E501
import json
# import src.FrcApi as FrcApi
from src import FrcApi
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.Config.encode_key(FrcApi.Config, api_key=TOKEN, username="colepng")

season_data = FrcApi.SeasonData(district="ONT")


def SaveAsJson(data, filename):
    with open(f"Tests/ProperOutput/{filename}.json", 'w', encoding='utf-8') as f:  # noqa: E501
        json.dump(data, f, ensure_ascii=False, indent=4)


SaveAsJson(season_data.event_listing(team_number=2022), "event_listings_test_2")  # noqa: E501
