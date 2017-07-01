# Export functions

import reportsOOP


def export_game_datas(repo, file_export='export_stat.txt', title='Counter-Strike'):
    content = []
    content.append(str(repo.get_most_played()))
    content.append(str(repo.sum_sold()))
    content.append(str(repo.get_selling_avg()))
    content.append(str(repo.count_longest_title()))
    content.append(str(repo.get_date_avg()))
    try:
        content.append(str(repo.get_game(title)))
    except ValueError:
        content.append('There is no game called {}'.format(title))
    genres = repo.count_grouped_by_genre()
    content.append('//'.join(['{}: {}'.format(list(genres.keys())[i], list(genres.values())[i]) for i in range(len(genres))]))
    content.append(str('//'.join(repo.get_date_ordered())))
    line_amount = len(content)
    content = '\n'.join(content)
    file = open(file_export, "w")
    file.write(content)
    file.close()
    print('Export to {} has made successfully. There are {} lines exported.'.format(file_export, line_amount))


def main():
    repo = reportsOOP.Report('game_stat.txt')
    export_game_datas(repo)


if __name__ == '__main__':
    main()
