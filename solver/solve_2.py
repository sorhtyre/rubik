'''Rubik's solver functions'''

from data.cube import pieces
from solver.si import do_move, do_seq


def find_solution():
    '''Find solution'''

    tmp_pieces = [['W', 'R', 'G'], ['W', 'B', 'R'],
                  ['W', 'G', 'O'], ['W', 'O', 'B']]

    find_5(find_piece(tmp_pieces[0]))
    find_6(find_piece(tmp_pieces[1]))
    find_7(find_piece(tmp_pieces[2]))
    find_8(find_piece(tmp_pieces[3]))

    return(pieces[8] == 'W' and pieces[51] == 'O' and pieces[29] == 'B' and
           pieces[2] == 'W' and pieces[45] == 'O' and pieces[17] == 'G' and
           pieces[6] == 'W' and pieces[44] == 'R' and pieces[27] == 'B' and
           pieces[0] == 'W' and pieces[38] == 'R' and pieces[15] == 'G')


def find_piece(t_piece):
    '''Find piece'''

    tmp_corners = [[0, 38, 15],  [2, 17, 45],  [6, 27, 44],  [8, 51, 29],
                   [18, 42, 33], [20, 35, 53], [24, 9, 36],  [26, 47, 11]]

    for w_items in tmp_corners[:]:
        if t_piece[0] in [pieces[w_items[0]],
                          pieces[w_items[1]],
                          pieces[w_items[2]]]:
            if t_piece[1] in [pieces[w_items[0]],
                              pieces[w_items[1]],
                              pieces[w_items[2]]]:
                if t_piece[2] in [pieces[w_items[0]],
                                  pieces[w_items[1]],
                                  pieces[w_items[2]]]:
                    return w_items
    return None


def find_5(top_left):
    '''Find 1'''

    pos = {
        0:  [],
        2:  ['7', '10', '8', '5', '9', '6'],
        6:  ['3', '9', '4', '1', '10', '2'],
        8:  ['8', '10', '7', '10', '1', '9', '2'],
        9:  ['1', '9', '2'],
        11: ['10', '1', '9', '9', '2'],
        15: ['1', '9', '2', '10', '1', '9', '2'],
        17: ['7', '10', '8', '9', '5', '10', '6'],
        18: ['7', '9', '8', '9', '5', '10', '6'],
        20: ['9', '7', '5', '9', '9', '6', '8'],
        24: ['10', '7', '5', '9', '9', '6', '8'],
        26: ['7', '5', '9', '9', '6', '8'],
        27: ['3', '10', '4', '2', '6', '1', '5'],
        29: ['4', '9', '3', '5', '9', '6'],
        33: ['1', '10', '2'],
        35: ['5', '9', '9', '6'],
        36: ['9', '1', '10', '2'],
        38: ['5', '10', '6', '9', '5', '10', '6'],
        42: ['10', '1', '9', '2'],
        44: ['3', '9', '4', '10', '1', '9', '2'],
        45: ['7', '5', '9', '6', '8'],
        47: ['5', '9', '6'],
        51: ['8', '10', '7', '1', '10', '2'],
        53: ['1', '9', '9', '2']
    }

    for tmp_item in top_left:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_6(bot_left):
    '''Find 2'''

    pos = {
        0:  [],
        2:  ['6', '7', '10', '10', '5', '8'],
        6:  [],
        8:  ['8', '9', '7', '6', '10', '5'],
        9:  ['9', '6', '9', '5'],
        11: ['6', '9', '9', '5'],
        15: [],
        17: ['2', '6', '9', '9', '5', '1'],
        18: ['3', '9', '4', '6', '9', '9', '5'],
        20: ['4', '5', '3', '6', '3', '9', '4'],
        24: ['5', '4', '6', '3', '6', '10', '5'],
        26: ['6', '9', '5', '9', '6', '10', '5'],
        27: ['6', '10', '5', '9', '6', '10', '5'],
        29: ['8', '9', '7', '10', '6', '9', '5'],
        33: ['9', '6', '10', '5'],
        35: ['10', '6', '9', '5'],
        36: ['10', '6', '9', '9', '5'],
        38: [],
        42: ['4', '5', '3', '6'],
        44: ['3', '9', '4', '4', '5', '3', '6'],
        45: ['7', '3', '9', '9', '4', '8'],
        47: ['7', '6', '10', '5', '8'],
        51: ['6', '8', '10', '5', '7'],
        53: ['6', '10', '5']
    }

    for tmp_item in bot_left:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_7(top_right):
    '''Find 3'''

    pos = {
        0:  [],
        2:  [],
        6:  [],
        8:  ['4', '10', '3', '2', '9', '1'],
        9:  ['10', '7', '9', '8'],
        11: ['9', '7', '10', '8'],
        15: [],
        17: ['7', '10', '8', '2', '10', '1'],
        18: ['2', '10', '1', '7', '9', '8'],
        20: ['10', '2', '10', '1', '7', '9', '8'],
        24: ['7', '10', '10', '8', '2', '10', '1'],
        26: ['2', '10', '10', '1', '9', '2', '10', '1'],
        27: [],
        29: ['4', '2', '9', '1', '3'],
        33: ['9', '9', '2', '10', '1'],
        35: ['2', '9', '1'],
        36: ['10', '2', '10', '1'],
        38: [],
        42: ['2', '10', '10', '1'],
        44: [],
        45: ['2', '9', '1', '7', '9', '8'],
        47: ['10', '2', '9', '1'],
        51: ['4', '10', '3', '9', '2', '10', '1'],
        53: ['9', '2', '10', '1']
    }

    for tmp_item in top_right:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break


def find_8(bot_right):
    '''Find 4'''

    pos = {
        0:  [],
        2:  [],
        6:  [],
        8:  [],
        9:  ['8', '10', '10', '7'],
        11: ['10', '8', '10', '7'],
        15: [],
        17: [],
        18: ['3', '7', '4', '8', '10', '8', '10', '7'],
        20: ['8', '10', '10', '7', '9', '8', '10', '7'],
        24: ['8', '10', '7', '10', '8', '9', '7'],
        26: ['9', '8', '10', '7', '4', '9', '3'],
        27: [],
        29: ['8', '9', '7', '4', '9', '3'],
        33: ['9', '9', '4', '10', '3'],
        35: ['4', '9', '3'],
        36: ['4', '10', '10', '3'],
        38: [],
        42: ['8', '9', '7'],
        44: [],
        45: [],
        47: ['10', '4', '9', '3'],
        51: ['4', '10', '3', '8', '10', '7'],
        53: ['9', '4', '10', '3']
    }

    for tmp_item in bot_right:
        if pieces[tmp_item] == 'W':
            do_seq(pos[tmp_item])
            break
