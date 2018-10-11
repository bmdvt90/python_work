# Start with players that are trying out for the team,
# as each player makes the team, move them to the roster.
tryout_players = ["bennett","archer","teddy","matthew","joe","william","jack"]
team_roster = []
player = ""
# Verify each player and move them to the roster
while tryout_players:
	player = tryout_players.pop()
	print("Congratulations " + player.title() + "! You made the team.")
	team_roster.append(player)
print("\nThe following players have made the team:")
for player in team_roster:
	print(player.title())