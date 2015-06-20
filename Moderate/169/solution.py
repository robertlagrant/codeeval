import sys
import re

with open(sys.argv[1], 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        params = line.split()
        
        regex_string = params[0]
        regex_string = regex_string.replace('.', '\.')
        regex_string = regex_string.replace('*', '.*')
        regex_string = regex_string.replace('?', '.')
        regex_string = '^' + regex_string + '$'
        regex = re.compile(regex_string)
        
        matching_filenames = []
        for filename in params[1:]:
            if regex.match(filename):
                matching_filenames.append(filename)
        
        if matching_filenames:
            print(' '.join(matching_filenames))
        else:
            print('-')