def tournamentWinner(competitions, results):
    score = {}

    for i in range(len(competitions)):
        winner = competitions[i][0] if results[i] == 1 else competitions[i][1]
        if winner in score:
            score[winner] += 1
        else:
            score[winner] = 1
    
    return max(score, key=score.get)
