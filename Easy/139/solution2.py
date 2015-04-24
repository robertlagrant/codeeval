import sys

months = {
    'Jan': 0,
    'Feb': 1,
    'Mar': 2,
    'Apr': 3,
    'May': 4,
    'Jun': 5,
    'Jul': 6,
    'Aug': 7,
    'Sep': 8,
    'Oct': 9,
    'Nov': 10,
    'Dec': 11
}

lines = open(sys.argv[1], 'r')

for line in lines:
    line = line.strip()
    if line == '':
        continue
    
    # Make a big dict up front
    results = {i: [False for _ in range(12)] for i in range(1990, 2021)}
    dates = line.split('; ')
    
    for date in dates:
        start_string, end_string = date.split('-')
        start_month, start_year = [int(months.get(i, i)) for i in start_string.split()]
        end_month, end_year = [int(months.get(i, i))for i in end_string.split()]
        range_years = range(start_year, end_year + 1)

        for y in range_years:
            start_point = start_month if y == start_year else 0
            end_point = end_month + 1 if y == end_year else 12
            for month in range(start_point, end_point):
                results[y][month] = True

    months = sum(sum(1 for j in results[i] if j) for i in results.keys())
    print(str(months // 12))

lines.close()