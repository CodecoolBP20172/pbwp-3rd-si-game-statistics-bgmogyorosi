# Export functions

import reportsOOP


def export_game_datas(repo, file_export='export_stat.txt', year=2000, genre='Firs-person shooter', title='Counter-Strike'):
    content = []
    content.append(str(repo.count_games()))
    content.append(str(repo.decide(year)))
    content.append(str(repo.get_latest()))
    content.append(str(repo.count_by_genre(genre)))
    try:
        content.append(str(repo.get_line_number_by_title(title)))
    except ValueError:
        content.append('There is no game called {}'.format(title))
    content.append(str('//'.join(repo.sort_abc())))
    content.append(str('//'.join(repo.get_genres())))
    try:
        content.append(str(repo.when_was_top_sold_fps()))
    except ValueError:
        content.append('There is no fps game!')
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
