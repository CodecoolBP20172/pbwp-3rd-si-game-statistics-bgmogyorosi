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


file_name = 'game_stat.txt'
datas = {}
reportsOOP.get_datas(datas)
repo = reportsOOP.Report(file_name)

# Exercise 1
print_exercise(1)
print(repo.count_games())

# Exercise 2
print_exercise(2)
print(repo.decide(datas['year']))

# Exercise 3
print_exercise(3)
print(repo.get_latest())

# Exercise 4
print_exercise(4)
print(repo.count_by_genre(datas['genre']))

# Exercise 5
print_exercise(5)
try:
    print(repo.get_line_number_by_title(datas['title']))
except ValueError:
    print('There is no game called {}!'.format(datas['title']))

# Exercise 6
print_exercise(6)
for title in repo.sort_abc():
    print(title)

# Exercise 7
print_exercise(7)
for genre in repo.get_genres():
    print(genre)

# Exercise 8
print_exercise(8)
try:
    print(repo.when_was_top_sold_fps())
except ValueError:
    print('There is not fps game in the stat!')