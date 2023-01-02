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


SaveAsJson(season_data.team_listings(page=[1, 5, 10, 20]), "team_listings_test_6")  # noqa: E501
