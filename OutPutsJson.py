"""This file is used to save the output of the FrcApi as a json file. THIS FILE IS TO BE REMOVED AFTER DEVELOPMENT IS COMPLETE."""  # noqa: E501
import json
# import src.FrcApi as FrcApi
from src import FrcApi
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("Frc-api-token")
FrcApi.Config.encode_key(FrcApi.Config, api_key=TOKEN, username="colepng")

season_data = FrcApi.SeasonData()
rankings = FrcApi.Rankings()


def save_as_json(data, filename):
    with open(f"Tests/ProperOutput/{filename}.json", 'w', encoding='utf-8') as f:  # noqa: E501
        json.dump(data, f, ensure_ascii=False, indent=4)


save_as_json(rankings.district_rankings(team_number=865, season=2022), filename="district_rankings_test_3")  # noqa: E501


# with open("Tests/ProperOutput/team_avatar_listings_test_2.png", "wb") as f:  # noqa: E501
#     f.write(season_data.team_avatar_listings(season=2022, event_code="on305"))  # noqa: E501
