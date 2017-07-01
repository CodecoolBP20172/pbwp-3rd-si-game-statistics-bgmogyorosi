# Printing functions


import reports
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


def printing(file_name, repo):
    # Exercise 1
    print_exercise(1)
    print('Title of the most played game: {}'.format(reports.get_most_played(file_name)))
    print('Title of the most played game: {}'.format(repo.get_most_played()))
    # Exercise 2
    print_exercise(2)
    print('Total copies sold: {}'.format(reports.sum_sold(file_name)))
    print('Total copies sold: {}'.format(repo.sum_sold()))
    # Exercise 3
    print_exercise(3)
    print('Average of the sellings: {}'.format(reports.get_selling_avg(file_name)))
    print('Average of the sellings: {}'.format(repo.get_selling_avg()))
    # Exercise 4
    print_exercise(4)
    print('Longest title in the statistics: {}'.format(reports.count_longest_title(file_name)))
    print('Longest title in the statistics: {}'.format(repo.count_longest_title()))
    # Exercise 5
    print_exercise(5)
    print('The average of the release dates: {}'.format(reports.get_date_avg(file_name)))
    print('The average of the release dates: {}'.format(repo.get_date_avg()))
    # Exercise 6
    print_exercise(6)
    print('What are the properties of the given game?')
    title = input('Please give the title of the game: ')
    try:
        print(reports.get_game(file_name, title))
        print(repo.get_game(title))
    except ValueError:
        print('There is no game with the title {}'.format(title))
    # Exercise 7
    print_exercise(7)
    print('Genres in the statistics: ')
    print(reports.count_grouped_by_genre(file_name))
    print(repo.count_grouped_by_genre())
    # Exercise 8
    print_exercise(8)
    print('Date ordered games: ')
    print(reports.get_date_ordered(file_name))
    print(repo.get_date_ordered())


def main():
    file_name = 'game_stat.txt'
    repo = reportsOOP.Report(file_name)
    printing(file_name, repo)


if __name__ == '__main__':
    main()