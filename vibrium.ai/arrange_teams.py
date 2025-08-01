'''
Given two teams (back row and front row), each with 5 players, determine if a group photo is
possible such that every player in the back row is taller than the corresponding player in 
the front row.

Anonymous clarified the problem requirements and confirmed assumptions with the interviewer.
'''

def arrange_teams(back_team, front_team):
    back_team.sort()
    front_team.sort()
    
    for back, front in zip(back_team, front_team):
        if back <= front:
            return False
    return True
    
if __name__ == "__main__":
    back_team = [67, 87, 12, 37, 78]
    front_team = [5, 77, 23, 54, 79]
    print("Is it possible to arrange the teams: ",arrange_teams(back_team, front_team))
