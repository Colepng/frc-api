# import src.FrcApi as FrcApi
# import os
# from dotenv import load_dotenv
# load_dotenv()

# TOKEN = os.getenv("Frc-api-token")

# FrcApi.token(username="colepng", token=TOKEN, encoded = False)

# rank = FrcApi.Rankings(season = 2022, team_number = 865, District = "ONT")
    
# class TestRankings:
#     def test_one_Qual_Performance_Points(self):
#         """Test the function for calculating the qual performance points"""
#         assert rank.Qual_Performance_Points(tournamentType = "Championship", qualificationRank = 1, teamsAtEvent = 10) == 22
#         print("test one passed")

#     def test_two_Qual_Performance_Points(self):
#         """Test the function for calculating the qual performance points"""
#         assert rank.Qual_Performance_Points(tournamentType = "Championship", qualificationRank = 2, teamsAtEvent = 10) == 19

#     def test_three_Qual_Performance_Points(self):
#         """Test the function for calculating the qual performance points"""
#         assert rank.Qual_Performance_Points(tournamentType = "Regional", qualificationRank = 10, teamsAtEvent = 30) == 15

#     def test_one_Alliance_Selection_Points(self):
#         """Test the Alliance Selection Points function"""
#         assert rank.Alliance_Selection_Points(tournamentType = "Championship", NumberOfAlliances = "Sixteen", allianceNumber = 1, allianceRole = "Captain") == 0
    
#     def test_two_Alliance_Selection_Points(self):
#         """Test the Alliance Selection Points function"""
#         assert rank.Alliance_Selection_Points(tournamentType = "DistrictEvent", NumberOfAlliances = "Six", allianceNumber = 3, allianceRole = "Backup") == 0

#     def test_three_Alliance_Selection_Points(self):
#         """Test the Alliance Selection Points function"""
#         assert rank.Alliance_Selection_Points(tournamentType = "Regional", NumberOfAlliances = "Eight", allianceNumber = 7, allianceRole = "Round2") == 7

#     # def test_one_Playoff_Advancement_Points(self):
#     #     """Test the Playoff Advancement Points function"""
#         #     assert rank.Playoff_Advancement_Points(tournamentType = "Championship", quarterFinalWins = 1, semiFinalWins = 1, finalWins = 1) == 0
#         # """ Playoff Advancement Points are down right now. Test later """

#     def test_one_Event_Rankings(self):
#         """Test the District Points function"""
#         assert rank.Event_Rankings(event_code = "on305") == open(r"Tests\Test returns\District_Points_test_one.txt", "r").read()

#     def test_two_Event_Rankings(self):
#         """Test the District Points function"""
#         assert rank.Event_Rankings(event_code = "onbar", season=2020, use_predifend_infomation = True) == open(r"Tests\Test returns\District_Points_test_two.txt", "r").read()

#     def test_three_Event_Rankings(self):
#         """Test the District Points function"""
#         assert rank.Event_Rankings(event_code = "ONCMP", season=2022, top=10) == open(r"Tests\Test returns\District_Points_test_three.txt", "r").read()