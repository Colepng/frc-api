import json
import src.FrcApi as FrcApi
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("Frc-api-token")

FrcApi.token(username="colepng", token=TOKEN, encoded = False)
rank = FrcApi.Rankings(season = 2022, team_number = 865, District = "ONT")
MatchResults = FrcApi.MatchResults(season = 2022, team_number = 865, District = "ONT") 
SeasonData = FrcApi.SeasonData(season = 2022, team_number = 865, District = "ONT")

def SaveAsJson(data, filename):
    with open(f"Tests/Test returns/{filename}.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# SaveAsJson(rank.Event_Rankings(event_code = "on305"), "Event_Rankings_test_1")(Eve
# SaveAsJson(rank.Event_Rankings(event_code = "onbar", season=2020, use_predifend_infomation = True), "Event_Rankings_test_2")
# SaveAsJson(rank.Event_Rankings(event_code = "ONCMP", season=2022, top=10), "Event_Rankings_test_3")
# SaveAsJson(MatchResults.ScoreDetailsnt="on305", MatchLevel="playoff"), "ScoreDetails_test_1")
# SaveAsJson(SeasonData.SeasonSummary(season=2022), "SeasonSummary_test_1")