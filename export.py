# Export functions


import reportsOOP


file_name = 'game_stat.txt'
file_export = 'export_stat.txt'
repo = reportsOOP.Report(file_name)

content = ''
content += str(repo.count_games()) + '\n'
content += str(repo.decide(2000)) + '\n'
content += str(repo.get_latest()) + '\n'
content += str(repo.count_by_genre("First-person shooter")) + '\n'
content += str(repo.get_line_number_by_title("Counter-Strike")) + '\n'
content += str(repo.sort_abc()) + '\n'
content += str(repo.get_genres()) + '\n'
content += str(repo.when_was_top_sold_fps()) + '\n'

file = open(file_export, "w")
file.write(content)
file.close()
