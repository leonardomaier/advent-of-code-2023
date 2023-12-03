with open('./inputs/day02.txt') as f:

    ans = []

    for line in f.readlines():

        bag_min = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        current_line = line.strip()

        game, plays = current_line.split(': ')

        _, gameId = game.split(' ')

        for play in plays.split('; '):

            for grab in play.split(', '):

                quantity, color = grab.split(' ')

                if int(quantity) > bag_min[color]:
                    bag_min[color] = int(quantity)

        temp = 1

        for cube_val in bag_min.values():
            temp = cube_val * temp
        
        ans.append(temp)

    print(sum(ans))