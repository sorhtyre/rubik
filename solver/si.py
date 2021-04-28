'''Solver interface functions'''

from data.cube import side_1, side_2, side_3, side_4, side_5, side_6
from data.cube import edge_1, edge_2, edge_3, edge_4, edge_5, edge_6
from data.cube import center_1, center_2, center_3
from data.cube import s_moves
from game.move import rotate_cw, rotate_ccw


def do_move(tmp_var):
    '''Execute move'''

    if tmp_var == '1':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        s_moves.append('[ 1] Side 2 - CW\r')
    elif tmp_var == '2':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        s_moves.append('[ 2] Side 2 - CCW\r')
    elif tmp_var == '3':
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        s_moves.append('[ 3] Side 4 - CCW\r')
    elif tmp_var == '4':
        rotate_cw(side_4)
        rotate_cw(edge_4)
        s_moves.append('[ 4] Side 4 - CW\r')
    elif tmp_var == '5':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        s_moves.append('[ 5] Side 5 - CCW\r')
    elif tmp_var == '6':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        s_moves.append('[ 6] Side 5 - CW\r')
    elif tmp_var == '7':
        rotate_cw(side_6)
        rotate_cw(edge_6)
        s_moves.append('[ 7] Side 6 - CW\r')
    elif tmp_var == '8':
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        s_moves.append('[ 8] Side 6 - CCW\r')
    elif tmp_var == '9':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        s_moves.append('[ 9] Side 3 - CW\r')
    elif tmp_var == '10':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        s_moves.append('[10] Side 3 - CCW\r')
    elif tmp_var == '11':
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        s_moves.append('[11] Side 1 - CCW\r')
    elif tmp_var == '12':
        rotate_cw(side_1)
        rotate_cw(edge_1)
        s_moves.append('[12] Side 1 - CW\r')
    elif tmp_var == 'SL':
        rotate_cw(side_2)
        rotate_cw(edge_2)
        rotate_ccw(center_1)
        rotate_ccw(side_4)
        rotate_ccw(edge_4)
        s_moves.append('[SL] Shift cube left\r')
    if tmp_var == 'SR':
        rotate_ccw(side_2)
        rotate_ccw(edge_2)
        rotate_cw(center_1)
        rotate_cw(side_4)
        rotate_cw(edge_4)
        s_moves.append('[SR] Shift cube right\r')
    elif tmp_var == 'SU':
        rotate_ccw(side_5)
        rotate_ccw(edge_5)
        rotate_ccw(center_2)
        rotate_cw(side_6)
        rotate_cw(edge_6)
        s_moves.append('[SU] Shift cube up\r')
    elif tmp_var == 'SD':
        rotate_cw(side_5)
        rotate_cw(edge_5)
        rotate_cw(center_2)
        rotate_ccw(side_6)
        rotate_ccw(edge_6)
        s_moves.append('[SR] Shift cube down\r')
    elif tmp_var == 'RL':
        rotate_cw(side_3)
        rotate_cw(edge_3)
        rotate_ccw(center_3)
        rotate_ccw(side_1)
        rotate_ccw(edge_1)
        s_moves.append('[RL] Rotate cube left\r')
    elif tmp_var == 'RR':
        rotate_ccw(side_3)
        rotate_ccw(edge_3)
        rotate_cw(center_3)
        rotate_cw(side_1)
        rotate_cw(edge_1)
        s_moves.append('[RR] Rotate cube right\r')
