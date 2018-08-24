from collections import Counter
c = Counter()
def winner_of_game(game):
    flag = 0
    for i in game:
        for j in i:
            if j == 'x' or j == 'o' or j == ".":
                c[j] += 1
            elif j != 'x' and j != 'o' and j != ".":
                flag = 1
    if flag == 1:
        return "invalid input"
    if abs(c['x']-c['o']) == 1:
        if ((game[0][0]=='x' and game[0][1] == 'x' and game[0][2] == 'x') or
            (game[1][0]=='x' and game[1][1] == 'x' and game[1][2] == 'x') or
            (game[2][0]=='x' and game[2][1] == 'x' and game[2][2] == 'x') or
            (game[0][0]=='x' and game[1][0] == 'x' and game[2][0] == 'x') or
            (game[0][1]=='x' and game[1][1] == 'x' and game[2][1] == 'x') or
            (game[0][2]=='x' and game[1][2] == 'x' and game[2][2] == 'x') or
            (game[0][0]=='x' and game[1][1] == 'x' and game[2][2] == 'x') or
            (game[0][2]=='x' and game[1][1] == 'x' and game[2][0] == 'x')):
            return 'x'
        if ((game[0][0]=='o' and game[0][1] == 'o' and game[0][2] == 'o') or
            (game[1][0]=='o' and game[1][1] == 'o' and game[1][2] == 'o') or
            (game[2][0]=='o' and game[2][1] == 'o' and game[2][2] == 'o') or
            (game[0][0]=='o' and game[1][0] == 'o' and game[2][0] == 'o') or
            (game[0][1]=='o' and game[1][1] == 'o' and game[2][1] == 'o') or
            (game[0][2]=='o' and game[1][2] == 'o' and game[2][2] == 'o') or
            (game[0][0]=='o' and game[1][1] == 'o' and game[2][2] == 'o') or
            (game[0][2]=='o' and game[1][1] == 'o' and game[2][0] == 'o')):
            return 'o'
        return "draw"

    elif abs(c['x']-c['o']) == 0 or abs(c['x']-c['o']) > 1:
        return "invalid game"
    return 
def main():
    '''
        Initialisation of matrix
        print addition of two matrices
        print multiplication of two matrices
    '''

    game = []
    for _ in range(3):
        row = list(map(str,input().split()))
        game.append(row)
    print(winner_of_game(game))

if __name__ == '__main__':
    main()
