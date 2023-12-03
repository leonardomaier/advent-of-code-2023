import re

with open('./inputs/day01.txt') as f:
    result = []

    for line in f.readlines():
        current_line = line.strip()
        
        line_only_numbers = re.sub(r'\D', '', current_line)
        
        first_and_last_digits_integer = int(f'{line_only_numbers[0]}{line_only_numbers[-1]}')

        result.append(first_and_last_digits_integer)
    
    print(sum(result))