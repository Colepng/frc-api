import requests
import sys
sys.path.append(r"C:\Users\gamin\OneDrive\Documents\GitHub\frc-api\src\FrcApi")
import src.FrcApi as FrcApi

class Rankings:
    def __init__(self, season : int = 2022, team_number : int = None, District : str = None):
        self.team_number = team_number
        self.season = season
        self.District = District
        self.headers = {'Authorization': f'Basic {FrcApi.config.key}'}
        self.payload = {}

    def Qual_Performance_Points(self, tournamentType : str, qualificationRank : int, teamsAtEvent : int):
        """
        This function returns the qual performance points for a given team.
        
        TournamentType: The type of tournament the team is in.
        Ex: "DistrictEvent" or "Championship" check docs for all of the types.

        qualificationRank: The rank of the team in the qual.

        teamsAtEvent: The number of teams at the event.
        """

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season}/rankings/district/qualPerformanceCalculation?tournamentType={tournamentType}&qualificationRank={qualificationRank}&teamsAtEvent={teamsAtEvent}"

        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        return int(response.text)

    def Alliance_Selection_Points(self, tournamentType : str, NumberOfAlliances : int or str, allianceNumber : int, allianceRole : str, season : int = None):

        """
        This function returns the alliance selection points for a given team.

        TournamentType: The type of tournament the team is in. 
        Ex: "DistrictEvent" or "Championship" check docs for all of the types.

        NumberOfAlliances: The number of alliances. 
        Ex: "Two", "Four",  "Six", "eight", "Sixteen"

        allianceNumber: What playoff alliance the team is on

        allianceRole: What role the team is in the alliance. 
        Ex: "Captain", "Round1-3", "Backup" or "None"   
        """

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/rankings/district/allianceSelectionCalculation?tournamentType={tournamentType}&sizeType={str(NumberOfAlliances) + 'Alliance'}&allianceNumber={allianceNumber}&allianceRole={allianceRole}"

        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        return int(response.text)

    def Playoff_Advancement_Points(self, tournamentType : str, quarterFinalWins : int, semiFinalWins : int, finalWins : int, season : int = None):

        """
        might be down test later
        This function returns the playoff advancement points for a given team.

        tournamentType: The type of tournament the team is in. 
        Ex: "DistrictEvent" or "Championship" check docs for all of the types.

        quarterFinalWins: The number of quarter finals the team has won.

        semiFinalWins: The number of semi finals the team has won.

        finalWins: The number of finals the team has won.
        """

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/rankings/district/playoffAdvancementCalculation?tournamentType={tournamentType}&quarterFinalWins={quarterFinalWins}&semiFinalWins={semiFinalWins}&finalWins={finalWins}"

        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        return response.text

    def Event_Rankings(self, event_code : str, team_number : int = None, top : int = None, season : int = None, use_predifend_infomation : bool = False):
        """
        This function returns the rankings of a event.

        event_code: The event code of the event.
        
        Team_number: The team number of the team.

        top: The number of teams to return.
        """

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/rankings/{event_code}"
        if use_predifend_infomation:  
            if self.team_number:
                url += f"?teamNumber={self.team_number}"
        else:
            if team_number:
                url += f"?teamNumber={team_number}"
            elif top:
                url += f"?top={top}"
        
        print(url, self.headers)
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        return response.text

    def Distirct_Rankings(self, District : str = None, teamNumber : int = None, page : int = None, top : int = None, season : int = None):

        """
        District: The district you want to get the rankings for.
        Ex: "NE" or "ONT"

        teamNumber: The team number of the team.
        If you have specified a team number when initializing the class and you want to get all teams feed teamNumber "All".

        page: The page of the rankings you want to get.
        Can't be used with top.

        top: The number of teams to return.
        Can't be used with page.
        """

        url = f"https://frc-api.firstinspires.org/v3.0/{self.season if not season else season}/rankings/district?"

        if District or self.District and not self.team_number and not teamNumber:
            url += f"districtCode={self.District if not District else District}"
    
        if teamNumber:
            url += f"&teamNumber={teamNumber}"

        elif page:
            url += f"&page={page}"

        elif top:
            url += f"&top={top}"
            
        elif self.team_number and str(teamNumber).upper() != "ALL":
            url += f"&teamNumber={self.team_number}"

        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        return response.text


