import src.FrcWrapper as rankings

rank = rankings.Rankings(season=2022, team_number=865, District="ONT")

"A test for the calc_qual_proformance_points function"
print(rank.Qual_Performance_Points(tournamentType="Championship", qualificationRank=1, teamsAtEvent=10))

"A test for the Alliance_Selection_Points function"
print(rank.Alliance_Selection_Points(tournamentType="Championship", NumberOfAlliances="Eight", allianceNumber=1, allianceRole="Captain"))

"A test for the Playoff_Advancement_Points function"
print(rank.Playoff_Advancement_Points(tournamentType="Regional", quarterFinalWins=4, semiFinalWins=4, finalWins=4))

"A test for the Event_rankings function"
print(rank.Event_rankings(event_key="ON305"))

"A test for the Distirct_Rankings function"
print(rank.Distirct_Rankings(District="NE", top=10))
