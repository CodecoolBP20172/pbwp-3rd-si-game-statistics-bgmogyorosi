# Printing functions


import reportsOOP


def decor(func):
    def wrap(string):
        print("\n\n==================================================")
        func(string)
        print("==================================================")
    return wrap


@decor
def print_exercise(number):
    print('Exercise {}'.format(number))


def printing(repo):
    # Exercise 1
    print_exercise(1)
    print('Number of games: {}'.format(repo.count_games()))
    # Exercise 2
    print_exercise(2)
    print('Is there a game in the given year?')
    while True:
        try:
            year = int(input('Please give the year: '))
            break
        except ValueError:
            continue
    if repo.decide(year):
        print('There is at least one game in this year: {}.'.format(year))
    else:
        print('There is no game in this year: {}.'.format(year))
    # Exercise 3
    print_exercise(3)
    print('Latest game: {}'.format(repo.get_latest()))
    # Exercise 4
    print_exercise(4)
    print('How many games in a specific genre?')
    genre = input('Please give the genre: ')
    try:
        print('There are {} games in {} genre!'.format(repo.count_by_genre(genre), genre))
    except ValueError:
        print('There is no game in {} genre!'.format(genre))
    # Exercise 5
    print_exercise(5)
    print('Which is the line of the game with the given title?')
    title = input('Please give the title: ')
    try:
        print(repo.get_line_number_by_title(title))
    except ValueError:
        print('There is no game called {}!'.format(title))
    # Exercise 6
    print_exercise(6)
    print('Game titles in the statistics: ')
    for title in repo.sort_abc():
        print(title)
    # Exercise 7
    print_exercise(7)
    print('Genres in the statistics: ')
    for genre in repo.get_genres():
        print(genre)
    # Exercise 8
    print_exercise(8)
    try:
        print('The most sold fps game was sold in {}!'.format(repo.when_was_top_sold_fps()))
    except ValueError:
        print('There is not fps game in the stat!')


def main():
    file_name = 'game_stat.txt'
    repo = reportsOOP.Report(file_name)
    printing(repo)


if __name__ == '__main__':
    main()