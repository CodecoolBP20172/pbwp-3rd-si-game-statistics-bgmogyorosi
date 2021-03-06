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


def get_sorted_strings(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1):
            if arr[j].lower() > arr[i].lower():
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


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
    raise ValueError('Invalid title')


def sort_abc(file_name):
    games = import_games(file_name)
    titles = []
    for game in games:
        titles.append(game[0])
    # return sorted(titles)
    return get_sorted_strings(titles)


def get_genres(file_name):
    games = import_games(file_name)
    genres = []
    for game in games:
        if game[3] not in genres:
            genres.append(game[3])
    return get_sorted_strings(genres)


def when_was_top_sold_fps(file_name):
    games = import_games(file_name)
    max_fps = -1
    for i in range(len(games)):
        if games[i][3] == "First-person shooter":
            max_fps = i
            break
    if max_fps == -1:
        raise ValueError
    for i in range(len(games)):
        if games[i][3] == "First-person shooter" and games[i][1] > games[max_fps][1]:
            max_fps = i
    return games[max_fps][2]
