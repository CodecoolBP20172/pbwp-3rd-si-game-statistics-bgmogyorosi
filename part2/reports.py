# Report functions


def import_games(file_name):
    file = open(file_name, "r")
    content = file.read().split('\n')
    games = []
    for line in content:
        game = line.split('\t') 
        if len(game) == 5:
            game[1] = float(game[1])
            game[2] = int(game[2])
            games.append(game)
    file.close()
    return games


def get_most_played(file_name):
    games = import_games(file_name)
    max_sold = 0
    for i in range(len(games)):
        if games[i][1] > games[max_sold][1]:
            max_sold = i
    return games[max_sold][0]


def sum_sold(file_name):
    games = import_games(file_name)
    return sum([game[1] for game in games])


def get_selling_avg(file_name):
    games = import_games(file_name)
    return sum_sold(file_name) / len(games)
    # return sum([game[1] for game in games]) / len(games)