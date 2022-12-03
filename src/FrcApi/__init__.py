from .config import token

from .MatchResults import MatchResults
from .rankings import Rankings
from .SeasonData import SeasonData

BASEURL = "https://frc-api.firstinspires.org/v3.0/"

# Code to formamt the output as a json for it to be more human readable
# with open('', 'w', encoding='utf-8') as f:
    # json.dump(response.json(), f, ensure_ascii=False, indent=3)