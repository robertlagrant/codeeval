import sys

# Get list of month names and a count of months, inclusive, between two months
def list_months(start_month, end_month):
    if start_month == end_month:
        return (start_month)
            
    start_found = False
    list_of_months = list()

    for month in ( 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ):
        if month == start_month:
            start_found = True
            list_of_months.append(month)
            
        elif month == end_month:
            list_of_months.append(month)
            return list_of_months
            
        elif start_found:
            list_of_months.append(month)

# Get list of years, inclusive, as ints
def list_years(start_year, end_year):
    return range(start_year, end_year+1)


lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.strip()
    if line is '':
        continue

    dates = line.split('; ')
    results = {}
    
    for date in dates:
        start_string, end_string = date.split('-')
        start_year, start_month = int(start_string.split()[1]), start_string.split()[0]
        end_year, end_month = int(end_string.split()[1]), end_string.split()[0]
        years = list_years(start_year, end_year)
        
        # Add default dict entries
        for year in years:
            if year not in results:
                results[year] = set()

            start = 'Jan'; end = 'Dec'
                
            if year == start_year:
                start = start_month
            if year == end_year:
                end = end_month
                
            for month in list_months(start, end):
                results[year].add(month)

    # Now we have a dict with years as keys and sets of months as values. Just add the months!
    months_count = 0
    for year, months_set in results.items():
        months_count += len(months_set)
    
    #years = months_count/12
    years = (months_count + 12 // 2) // 12
    print(str(years))
    
lines.close()