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
    return sum(game[1] for game in games)


def get_selling_avg(file_name):
    games = import_games(file_name)
    return sum_sold(file_name) / len(games)
    # return sum(game[1] for game in games) / len(games)


def count_longest_title(file_name):
    games = import_games(file_name)
    max_len = 0
    for i in range(len(games)):
        if len(games[i][0]) > len(games[max_len][0]):
            max_len = i
    return len(games[max_len][0])


def get_date_avg(file_name):
    games = import_games(file_name)
    return round(sum(game[2] for game in games) / len(games))


def get_game(file_name, title):
    games = import_games(file_name)
    for i in range(len(games)):
        if games[i][0] == title:
            break
    return games[i]


def count_grouped_by_genre(file_name):
    games = import_games(file_name)
    genres = {}
    for game in games:
        if not genres.get(game[3]):
            genres.update({game[3]: 0})
        genres[game[3]] += 1
    return genres


def get_date_ordered(file_name):
    games = import_games(file_name)
    titles = []
    # Ordering in ascending, but we order the negative of the year in asc, so it is desc
    games.sort(key=lambda x: (-x[2], x[0]), reverse=False)
    return [game[0] for game in games]
