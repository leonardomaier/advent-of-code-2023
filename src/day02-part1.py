with open('./inputs/day02.txt') as f:

    valid_games = []

    for line in f.readlines():

        current_line = line.strip()

        game, plays = current_line.split(': ')

        _, gameId = game.split(' ')

        is_game_valid = True
        
        for play in plays.split('; '):

            bag = {
                'red': 12,
                'green': 13,
                'blue': 14
            }

            for grab in play.split(', '):

                quantity, color = grab.split(' ')

                bag[color] -= int(quantity)

            if bag['red'] < 0 or bag['green'] < 0 or bag['blue'] < 0:
                is_game_valid = False
                break
        
        if is_game_valid:
            valid_games.append(int(gameId))        

    print(sum(valid_games))