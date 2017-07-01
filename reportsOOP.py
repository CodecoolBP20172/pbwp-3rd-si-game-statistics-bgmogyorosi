# Report functions
def get_sorted_strings(arr):
        for i in range(1, len(arr)):
            for j in range(len(arr) - 1):
                if arr[j].lower() > arr[i].lower():
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return arr


class Report:

    file_name = ''

    games = []

    def __init__(self, file_name=None):
        self.file_name = file_name if file_name else 'game_stat.txt'
        self.import_games()

    def import_games(self):
        file = open(self.file_name, "r")
        content = file.read().split('\n')
        games = []
        for line in content:
            game = line.split('\t')
            if len(game) == 5:
                try:
                    game[1] = float(game[1])
                    game[2] = int(game[2])
                except ValueError:
                    continue
                games.append(game)
        file.close()
        self.games = games

    def count_games(self):
        return len(self.games)

    def decide(self, year):
        for i in range(len(self.games)):
            if self.games[i][2] == year:
                return True
        return False

    def get_latest(self):
        # max_index = 0
        # for i in range(len(self.games)):
        #    if self.games[i][2] > self.games[max_index][2]:
        #        max_index = i
        # return self.games[max_index][0]
        games = sorted(self.games, key=lambda x: x[2], reverse=True)
        return games[0][0]

    def count_by_genre(self, genre):
        # genre_sum = 0
        # for game in self.games:
        #    if game[3] == genre:
        #        genre_sum += 1
        # return genre_sum
        genre_sum = [1 for game in self.games if game[3] == genre]
        return sum(genre_sum)

    def get_line_number_by_title(self, title):
        for i in range(len(self.games)):
            if self.games[i][0] == title:
                return i + 1
        raise ValueError

    def sort_abc(self):
        return get_sorted_strings([game[0] for game in self.games])

    def get_genres(self):
        genres = []
        for game in self.games:
            if game[3] not in genres:
                genres.append(game[3])
        return get_sorted_strings(genres)

    def when_was_top_sold_fps(self):
        max_fps = -1
        genre = "First-person shooter"
        for i in range(len(self.games)):
            if self.games[i][3] == genre:
                max_fps = i
                break
        if max_fps == -1:
            raise ValueError
        for i in range(len(self.games)):
            if self.games[i][3] == genre and self.games[i][1] > self.games[max_fps][1]:
                max_fps = i
        return self.games[max_fps][2]
