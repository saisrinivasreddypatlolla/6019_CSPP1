from collections import Counter
def winner_of_game(game):
    counter = Counter()
    flag = 0
    for row in game:
        for value in row:
            if value in ('x', 'o', '.'):
                counter[value] += 1
            elif value not in ('x', 'o', '.'):
                flag = 1
    if flag == 1:
        return "invalid input"
    if abs(counter['x']-counter['o']) == 1:
        if ((game[0][0] == 'x' and game[0][1] == 'x' and game[0][2] == 'x') or
                (game[1][0] == 'x' and game[1][1] == 'x' and game[1][2] == 'x') or
                (game[2][0] == 'x' and game[2][1] == 'x' and game[2][2] == 'x') or
                (game[0][0] == 'x' and game[1][0] == 'x' and game[2][0] == 'x') or
                (game[0][1] == 'x' and game[1][1] == 'x' and game[2][1] == 'x') or
                (game[0][2] == 'x' and game[1][2] == 'x' and game[2][2] == 'x') or
                (game[0][0] == 'x' and game[1][1] == 'x' and game[2][2] == 'x') or
                (game[0][2] == 'x' and game[1][1] == 'x' and game[2][0] == 'x')):
            return 'x'
        if ((game[0][0] == 'o' and game[0][1] == 'o' and game[0][2] == 'o') or
                (game[1][0] == 'o' and game[1][1] == 'o' and game[1][2] == 'o') or
                (game[2][0] == 'o' and game[2][1] == 'o' and game[2][2] == 'o') or
                (game[0][0] == 'o' and game[1][0] == 'o' and game[2][0] == 'o') or
                (game[0][1] == 'o' and game[1][1] == 'o' and game[2][1] == 'o') or
                (game[0][2] == 'o' and game[1][2] == 'o' and game[2][2] == 'o') or
                (game[0][0] == 'o' and game[1][1] == 'o' and game[2][2] == 'o') or
                (game[0][2] == 'o' and game[1][1] == 'o' and game[2][0] == 'o')):
            return 'o'
        return "draw"

    if abs(counter['x']-counter['o']) == 0 or abs(counter['x']-counter['o']) > 1:
        return "invalid game"
def main():
    '''
        Initialisation of matrix
        print addition of two matrices
        print multiplication of two matrices
    '''

    game = []
    for _ in range(3):
        row = list(map(str, input().split()))
        game.append(row)
    print(winner_of_game(game))

if __name__ == '__main__':
    main()