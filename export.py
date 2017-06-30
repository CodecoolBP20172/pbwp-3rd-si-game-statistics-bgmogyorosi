# Export functions


import reports


file_name = 'game_stat.txt'
file_export = 'export_stat.txt'

content = ''
content += str(reports.count_games(file_name)) + '\n'
content += str(reports.decide(file_name, 2000)) + '\n'
content += reports.get_latest(file_name) + '\n'
content += str(reports.count_by_genre(file_name, "First-person shooter")) + '\n'
content += str(reports.get_line_number_by_title(file_name, "Counter-Strike")) + '\n'
content += str(reports.sort_abc(file_name)) + '\n'
content += str(reports.get_genres(file_name)) + '\n'
content += str(reports.when_was_top_sold_fps(file_name)) + '\n'

file = open(file_export, "w")
file.write(content)
file.close()