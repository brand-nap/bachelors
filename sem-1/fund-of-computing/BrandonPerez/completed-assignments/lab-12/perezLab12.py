"""
Name: Brandon Perez
Class: CSCI 1411-006
Due Date: 11/17/23
Description: 
Status: works as expected
"""

def main():
    grid = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ];
    
    gameplay(grid);


def gameplay(grid, players = None, current = 1, position = [0, 0]):

    if players is None:
        players = [
            [input('Player 1, please enter your name: '), 'x'],
            [input('Player 2, please enter your name: '),'o']
            ];
        print();
    
    while playable(grid) and not check_row(grid, position[0]) and not check_column(grid, position[1]) and not check_diagonal(grid):
        
        current = (current+1)%2;
        
        position = input(f'\n{players[current][0]} where would you like to play (row, column): ').split(' ');
        
        if int(position[0]) < 1 or int(position[0]) > 3 or int(position[1]) < 1 or int(position[1]) > 3:
            print(f'Square Doesn\'t Exist: {players[current][0]} loses this turn');
            position = [0,0]
        else:
            position[0] = int(position[0]) - 1;
            position[1] = int(position[1]) - 1;
            if not place_entry(grid, position[0], position[1], players[current][1]):
                print(f'Square is already filled: {players[current][0]} loses this turn');
        print_grid(grid);
        print('\n');

    if check_row(grid, position[0]) or check_column(grid, position[1]) or check_diagonal(grid):
        print(f'{players[current][0]} Wins!');
    else:
        print(f'You both tied!');

    if input('Would you like to play again? (Y/N) ') == 'Y':
        reset_grid(grid);
        gameplay(grid, players);
 
def reset_grid(grid):
    for i in range(3):
        for j in range(3):
            grid[i][j] = ' ';
        
def check_row(grid, row_num):
    return grid[row_num][0] == grid[row_num][1] and grid[row_num][1] == grid[row_num][2] and grid[row_num][2] != ' '

def check_column(grid, col_num):
    return grid[0][col_num] == grid[1][col_num] and grid[1][col_num] == grid[2][col_num] and grid[2][col_num] != ' '

def check_diagonal(grid):
    return grid[0][0] == grid [1][1] and grid [1][1]==grid[2][2] and grid[2][0] == grid [1][1] and grid [1][1]==grid[0][2] and grid[1][1] != ' '
    
def place_entry(grid,row_num,col_num, ch):
    if grid[row_num][col_num] == ' ':
        grid[row_num][col_num] = ch
        return True
    return False

def playable(grid):
    for row in grid:
        for spot in row:
            if spot == ' ':
                return True
    return False

def print_grid(grid):
    for row in grid:
        print('-------------');
        for item in row:
            print(f'| {item} ', end = '')
        print('|');
    print('-------------');
        
        
