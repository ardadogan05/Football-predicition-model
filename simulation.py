# from data_fetch import xg_form1, xg_form2, xg_seasonavg1, xg_seasonavg2, xga_form2, xga_form1, xga_seasonavg2, xga_seasonavg1, team1_h2h_xg, team2_h2h_xg, team1LeagueCoef, team2LeagueCoef, h2h_url
# from data_fetch import team1_name, team2_name
import numpy as np

N = 10000 #simulations

def calculateSimulation(stats):
    #determine lambda for team 1 and 2
    #try to get probability to match opta's, 
    team1LeagueCoef = stats["team 1 league coef"]
    team2LeagueCoef = stats["team 2 league coef"]

    team1League = stats["team 1 league"]
    team2League = stats["team 2 league"]

    team1_name = stats["team1 name"]
    team2_name = stats["team2 name"]

    homeAdvantage = stats["homeAdvantage"] # boost for home team, based on: https://www.premierleague.com/en/news/4032415, 1.1(very low) - 1.25 (average is 1.3)
    awayDisadvantage = stats["awayDisadvantage"]

    print(homeAdvantage, awayDisadvantage)

    h2h_url = stats["h2h url"]


    #maybe check home vs away advantage etc.
    lambda1 = 0.1875*stats["xG form 1"] + 0.1875*stats["xG szn avg 1"] + 0.1875*stats["xGa form 2"] + 0.1375*stats["xGa szn avg 2"] + 0.30*stats["xG h2h team 1"]  #lambda does not represent xG if h2h data is missing
    lambda2 = 0.1875*stats["xG form 2"] + 0.1875*stats["xG szn avg 2"] + 0.1875*stats["xGa form 1"] + 0.1375*stats["xGa szn avg 1"] + 0.30*stats["xG h2h team 2"] 


    lambda1 *= homeAdvantage 
    lambda2 *= awayDisadvantage 

    if (team1LeagueCoef == team2LeagueCoef) and h2h_url is not None:
        print(f"Expected goals for {team1_name} (H): {round(lambda1,3)} and {team2_name} (A) : {round(lambda2,3)}")
    else:
        #xG is no longer representative, we can only predict result, not goals
        lambda1 *=  team1LeagueCoef
        lambda2 *=  team2LeagueCoef



    t1_win = 0
    t2_win = 0
    draw = 0

    sim1 = np.random.poisson(lambda1,N)
    sim2 = np.random.poisson(lambda2,N)

    for i in range(N):
        if sim1[i]>sim2[i]:
            t1_win += 1
        elif sim2[i]>sim1[i]:
            t2_win += 1
        else: 
            draw += 1

    print(f'H: {t1_win/N}, D: {draw/N}, A: {t2_win/N}')
    team1WinRate = t1_win/N
    team2WinRate = t2_win/N
    drawRate = draw/N
    return team1WinRate, drawRate, team2WinRate, team1League, team2League
        



