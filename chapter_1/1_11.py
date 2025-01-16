current_population = 312032486
seconds_per_year = (365 * 24) * (60 * 60)

births_per_year = seconds_per_year // 7
deaths_per_year = seconds_per_year // 13
immigrants_per_year = seconds_per_year // 45

for year in range(1, 6):
    current_population += births_per_year - deaths_per_year + immigrants_per_year
    print('Year', year,':', 'Population = ', current_population)
