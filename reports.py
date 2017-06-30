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


def count_games(file_name):
    games = import_games(file_name)
    return len(games)


def decide(file_name, year):
    games = import_games(file_name)
    for i in range(len(games)):
        if games[i][2] == year:
            return True
    return False


def get_latest(file_name):
    games = import_games(file_name)
    max_index = 0
    for i in range(len(games)):
        if games[i][2] > games[max_index][2]:
            max_index = i
    return games[max_index][0]


def count_by_genre(file_name, genre):
    games = import_games(file_name)
    genre_sum = 0
    for game in games:
        if game[3] == genre:
            genre_sum += 1
    return genre_sum


def get_line_number_by_title(file_name, title):
    games = import_games(file_name)
    for i in range(len(games)):
        if games[i][0] == title:
            return i + 1
    raise ValueError
