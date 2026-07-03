# test_leaderboard.py
# Kleine test om te checken of leaderboard.py goed werkt.
# Run met: python test_leaderboard.py

import leaderboard

# Test 1: multiplayer scores worden gesorteerd op punten (hoog naar laag)
leaderboard.reset()
leaderboard.zet_max(None)
leaderboard.voeg_multi_toe("Ali", 300, 2)
leaderboard.voeg_multi_toe("Sam", 500, 3)
leaderboard.voeg_multi_toe("Bo", 100, 1)
lijst = leaderboard.get_scores()
assert lijst[0][0] == "Sam"   # hoogste punten staat bovenaan
assert lijst[1][0] == "Ali"
assert lijst[2][0] == "Bo"
print("Test 1 OK: sorteren werkt")

# Test 2: single player houdt maar 5 scores over (top 5)
leaderboard.reset()
leaderboard.zet_max(5)
leaderboard.voeg_single_toe(100, 1)
leaderboard.voeg_single_toe(200, 1)
leaderboard.voeg_single_toe(300, 1)
leaderboard.voeg_single_toe(400, 1)
leaderboard.voeg_single_toe(500, 1)
leaderboard.voeg_single_toe(600, 1)   # 6e score, 100 moet eruit vallen
lijst = leaderboard.get_scores()
assert len(lijst) == 5                # er blijven maar 5 over
assert lijst[0][1] == 600             # hoogste bovenaan
assert lijst[4][1] == 200             # laagste van de top 5
print("Test 2 OK: top 5 werkt")

# Test 3: bij gelijke punten sorteren we op level
leaderboard.reset()
leaderboard.zet_max(None)
leaderboard.voeg_multi_toe("A", 200, 1)
leaderboard.voeg_multi_toe("B", 200, 4)
lijst = leaderboard.get_scores()
assert lijst[0][0] == "B"             # zelfde punten, hoger level eerst
print("Test 3 OK: level als tiebreak werkt")

# Test 4: reset maakt de lijst leeg
leaderboard.reset()
assert len(leaderboard.get_scores()) == 0
print("Test 4 OK: reset werkt")

print("Alle tests geslaagd!")
