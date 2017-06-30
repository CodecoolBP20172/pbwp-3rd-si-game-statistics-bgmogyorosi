# Printing functions


import reports


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

# Exercise 1
print_exercise(1)
print(reports.count_games(file_name))

# Exercise 2
print_exercise(2)
print(reports.decide(file_name, 2000))

# Exercise 3
print_exercise(3)
print(reports.get_latest(file_name))

# Exercise 4
print_exercise(4)
print(reports.count_by_genre(file_name, "First-person shooter"))

# Exercise 5
print_exercise(5)
print(reports.get_line_number_by_title(file_name, "Counter-Strike"))

# Exercise 6
print_exercise(6)
for title in reports.sort_abc(file_name):
    print(title)

# Exercise 7
print_exercise(7)
for genre in reports.get_genres(file_name):
    print(genre)

# Exercise 8
print_exercise(8)
print(reports.when_was_top_sold_fps(file_name))