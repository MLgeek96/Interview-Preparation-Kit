from typing import List

def tournamentWinner(competitions, results):
    """
    There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible. Teams compete in round robin, where each team faces off against all other teams. Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team. In each competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.

    Given an array of pairs representing the teams that have competed against each other and an array containing the results of each competition, write a function that returns the winner of the tournament. The input arrays are named competitions and results, respectively. The competitions array has elements in the form of [homeTeam, awayTeam], where each team is a string of at most 30 characters representing the name of the team. The results array contains information about the winner of each corresponding competition in the competitions array. Specifically, results[i] denotes the winner of competitions[i], where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won.

    It's guaranteed that exactly one team will win the tournament and that each team will compete all other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.

    Sample Input:
    competitions = [
        ["HTML", "CSS"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]

    Sample Output:
    "Python"

    Hints:
    1. Don't overcomplicate this problem. How would you solve it by hand? Consider that approach, and try to translate it into code.

    2. Use a hash table to store the total points collected by each team, with the team names as keys in the hash table. Once you know how many points each team has, how can you determine which one is the winner?

    3. Loop through all of the competitions, and update the hash table at every iteration. FOr each competition, consider the name of the winning team; if the name already exists in the hash table, update that entry by adding 3 points to it. If the team name doesn't exist in the hash table, add a new entry in the hash table with the key as the team name and the value as 3 (since the team won its first competition). While looping through all of the competitions, keep track of the team with the highest score, and at the end of the algorithm, return the team with the highest score.

    Optimal Space & Time Complexity:
    O(n) time | O(k) space - where n is the number of competitions and k is the number of teams
    """
    HOME_TEAM_WON = 1

    # O(n) time | O(k) space
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam

def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points

if __name__ == "__main__":
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results =  [0, 0, 1]
    assert tournamentWinner(competitions, results) == "Python"

    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 1, 1]
    assert tournamentWinner(competitions, results) == "Java"
    
    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"]
    ]
    results = [0, 1, 1, 1, 0, 1]
    assert tournamentWinner(competitions, results) == "C#"

    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"]
    ]
    results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]
    assert tournamentWinner(competitions, results) == "C#"

    competitions = [
        ["Bulls", "Eagles"]
    ]
    results = [1]
    assert tournamentWinner(competitions, results) == "Bulls"

    competitions = [
        ["Bulls", "Eagles"],
        ["Bulls", "Bears"],
        ["Bears", "Eagles"]
    ]
    results = [0, 0, 0]
    assert tournamentWinner(competitions, results) == "Eagles"

    competitions = [
        ["Bulls", "Eagles"],
        ["Bulls", "Bears"],
        ["Bulls", "Monkeys"],
        ["Eagles", "Bears"],
        ["Eagles", "Monkeys"],
        ["Bears", "Monkeys"]
    ]
    results = [1, 1, 1, 1, 1, 1]
    assert tournamentWinner(competitions, results) == "Bulls"

    competitions = [
        ["AlgoMasters", "FrontPage Freebirds"],
        ["Runtime Terror", "Static Startup"],
        ["WeC#", "Hypertext Assassins"],
        ["AlgoMasters", "WeC#"],
        ["Static Startup", "Hypertext Assassins"],
        ["Runtime Terror", "FrontPage Freebirds"],
        ["AlgoMasters", "Runtime Terror"],
        ["Hypertext Assassins", "FrontPage Freebirds"],
        ["Static Startup", "WeC#"],
        ["AlgoMasters", "Static Startup"],
        ["FrontPage Freebirds", "WeC#"],
        ["Hypertext Assassins", "Runtime Terror"],
        ["AlgoMasters", "Hypertext Assassins"],
        ["WeC#", "Runtime Terror"],
        ["FrontPage Freebirds", "Static Startup"]
    ]
    results =  [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
    assert tournamentWinner(competitions, results) == "AlgoMasters"    

    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"]
    ]
    results = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1]
    assert tournamentWinner(competitions, results) == "SQL"

    competitions = [
         ["A", "B"]
    ]
    results = [0]
    assert tournamentWinner(competitions, results) == "B"