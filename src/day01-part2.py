word_to_number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open('./inputs/day01.txt') as f:
    sum = 0

    for line in f.readlines():
        digits = []

        for index, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
            
            for word in word_to_number_map.keys():
                if line[index:].startswith(word):
                    digits.append(word_to_number_map[word])
        
        sum += int(digits[0] + digits[-1])

    print(sum)