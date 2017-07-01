# Report functions


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

    def get_most_played(self):
        max_sold = 0
        for i in range(len(self.games)):
            if self.games[i][1] > self.games[max_sold][1]:
                max_sold = i
        return self.games[max_sold][0]
        
    def sum_sold(self):
        return sum([game[1] for game in self.games])
    
    def get_selling_avg(self):
        return self.sum_sold() / len(self.games)

    def count_longest_title(self):
        max_len = 0
        for i in range(len(self.games)):
            if len(self.games[i][0]) > len(self.games[max_len][0]):
                max_len = i
        return len(self.games[max_len][0])

    def get_date_avg(self):
        return round(sum(game[2] for game in self.games) / len(self.games))

    def get_game(self, title):
        for i in range(len(self.games)):
            if self.games[i][0] == title:
                return self.games[i]
        raise ValueError
    
    def count_grouped_by_genre(self):
        genres = {}
        for game in self.games:
            if not genres.get(game[3]):
                genres.update({game[3]: 0})
            genres[game[3]] += 1
        return genres
    
    def get_date_ordered(self):
        # Ordering in ascending, but we order the negative of the year in asc, so it is desc
        return [game[0] for game in sorted(self.games, key=lambda x: (-x[2], x[0]), reverse=False)]
