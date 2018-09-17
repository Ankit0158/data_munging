
def get_smallest_temperrature():
	weather_data_file_path = 'weather.dat'
	with open(weather_data_file_path) as weather_data:
		smallest_temp_data = dict()
		min_column_count = 14
		max_column_count = 15
		day_column_index = 0
		min_temp_column_index = 2
		for weather_report in weather_data:
			report = weather_report.split()
			if len(report) == min_column_count or len(weather_report.split()) == 15:
				day = report[day_column_index]
				min_temp = report[min_temp_column_index]
				if 'min_temp' not in smallest_temp_data:
					smallest_temp_data['day_number'] = day
					smallest_temp_data['min_temp'] = min_temp
				elif smallest_temp_data['min_temp'] >  min_temp:
					smallest_temp_data['day_number'] = day
					smallest_temp_data['min_temp'] = min_temp
		weather_data.close()
		return smallest_temp_data

def get_football_match_smallest_for_against_diffrence	
	football_match_data_file_path = 'football.dat'
	with open(football_match_data_file_path) as football_match_data:
		match_column_count = 10
		team_name_column_index = 1
		goals_score_column_index = 6
		against_score_column_index = 8
		smallest_for_against_diffrence = dict()
		for match in football_match_data:
			match_result = match.split()
			if len(match_result) == match_column_count:
				team_name = match_result[team_name_column_index]
				diffrence = abs(int(match_result[goals_score_column_index]) - int(match_result[against_score_column_index]))
				if 'difference' not in smallest_for_against_diffrence:
					smallest_for_against_diffrence['team_name'] = team_name
					smallest_for_against_diffrence['difference'] = diffrence
				elif smallest_for_against_diffrence['difference'] > diffrence:
					smallest_for_against_diffrence['team_name'] = team_name
					smallest_for_against_diffrence['difference'] = diffrence
		football_match_data.close()


