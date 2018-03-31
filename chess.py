# CHESS ASSIGNMENT FOR CSC190, ROBIN LIN (1003993244)
from random import randint
import math
import operator
movecounter = 0

def init_board():
    #White: Offset=10
    #Black: Offset=20
    #Piece: Value
    #Pawn:   +0
    #Knight: +1
    #Bishop: +2
    #Rook:   +3
    #Queen:  +4
    #King:   +5
    #board index from 0 to 63 (64 total positions)
    state = [0] * 64
    # White pieces
    state[0] = 13
    state[1] = 11
    state[2] = 12
    state[3] = 14
    state[4] = 15
    state[5] = 12
    state[6] = 11
    state[7] = 13
    state[8] = 10
    state[9] = 10
    state[10] = 10
    state[11] = 10
    state[12] = 10
    state[13] = 10
    state[14] = 10
    state[15] = 10
    # Black pieces
    state[48] = 20
    state[49] = 20
    state[50] = 20
    state[51] = 20
    state[52] = 20
    state[53] = 20
    state[54] = 20
    state[55] = 20
    state[56] = 23
    state[57] = 21
    state[58] = 22
    state[59] = 24
    state[60] = 25
    state[61] = 22
    state[62] = 21
    state[63] = 23
    return state

def init_image():
    image = [0] * 64
    return image

def PrintBoard(state, image):
    for i in range(0,len(state)):
        # White pieces, pawn knight bishop rook queen and king
        if state[i] == 10:
            image[i] = "WP"
        elif state[i] == 11:
            image[i] = "Wk"
        elif state[i] == 12:
            image[i] = "WB"
        elif state[i] == 13:
            image[i] = "WR"
        elif state[i] == 14:
            image[i] = "WQ"
        elif state[i] == 15:
            image[i] = "WK"
        elif state[i] == 0:
            image[i] = "OO"

        # Black pieces, pawn knight bishop rook queen and king
        elif state[i] == 20:
            image[i] = "BP"
        elif state[i] == 21:
            image[i] = "Bk"
        elif state[i] == 22:
            image[i] = "BB"
        elif state[i] == 23:
            image[i] = "BR"
        elif state[i] == 24:
            image[i] = "BQ"
        elif state[i] == 25:
            image[i] = "BK"
        # Build the board schematic
    print "", str(image[56]), "|", str(image[57]), "|", str(image[58]), "|", str(image[59]), "|",  str(image[60]), "|", str(image[61]), "|", str(image[62]), "|",  str(image[63])
    print "--------------------------------------"
    print "", str(image[48]), "|", str(image[49]), "|", str(image[50]), "|", str(image[51]), "|", str(image[52]), "|", str(image[53]), "|", str(image[54]), "|", str(image[55])
    print "--------------------------------------"
    print "", str(image[40]), "|", str(image[41]), "|", str(image[42]), "|", str(image[43]), "|", str(image[44]), "|", str(image[45]), "|", str(image[46]), "|", str(image[47])
    print "--------------------------------------"
    print "", str(image[32]), "|", str(image[33]), "|", str(image[34]), "|", str(image[35]), "|", str(image[36]), "|", str(image[37]), "|", str(image[38]), "|", str(image[39])
    print "--------------------------------------"
    print "", str(image[24]), "|", str(image[25]), "|", str(image[26]), "|", str(image[27]), "|", str(image[28]), "|", str(image[29]), "|", str(image[30]), "|", str(image[31])
    print "--------------------------------------"
    print "", str(image[16]), "|", str(image[17]), "|", str(image[18]), "|", str(image[19]), "|", str(image[20]), "|", str(image[21]), "|", str(image[22]), "|", str(image[23])
    print "--------------------------------------"
    print "", str(image[8]), "|", str(image[9]), "|", str(image[10]), "|", str(image[11]), "|", str(image[12]), "|", str(image[13]), "|", str(image[14]), "|", str(image[15])
    print "--------------------------------------"
    print "", str(image[0]), "|", str(image[1]), "|", str(image[2]), "|", str(image[3]), "|", str(image[4]), "|", str(image[5]), "|", str(image[6]), "|", str(image[7])

def GetPlayerPositions(board, player):
    accumulatorwhite = []
    accumulatorblack = []
    if player == 10:
        for i in range(0, len(board)):
            if (board[i] >= 10) and (board[i] <= 15):
                accumulatorwhite = accumulatorwhite + [i]
        return accumulatorwhite
    elif player == 20:
        for i in range(0, len(board)):
            if (board[i] >= 20) and ((board[i]) <= 25):
                accumulatorblack = accumulatorblack + [i]
        return accumulatorblack
    else:
        print "ERROR OCCURED! PLEASE ENTER A VALID PLAYER NUMBER!"
        return -1

def getinfo(board,position,player):
        if board[position] == 0:
            return "blank"
        if board[position] == 20 or board[position] == 21 or board[position] == 22 or board[position] == 23 or board[position] == 24 or board[position] == 25:
            return "black"
        else:
            return "white"

def position_type(position):
    # Returns the type of position piece is currently in -> edge, corner, or center
    if (position == 0) or (position == 7) or (position == 56) or (position == 63):
        if (position == 0):
            return "BL"
        elif (position == 7):
            return "BR"
        elif (position == 56):
            return "TL"
        elif (position == 63):
            return "TR"
    elif (position % 8 == 0) and (position != 56) and (position != 0):
        return "LE"
    elif (position == 15) or (position == 23) or (position == 31) or (position == 39) or (position == 47) or (position == 55):
        return "RE"
    elif (position >= 1) and (position <= 6):
        return "BE"
    elif (position >= 57) and (position <= 62):
        return "TE"
    else:
        return "CENTER"

def horizontal(board, x, y, player):
    if player == 10:
        # Horizontal
        if x == 0:
            if board[y][1] == 25 or board[y][1] == 24 or board[y][1] == 23:
                return True
            for i in range(1, 8):
                if (board[y][i] == 0):
                    pass
                elif (board[y][i] == 23) or (board[y][i] == 24):
                    return True
                else:
                    return False
        elif x == 7:
            if board[y][6] == 25 or board[y][6] == 24 or board[y][6] == 23:
                return True
            for i in range(6, -1, -1):
                if (board[y][i] == 0):
                    pass

                elif (board[y][i] == 23) or (board[y][i] == 24):
                    return True
                else:
                    return False
        else:
            if board[y][x + 1] == 25:
                return True
            if board[y][x - 1] == 25:
                return True
            for i in range(x + 1, 8):
                if (board[y][i] == 0):
                    pass

                elif (board[y][i] == 23) or (board[y][i] == 24):
                    return True
                else:
                    return False
            for i in range(x - 1, -1, -1):
                if (board[y][i] == 0):
                    pass

                elif (board[y][i] == 23) or (board[y][i] == 24):
                    return True
                else:
                    return False
    if player == 20:
        # Horizontal
        if x == 0:
            if board[y][1] == 15 or board[y][1] == 14 or board[y][1] == 13:
                return True
            for i in range(1, 8):
                if (board[y][i] == 0):
                    pass
                elif (board[y][i] == 13) or (board[y][i] == 14):
                    return True
                else:
                    return False
        elif x == 7:
            if board[y][6] == 15 or board[y][6] == 14 or board[y][6] == 13:
                return True
            for i in range(6, -1, -1):
                if (board[y][i] == 0):
                    pass

                elif (board[y][i] == 13) or (board[y][i] == 14):
                    return True
                else:
                    return False
        else:
            if board[y][x + 1] == 15:
                return True
            if board[y][x - 1] == 15:
                return True
            for i in range(x + 1, 8):
                if (board[y][i] == 0):
                    pass

                elif (board[y][i] == 13) or (board[y][i] == 14):
                    return True
                else:
                    return False
            for i in range(x - 1, -1, -1):
                if (board[y][i] == 0):
                    pass
                elif (board[y][i] == 13) or (board[y][i] == 14):
                    return True
                else:
                    return False

def vertical(board, x, y, player):
    if player == 10:
        if y == 0:
            if board[1][x] == 25:
                return True
            for i in range(1, 8):
                if (board[i][x] == 0):
                    pass
                elif (board[i][x] == 23) or (board[i][x] == 24):
                    return True
                else:
                    return False
        if y == 7:
            if board[6][x] == 25:
                return True
            for i in range(6, -1, -1):
                if (board[i][x] == 0):
                    pass

                elif (board[i][x] == 23) or (board[i][x] == 24):
                    return True
                else:
                    return False
        else:
            if board[y + 1][x] == 25:
                return True
            if board[y - 1][x] == 25:
                return True
            for i in range(x + 1, 8):
                if (board[i][x] == 0):
                    pass

                elif (board[i][x] == 23) or (board[i][x] == 24):
                    return True
                else:
                    return False
            for i in range(x - 1, -1, -1):
                if (board[i][x] == 0):
                    pass

                elif (board[i][x] == 23) or (board[i][x] == 24):
                    return True
                else:
                    return False
    if player == 20:
        if y == 0:
            if board[1][x] == 15:
                return True
            for i in range(1, 8):
                if (board[i][x] == 0):
                    pass

                elif (board[i][x] == 13) or (board[i][x] == 14):
                    return True
                else:
                    return False
        if y == 7:
            if board[6][x] == 15:
                return True
            for i in range(6, -1, -1):
                if (board[i][x] == 0):
                    pass
                elif (board[i][x] == 13) or (board[i][x] == 14):
                    return True
                else:
                    return False
        else:
            if board[y + 1][x] == 15:
                return True
            if board[y - 1][x] == 15:
                return True
            for i in range(x + 1, 8):
                if (board[i][x] == 0):
                    pass
                elif (board[i][x] == 13) or (board[i][x] == 14):
                    return True
                else:
                    return False
            for i in range(x - 1, -1, -1):
                if (board[i][x] == 0):
                    pass
                elif (board[i][x] == 13) or (board[i][x] == 14):
                    return True
                else:
                    return False

def diagonal(board, x, y, player):
    xnew1 = x + 1
    ynew1 = y + 1
    xnew2 = x + 1
    ynew2 = y - 1
    xnew3 = x + 1
    ynew3 = y + 1
    xnew4 = x + 1
    ynew4 = y - 1
    xnew5 = x - 1
    ynew5 = y - 1
    xnew6 = x - 1
    ynew6 = y + 1
    xnew7 = x - 1
    ynew7 = y - 1
    xnew8 = x - 1
    ynew8 = y + 1

    if player == 10:
        #    up
        #   /
        #  /
        # /
        while (xnew1 <= 7) and (ynew1 <= 7):
            if (board[ynew1][xnew1] == 0):
                pass
            elif (board[ynew1][xnew1] == 22) or (board[ynew1][xnew1] == 24):
                return True
            else:
                return False
            xnew1 = xnew1 + 1
            ynew1 = ynew1 + 1
        # \
        #  \
        #   \
        #    down
        while (xnew2 <= 7) and (ynew2 >= 0):
            if (board[ynew2][xnew2] == 0):
                pass
            elif (board[ynew2][xnew2] == 22) or (board[ynew2][xnew2] == 24):
                return True
            else:
                return False
            xnew2 = xnew2 + 1
            ynew2 = ynew2 - 1
        #    /
        #   /
        #  /
        # down
        while (xnew5 >= 0) and (ynew5 >= 0):
            if (board[ynew5][xnew5] == 0):
                pass
            elif (board[ynew5][xnew5] == 22) or (board[ynew5][xnew5] == 24):
                return True
            else:
                return False
            xnew5 = xnew5 - 1
            ynew5 = ynew5 - 1

        # up
        #  \
        #   \
        #    \
        while (xnew6 >= 0) and (ynew6 <= 7):
            if (board[ynew6][xnew6] == 0):
                pass
            elif (board[ynew6][xnew6] == 22) or (board[ynew6][xnew6] == 24):
                return True
            else:
                return False
            xnew6 = xnew6 - 1
            ynew6 = ynew6 + 1

    if player == 20:
        #    up
        #   /
        #  /
        # /
        while (xnew3 <= 7) and (ynew3 <= 7):
            if (board[ynew3][xnew3] == 0):
                pass
            elif (board[ynew3][xnew3] == 12) or (board[ynew3][xnew3] == 14):
                return True
            else:
                return False
            xnew3 = xnew3 + 1
            ynew3 = ynew3 + 1
        # \
        #  \
        #   \
        #   down
        while (xnew4 <= 7) and (ynew4 >= 0):
            if (board[ynew4][xnew4] == 0):
                pass
            elif (board[ynew4][xnew4] == 12) or (board[ynew4][xnew4] == 14):
                return True
            else:
                return False
            xnew4 = xnew4 + 1
            ynew4 = ynew4 - 1

            #    /
            #   /
            #  /
            # down
            while (xnew7 >= 0) and (ynew7 >= 0):
                if (board[ynew7][xnew7] == 0):
                    pass
                elif (board[ynew7][xnew7] == 12) or (board[ynew7][xnew7] == 14):
                    return True
                else:
                    return False
                xnew7 = xnew7 - 1
                ynew7 = ynew7 - 1

            # up
            #  \
            #   \
            #    \
            while (xnew8 >= 0) and (ynew8 <= 7):
                if (board[ynew8][xnew8] == 0):
                    pass
                elif (board[ynew8][xnew8] == 12) or (board[ynew8][xnew8] == 14):
                    return True
                else:
                    return False
                xnew8 = xnew8 - 1
                ynew8 = ynew8 + 1

def diagonal_adjacency(board, position, player):
    if player == 10:
        # Classify type of position
        if position_type(position) == "BL":
            if (board[position + 9] == 20) or (board[position + 9] == 25):
                return True
        elif position_type(position) == "BR":
            if (board[position + 7] == 20) or (board[position + 7] == 25):
                return True
        elif position_type(position) == "TL":
            if (board[position - 7] == 25):
                return True
        elif position_type(position) == "TR":
            if (board[position - 9] == 25):
                return True
        elif position_type(position) == "LE":
            if (board[position - 7] == 25):
                return True
            elif (board[position + 9] == 25) or (board[position + 9] == 20):
                return True
        elif position_type(position) == "RE":
            if (board[position - 9] == 25):
                return True
            elif (board[position + 7] == 25) or (board[position + 7] == 20):
                return True
        elif position_type(position) == "TE":
            if (board[position - 9] == 25):
                return True
            elif (board[position - 7] == 25):
                return True
        elif position_type(position) == "BE":
            if (board[position + 9] == 25) or (board[position + 9] == 20):
                return True
            elif (board[position + 7] == 25) or (board[position + 7] == 20):
                return True
        elif position_type(position) == "CENTER":
            if (board[position + 9] == 25) or (board[position + 9] == 20):
                return True
            elif (board[position + 7] == 25) or (board[position + 7] == 20):
                return True
            elif (board[position - 9] == 25):
                return True
            elif (board[position - 7] == 25):
                return True
    if player == 20:
        # Classify type of position
        if position_type(position) == "BL":
            if (board[position + 9] == 15):
                return True
        elif position_type(position) == "BR":
            if (board[position + 7] == 15):
                return True
        elif position_type(position) == "TL":
            if (board[position - 7] == 15) or (board[position - 7] == 10):
                return True
        elif position_type(position) == "TR":
            if (board[position - 9] == 15) or (board[position - 9] == 10):
                return True
        elif position_type(position) == "LE":
            if (board[position - 7] == 15) or board[position - 7] == 10:
                return True
            elif (board[position + 9] == 15):
                return True
        elif position_type(position) == "RE":
            if (board[position - 9] == 15) or (board[position - 9] == 10):
                return True
            elif (board[position + 7] == 15):
                return True
        elif position_type(position) == "TE":
            if (board[position - 9] == 15) or (board[position - 9] == 10):
                return True
            elif (board[position - 7] == 15) or (board[position - 7] == 10):
                return True
        elif position_type(position) == "BE":
            if (board[position + 9] == 15):
                return True
            elif (board[position + 7] == 15):
                return True
        elif position_type(position) == "CENTER":
            if (board[position + 9] == 15):
                return True
            elif (board[position + 7] == 15):
                return True
            elif (board[position - 9] == 15) or (board[position - 9] == 10):
                return True
            elif (board[position - 7] == 15) or (board[position - 7] == 10):
                return True

def knight(board, position, player):
    candidate = [position + 17, position + 15, position + 6, position - 10, position + 10, position - 6, position - 17,position - 15]
    if player == 10:
        if position_type(position) == "BL":
            if (board[position + 17] == 21) or (board[position + 10] == 21):
                return True
        elif position_type(position) == "BR":
            if (board[position + 6] == 21) or (board[position + 15] == 21):
                return True
        elif position_type(position) == "TL":
            if (board[position - 15] == 21) or (board[position - 6] == 21):
                return True
        elif position_type(position) == "TR":
            if (board[position - 10] == 21) or (board[position - 17] == 21):
                return True
        elif position == 8:
            if (board[position + 17] == 21) or (board[position + 10] == 21) or (board[position - 6] == 21):
                return True
        elif position == 48:
            if (board[position - 15] == 21) or (board[position - 6] == 21) or (board[position + 10] == 21):
                return True
        elif position_type(position) == "LE" and position != 48 and position != 8:
            if (board[position + 17] == 21) or (board[position + 10] == 21) or (board[position - 6] == 21) or (board[position - 15] == 21):
                return True
        elif position == 55:
            if (board[position - 17] == 21) or (board[position - 10] == 21) or (board[position + 6] == 21):
                return True
        elif position == 15:
            if (board[position - 10] == 21) or (board[position + 6] == 21) or (board[position + 15] == 21):
                return True
        elif position_type(position) == "RE" and position != 55 and position != 15:
            if (board[position - 17] == 21) or (board[position - 10] == 21) or (board[position + 6] == 21) or (board[position + 15] == 21):
                return True
        elif position == 62:
            if (board[position - 17] == 21) or (board[position - 15] == 21) or (board[position - 10] == 21):
                return True
        elif position == 57:
            if (board[position - 17] == 21) or (board[position - 15] == 21) or (board[position - 6] == 21):
                return True
        elif position_type(position) == "TE" and position != 57 and position != 62:
            if (board[position - 17] == 21) or (board[position - 15] == 21) or (board[position - 10] == 21) or (board[position - 6] == 21):
                return True
        elif position == 6:
            if (board[position + 17] == 21) or (board[position + 15] == 21) or (board[position + 6] == 21):
                return True
        elif position == 1:
            if (board[position + 17] == 21) or (board[position + 15] == 21) or (board[position + 10] == 21):
                return True
        elif position_type(position) == "BE" and position != 1 and position != 6:
            if (board[position + 15] == 21) or (board[position + 17] == 21) or (board[position + 10] == 21) or (board[position + 6] == 21):
                return True
        elif position_type(position) == "CENTER":
            if position == 9 or position ==  17 or position ==  25 or position ==  33 or position ==  41 or position ==  49:
                candidate.remove(position-10)
                candidate.remove(position+6)
            if position == 49 or position == 50 or position == 51 or position == 52 or position == 53 or position == 54:
                candidate.remove(position+15)
                candidate.remove(position+17)
            if position == 54 or position == 46 or position == 38 or position == 30 or position == 22 or position == 14:
                candidate.remove(position+10)
                candidate.remove(position-6)
            if position == 9 or position == 10 or position == 11 or position == 12 or position == 13 or position == 14:
                candidate.remove(position - 17)
                candidate.remove(position - 15)
            for i in candidate:
                if board[i] == 21:
                    return True
    if player == 20:
        if position_type(position) == "BL":
            if (board[position + 17] == 11) or (board[position + 10] == 11):
                return True
        elif position_type(position) == "BR":
            if (board[position + 6] == 11) or (board[position + 15] == 11):
                return True
        elif position_type(position) == "TL":
            if (board[position - 15] == 11) or (board[position - 6] == 11):
                return True
        elif position_type(position) == "TR":
            if (board[position - 10] == 11) or (board[position - 17] == 11):
                return True
        elif position == 8:
            if (board[position + 17] == 11) or (board[position + 10] == 11) or (board[position - 6] == 11):
                return True
        elif position == 48:
            if (board[position - 15] == 11) or (board[position - 6] == 11) or (board[position + 10] == 11) or (board[position - 15] == 11):
                return True
        elif position_type(position) == "LE" and position != 48 and position != 8:
            if (board[position + 17] == 11) or (board[position + 10] == 11) or (board[position - 6] == 11) or (board[position - 15] == 11):
                return True
        elif position == 55:
            if (board[position - 17] == 11) or (board[position - 10] == 11) or (board[position + 6] == 11):
                return True
        elif position == 15:
            if (board[position - 10] == 11) or (board[position + 6] == 11) or (board[position + 15] == 11):
                return True
        elif position_type(position) == "RE" and position != 55 and position != 15:
            if (board[position - 17] == 11) or (board[position - 10] == 11) or (board[position + 6] == 11) or (board[position + 15] == 11):
                return True
        elif position == 62:
            if (board[position - 17] == 11) or (board[position - 15] == 11) or (board[position - 10] == 11):
                return True
        elif position == 57:
            if (board[position - 17] == 11) or (board[position - 15] == 11) or (board[position - 6] == 11):
                return True
        elif position_type(position) == "TE" and position != 57 and position != 62:
            if (board[position - 17] == 11) or (board[position - 15] == 11) or (board[position - 10] == 11) or (board[position - 6] == 11):
                return True
        elif position == 6:
            if (board[position + 17] == 11) or (board[position + 15] == 11) or (board[position + 6] == 11):
                return True
        elif position == 1:
            if (board[position + 17] == 11) or (board[position + 15] == 11) or (board[position + 10] == 11):
                return True
        elif position_type(position) == "BE" and position != 1 and position != 6:
            if (board[position + 15] == 11) or (board[position + 17] == 11) or (board[position + 10] == 11) or (board[position + 6] == 11):
                return True
        elif position_type(position) == "CENTER":
            if position == 9 or position ==  17 or position ==  25 or position ==  33 or position ==  41 or position ==  49:
                candidate.remove(position-10)
                candidate.remove(position+6)
            if position == 49 or position == 50 or position == 51 or position == 52 or position == 53 or position == 54:
                candidate.remove(position+15)
                candidate.remove(position+17)
            if position == 54 or position == 46 or position == 38 or position == 30 or position == 22 or position == 14:
                candidate.remove(position+10)
                candidate.remove(position-6)
            if position == 9 or position == 10 or position == 11 or position == 12 or position == 13 or position == 14:
                candidate.remove(position - 15)
                candidate.remove(position - 17)
            for i in candidate:
                if board[i] == 11:
                    return True

def IsPositionUnderThreat(board, position, player):
    # Convert board into matrix
    copy = [[board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7]],
            [board[8], board[9], board[10], board[11], board[12], board[13], board[14], board[15]],
            [board[16], board[17], board[18], board[19], board[20], board[21], board[22], board[23]],
            [board[24], board[25], board[26], board[27], board[28], board[29], board[30], board[31]],
            [board[32], board[33], board[34], board[35], board[36], board[37], board[38], board[39]],
            [board[40], board[41], board[42], board[43], board[44], board[45], board[46], board[47]],
            [board[48], board[49], board[50], board[51], board[52], board[53], board[54], board[55]],
            [board[56], board[57], board[58], board[59], board[60], board[61], board[62], board[63]]]
    key = board[position]
    xval = 0
    yval = 0
    rval = [0, 0, 0, 0, 0]
    for i in range(0, len(copy)):
        for j in range(0, len(copy[0])):
            if copy[i][j] == key:
                yval = i
                xval = j
                break

    if player == 10:
        rval[0] = horizontal(copy, xval, yval, 10)
        rval[1] = vertical(copy, xval, yval, 10)
        rval[2] = diagonal_adjacency(board, position, 10)
        rval[3] = diagonal(copy, xval, yval, 10)
        rval[4] = knight(board, position, 10)

    elif player == 20:
        rval[0] = horizontal(copy, xval, yval, 20)
        rval[1] = vertical(copy, xval, yval, 20)
        rval[2] = diagonal_adjacency(board, position, 20)
        rval[3] = diagonal(copy, xval, yval, 20)
        rval[4] = knight(board, position, 20)

    for i in rval:
        if i == True:
            return True
    return False

def update_check(board,pos,move,player):
    update = []
    piece = 0
    update = list(board)
    piece = board[pos]
    update[pos] = 0
    update[move] = piece
    wking = 0
    bking = 0
    state = 0
    if player == 10:
        for i in range(0,64):
            if update[i] == 15:
                wking = i
                break
        state = IsPositionUnderThreat(update,wking,10)
    if player == 20:
        for i in range(0,64):
            if update[i] == 25:
                bking = i
                break
        state = IsPositionUnderThreat(update, bking, 20)
    if state == True:
        return True
    else:
        return False

def get_row(position):
    if position >= 56 and position <= 63:
        return list(range(56,64))
    if position >= 48 and position <= 55:
        return list(range(48,56))
    if position >= 40 and position <= 47:
        return list(range(40,48))
    if position >= 32 and position <= 39:
        return list(range(32, 40))
    if position >= 24 and position <= 31:
        return list(range(24, 32))
    if position >= 16 and position <= 23:
        return list(range(16, 24))
    if position >= 8 and position <= 15:
        return list(range(8, 16))
    if position >= 0 and position <= 7:
        return list(range(0, 8))

# Move helper functions
def mpawn(board,position,player):
    accum = []
    candidate_listw = [position+7,position+9]
    candidate_listb = [position-7,position-9]
    if player == 10:
        if board[position+8] == 0 and update_check(board,position,position+8,10) == False:
            accum = accum + [position+8]
        for i in candidate_listw:
            if (board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24) and update_check(board,position,i,10) == False:
                accum = accum + [i]
    if player == 20:
        if board[position - 8] == 0 and update_check(board, position, position - 8, 10) == False:
            accum = accum + [position - 8]
        for i in candidate_listb:
            if (board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14) and update_check(board,position,i,20) == False:
                accum = accum + [i]
    return accum

def mrook(board,position,player):
    accum = []
    candidatecol = []
    candidaterow = []
    indexwrow = 0
    indexwcol = 0
    if player == 10:
        # Find all possible moves
        # Horizontal and vertical
        for i in range(position-8,-1,-8):
            candidatecol.append(i)

        for i in range(position,64,8):
            candidatecol.append(i)

        candidaterow = list(get_row(position))


        # Check for valid moves
        for i in range(0,len(candidatecol)):
            if candidatecol[i] == position:
                indexwcol = i
                break
        for i in range (0, len(candidaterow)):
            if candidaterow[i] == position:
                indexwrow = i
                break

        for i in range(indexwrow-1,-1,-1):
            if update_check(board,position,candidaterow[i],10) == False:
                if getinfo(board,candidaterow[i],10) == "blank":
                    accum.append(candidaterow[i])
                elif getinfo(board,candidaterow[i],10) == "black":
                    accum.append(candidaterow[i])
                    break
                else:
                    break

        for i in range(indexwrow+1,len(candidaterow)):
            if update_check(board, position, candidaterow[i], 10) == False:
                if getinfo(board, candidaterow[i], 10) == "blank":
                    accum.append(candidaterow[i])
                elif getinfo(board, candidaterow[i], 10) == "black":
                    accum.append(candidaterow[i])
                    break
                else:
                    break

        for i in range(0,indexwcol,1):
            if update_check(board,position,candidatecol[i],10) == False:
                if getinfo(board,candidatecol[i],10) == "blank":
                    accum.append(candidatecol[i])

                elif getinfo(board,candidatecol[i],10) == "black":
                    accum.append(candidatecol[i])
                    break
                else:
                    break

        for i in range(indexwcol+1,len(candidatecol)):
            if update_check(board,position,candidatecol[i],10) == False:
                if getinfo(board,candidatecol[i],10) == "blank":
                    accum.append(candidatecol[i])
                elif getinfo(board,candidatecol[i],10) == "black":
                    accum.append(candidatecol[i])
                    break
                else:
                    break

    if player == 20:

        # Find all possible moves
        # Horizontal and vertical
        for i in range(position - 8, -1, -8):
            candidatecol.append(i)

        for i in range(position, 64, 8):
            candidatecol.append(i)

        candidaterow = list(get_row(position))

        # Check for valid moves
        for i in range(0, len(candidatecol)):
            if candidatecol[i] == position:
                indexwcol = i
                break
        for i in range(0, len(candidaterow)):
            if candidaterow[i] == position:
                indexwrow = i
                break


        for i in range(indexwrow - 1, -1, -1):
            if update_check(board, position, candidaterow[i], 20) == False:
                if getinfo(board, candidaterow[i], 20) == "blank":

                    accum.append(candidaterow[i])
                elif getinfo(board, candidaterow[i], 20) == "white":
                    accum.append(candidaterow[i])
                    break
                else:
                    break

        for i in range(indexwrow + 1, len(candidaterow)):
            if update_check(board, position, candidaterow[i], 20) == False:
                if getinfo(board, candidaterow[i], 20) == "blank":
                    accum.append(candidaterow[i])
                elif getinfo(board, candidaterow[i], 20) == "white":
                    accum.append(candidaterow[i])
                    break
                else:
                    break

        for i in range(0, indexwcol, 1):
            if update_check(board, position, candidatecol[i], 20) == False:
                if getinfo(board, candidatecol[i], 20) == "blank":
                    accum.append(candidatecol[i])

                elif getinfo(board, candidatecol[i], 20) == "white":
                    accum.append(candidatecol[i])
                    break
                else:
                    break
        for i in range(indexwcol + 1, len(candidatecol)):
            if update_check(board, position, candidatecol[i], 20) == False:
                if getinfo(board, candidatecol[i], 20) == "blank":
                    accum.append(candidatecol[i])
                elif getinfo(board, candidatecol[i], 20) == "white":
                    accum.append(candidatecol[i])
                    break
                else:
                    break
    return accum

def mking(board,position,player):
    candidate_movesk = [position+7,position+8,position+9,position+1,position-7,position-8,position-9,position-1]
    accum = []
    if player == 10:
        if position_type(position) == "LE":
            candidate_movesk = [position + 8, position + 9, position + 1, position - 7, position - 8]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "RE":
            candidate_movesk = [position + 7, position + 8, position - 8,position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TE":
            candidate_movesk = [position + 1, position - 7, position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "BE":
            candidate_movesk = [position + 7, position + 8, position + 9, position + 1, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TR":
            candidate_movesk = [position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass
        if position_type(position) == "BR":
            candidate_movesk = [position + 7, position + 8, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TL":
            candidate_movesk = [position + 1, position - 7, position - 8]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "BL":
            candidate_movesk = [position + 8, position + 9, position + 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "CENTER":
            candidate_movesk = [position + 7, position + 8, position + 9, position + 1, position - 7, position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 10)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 20 or board[i] == 21 or board[i] == 22 or board[i] == 23 or board[i] == 24 or \
                            board[i] == 25:
                        accum.append(i)
                    else:
                        pass

    if player == 20:
        if position_type(position) == "LE":
            candidate_movesk = [position + 8, position + 9, position + 1, position - 7, position - 8]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass
        if position_type(position) == "RE":
            candidate_movesk = [position + 7, position + 8, position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TE":
            candidate_movesk = [position + 1, position - 7, position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "BE":
            candidate_movesk = [position + 7, position + 8, position + 9, position + 1, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TR":
            candidate_movesk = [position - 8, position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "BR":
            candidate_movesk = [position + 7, position + 8, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "TL":
            candidate_movesk = [position + 1, position - 7, position - 8]
            for i in candidate_movesk:
                state = update_check(board,position,i,20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or board[i] == 15:
                        accum.append(i)
                    else:
                        pass

        if position_type(position) == "BL":
            candidate_movesk = [position + 8, position + 9, position + 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass
        if position_type(position) == "CENTER":
            candidate_movesk = [position + 7, position + 8, position + 9, position + 1, position - 7, position - 8,
                                position - 9, position - 1]
            for i in candidate_movesk:
                state = update_check(board, position, i, 20)
                if state == False:
                    if board[i] == 0:
                        accum.append(i)
                    elif board[i] == 10 or board[i] == 11 or board[i] == 12 or board[i] == 13 or board[i] == 14 or \
                            board[i] == 15:
                        accum.append(i)
                    else:
                        pass
    return accum

def mknight(board, position, player):
    accum = []
    candidate = [position+17,position+15,position+6,position-10,position+10,position-6,position-17,position-15]
    if player == 10:
        if position_type(position) == "BL":
            candidate.remove(position+15)
            candidate.remove(position + 6)
            candidate.remove(position -10)
            candidate.remove(position - 17)
            candidate.remove(position -15)
            candidate.remove(position -6)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "BR":
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            candidate.remove(position + 10)
            candidate.remove(position + 17)
            candidate.remove(position - 15)
            candidate.remove(position - 6)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "TL":
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "TR":
            candidate.remove(position + 10)
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 8:
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position -17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)


        elif position == 48:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "LE" and position != 48 and position != 8:
            candidate.remove(position+15)
            candidate.remove(position+6)
            candidate.remove(position-10)
            candidate.remove(position-17)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 55:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position + 15)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 15:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "RE" and position != 55 and position != 15:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)


        elif position == 62:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 57:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position + 10)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "TE" and position != 57 and position != 62:
            candidate.remove(position + 15)
            candidate.remove(position + 17)
            candidate.remove(position + 6)
            candidate.remove(position + 10)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 6:
            candidate.remove(position - 10)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position == 1:
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 6)
            candidate.remove(position - 17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board, position, i, 10) == False:
                    if (getinfo(board, i, 10) == "blank" or getinfo(board, i, 10) == "black"):
                        accum.append(i)

        elif position_type(position) == "BE" and position != 1 and position != 6:
            candidate.remove(position - 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)

        elif position_type(position) == "CENTER":
            if position == 9 or position == 17 or position == 25 or position == 33 or position == 41 or position == 49:
                candidate.remove(position - 10)
                candidate.remove(position + 6)
            if position == 49 or position == 50 or position == 51 or position == 52 or position == 53 or position == 54:
                candidate.remove(position + 15)
                candidate.remove(position + 17)
            if position == 54 or position == 46 or position == 38 or position == 30 or position == 22 or position == 14:
                candidate.remove(position + 10)
                candidate.remove(position - 6)
            if position == 9 or position == 10 or position == 11 or position == 12 or position == 13 or position == 14:
                candidate.remove(position - 15)
                candidate.remove(position - 7)
            for i in candidate:
                if update_check(board,position,i,10) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "black"):
                        accum.append(i)
    if player == 20:
        if position_type(position) == "BL":
            candidate.remove(position+15)
            candidate.remove(position + 6)
            candidate.remove(position -10)
            candidate.remove(position - 17)
            candidate.remove(position -15)
            candidate.remove(position -6)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "BR":
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            candidate.remove(position + 10)
            candidate.remove(position + 17)
            candidate.remove(position - 15)
            candidate.remove(position - 6)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "TL":
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)


        elif position_type(position) == "TR":
            candidate.remove(position + 10)
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 8:
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position -17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)


        elif position == 48:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "LE" and position != 48 and position != 8 and position != 48:
            candidate.remove(position+15)
            candidate.remove(position+6)
            candidate.remove(position-10)
            candidate.remove(position-17)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 55:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position + 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 15:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "RE" and position != 55 and position != 15:
            candidate.remove(position + 17)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)


        elif position == 62:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 57:
            candidate.remove(position + 17)
            candidate.remove(position + 15)
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position + 10)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "TE" and position != 57 and position != 62:
            candidate.remove(position + 15)
            candidate.remove(position + 17)
            candidate.remove(position + 6)
            candidate.remove(position + 10)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 6:
            candidate.remove(position - 10)
            candidate.remove(position + 10)
            candidate.remove(position - 6)
            candidate.remove(position - 17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position == 1:
            candidate.remove(position + 6)
            candidate.remove(position - 10)
            candidate.remove(position - 6)
            candidate.remove(position - 17)
            candidate.remove(position - 15)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "BE" and position != 1 and position != 6:
            candidate.remove(position - 10)
            candidate.remove(position - 6)
            candidate.remove(position - 15)
            candidate.remove(position - 17)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

        elif position_type(position) == "CENTER":
            if position == 9 or position == 17 or position == 25 or position == 33 or position == 41 or position == 49:
                candidate.remove(position - 10)
                candidate.remove(position + 6)
            if position == 49 or position == 50 or position == 51 or position == 52 or position == 53 or position == 54:
                candidate.remove(position + 15)
                candidate.remove(position + 17)
            if position == 54 or position == 46 or position == 38 or position == 30 or position == 22 or position == 14:
                candidate.remove(position + 10)
                candidate.remove(position - 6)
            if position == 9 or position == 10 or position == 11 or position == 12 or position == 13 or position == 14:
                candidate.remove(position - 15)
                candidate.remove(position - 6)
            for i in candidate:
                if update_check(board,position,i,20) == False:
                    if (getinfo(board,i,10) == "blank" or getinfo(board,i,10) == "white"):
                        accum.append(i)

    return accum

def get_y(position):
    if position in [0,1,2,3,4,5,6,7]:
        return 0
    if position in [8,9,10,11,12,13,14,15]:
        return 1
    if position in [16,17,18,19,20,21,22,23]:
        return 2
    if position in [24,25,26,27,28,29,30,31]:
        return 3
    if position in [32,33,34,35,36,37,38,39]:
        return 4
    if position in [40,41,42,43,44,45,46,47]:
        return 5
    if position in [48,49,50,51,52,53,54,55]:
        return 6
    if position in [56,57,58,59,60,61,62,63]:
        return 7
def get_x(position):
    if position in [0,8,16,24,32,40,48,56]:
        return 0
    if position in [1,9,17,25,33,41,49,57]:
        return 1
    if position in [2,10,18,26,34,42,50,58]:
        return 2
    if position in [3,11,19,27,35,43,51,59]:
        return 3
    if position in [4,12,20,28,36,44,52,60]:
        return 4
    if position in [5,13,21,29,37,45,53,61]:
        return 5
    if position in [6,14,22,30,38,46,54,62]:
        return 6
    if position in [7,15,23,31,47,55,63]:
        return 7

def mbishop(board,position,player):
    # Convert to x-y coordinates
    accum = []
    copy = [[board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7]],
            [board[8], board[9], board[10], board[11], board[12], board[13], board[14], board[15]],
            [board[16], board[17], board[18], board[19], board[20], board[21], board[22], board[23]],
            [board[24], board[25], board[26], board[27], board[28], board[29], board[30], board[31]],
            [board[32], board[33], board[34], board[35], board[36], board[37], board[38], board[39]],
            [board[40], board[41], board[42], board[43], board[44], board[45], board[46], board[47]],
            [board[48], board[49], board[50], board[51], board[52], board[53], board[54], board[55]],
            [board[56], board[57], board[58], board[59], board[60], board[61], board[62], board[63]]]

    if player == 10:
        xvar = get_x(position)
        yvar = get_y(position)
        while (xvar <= 7) and (yvar <= 7):
            xvar = xvar + 1
            yvar = yvar + 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if (board[yvar * 8 + xvar] == 0) and update_check(board, position, yvar * 8 + xvar, 10) == False:
                accum.append(yvar * 8 + xvar)
            elif getinfo(board, yvar * 8 + xvar, 10) == "black" and update_check(board, position, yvar * 8 + xvar,
                                                                                 10) == False:
                accum.append(yvar * 8 + xvar)
                break
            else:
                break

        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar >= 0) and (yvar >= 0):
            xvar = xvar - 1
            yvar = yvar - 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if (board[yvar * 8 + xvar] == 0) and update_check(board, position, yvar * 8 + xvar, 10) == False:
                accum.append(yvar * 8 + xvar)
            elif getinfo(board, yvar * 8 + xvar, 10) == "black" and update_check(board, position, yvar * 8 + xvar,10) == False:
                accum.append(yvar * 8 + xvar)
                break
            else:
                break

        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar >= 0) and (yvar <= 7):
            xvar = xvar - 1
            yvar = yvar + 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if (board[yvar * 8 + xvar] == 0) and update_check(board, position, yvar * 8 + xvar, 10) == False:
                accum.append(yvar * 8 + xvar)
            elif getinfo(board, yvar * 8 + xvar, 10) == "black" and update_check(board, position, yvar * 8 + xvar,
                                                                                 10) == False:
                accum.append(yvar * 8 + xvar)
                break
            else:
                break

        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar <= 7) and (yvar >= 0):
            xvar = xvar + 1
            yvar = yvar - 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if (board[yvar * 8 + xvar] == 0) and update_check(board, position, yvar * 8 + xvar, 10) == False:
                accum.append(yvar * 8 + xvar)
            elif getinfo(board, yvar * 8 + xvar, 10) == "black" and update_check(board, position, yvar * 8 + xvar,
                                                                                 10) == False:
                accum.append(yvar * 8 + xvar)
                break
            else:
                break

    if player == 20:
        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar <= 7) and (yvar <= 7):
            xvar = xvar + 1
            yvar = yvar + 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if update_check(board, position, yvar * 8 + xvar, 20) == False:
                if (board[yvar * 8 + xvar] == 0):
                    accum.append(yvar * 8 + xvar)
                elif getinfo(board, yvar * 8 + xvar, 20) == "white":
                    accum.append(yvar * 8 + xvar)
                    break
                else:
                    break

        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar >= 0) and (yvar >= 0):
            xvar = xvar - 1
            yvar = yvar - 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if update_check(board, position, yvar * 8 + xvar, 20) == False:
                if (board[yvar * 8 + xvar] == 0):
                    accum.append(yvar * 8 + xvar)
                elif getinfo(board, yvar * 8 + xvar, 20) == "white":
                    accum.append(yvar * 8 + xvar)
                    break
                else:
                    break

        xvar = get_x(position)
        yvar = get_y(position)


        while (xvar >= 0) and (yvar <= 7):
            xvar = xvar - 1
            yvar = yvar + 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if update_check(board, position, yvar * 8 + xvar, 20) == False:
                if (board[yvar * 8 + xvar] == 0):
                    accum.append(yvar * 8 + xvar)
                elif getinfo(board, yvar * 8 + xvar, 20) == "white":
                    accum.append(yvar * 8 + xvar)
                    break
                else:
                    break

        xvar = get_x(position)
        yvar = get_y(position)

        while (xvar <= 7) and (yvar >= 0):
            xvar = xvar + 1
            yvar = yvar - 1
            if xvar < 0 or yvar < 0 or xvar > 7 or yvar > 7:
                break
            if update_check(board, position, yvar * 8 + xvar, 20) == False:
                if (board[yvar * 8 + xvar] == 0):
                    accum.append(yvar * 8 + xvar)
                elif getinfo(board, yvar * 8 + xvar, 20) == "white":
                    accum.append(yvar * 8 + xvar)
                    break
                else:
                    break

    return accum


def mqueen(board, position, player):
    bishop = []
    queen = []
    rook = []
    if player == 10:
        bishop = mbishop(board,position,10)
        rook = mrook(board,position,10)
        queen = bishop + rook
    if player == 20:
        bishop = mbishop(board, position, 20)
        rook = mrook(board, position, 20)
        queen = bishop + rook
    return queen

def GetPieceLegalMoves(board, position):
    if board[position] == 10:
        return mpawn(board,position,10)
    if board[position] == 11:
        return mknight(board, position, 10)
    if board[position] == 12:
        return mbishop(board, position, 10)
    if board[position] == 13:
        return mrook(board, position, 10)
    if board[position] == 14:
        return mqueen(board, position, 10)
    if board[position] == 15:
        return mking(board, position, 10)

    if board[position] == 20:
        return mpawn(board, position, 20)
    if board[position] == 21:
        return mknight(board, position, 20)
    if board[position] == 22:
        return mbishop(board, position, 20)
    if board[position] == 23:
        return mrook(board, position, 20)
    if board[position] == 24:
        return mqueen(board, position, 20)
    if board[position] == 25:
        return mking(board, position, 20)

def threatupdate(board,pos,move,player):
    update = []
    piece = 0
    update = list(board)
    piece = board[pos]
    update[pos] = 0
    update[move] = piece
    state = 0
    if player == 10:
        state = IsPositionUnderThreat(update,move,10)
    if player == 20:
        state = IsPositionUnderThreat(update,move,20)
    if state == True:
        return True
    else:
        return False

def value(piece):
    # relative values
    if piece == 10 or 20:
        return 1.0
    if piece == 11 or 21:
        return 3.0
    if piece == 12 or 22:
        return 3.0
    if piece == 13 or 23:
        return 5.0
    if piece == 14 or 24:
        return 10.0
    if piece == 15 or 25:
        return 2.0

def valuepiece(piece):
    # relative values
    if piece == 10 or 20:
        return 1.0
    if piece == 11 or 21:
        return 3.0
    if piece == 12 or 22:
        return 3.0
    if piece == 13 or 23:
        return 5.0
    if piece == 14 or 24:
        return 10.0
    if piece == 15 or 25:
        return 2.0

def moveincrement():
    global movecounter
    movecounter = movecounter + 1
    return movecounter

def evaluate(board,position,move,player):
    # If checks king and doesn't put you in harm, return 4.0
    if player == 10:
        if (update_check(board,position,move,20) == True) and (threatupdate(board,position,move,player) == False):
            return 4.0
            # Taking a piece computation: enemypieceval - 0 (if no threat) - mypieceval (if threat)
        else:
            if (getinfo(board,board[move],player) == "black") and (threatupdate(board,position,move,player) == False):
                return 2*value(board[move])

            elif (getinfo(board,board[move],player) == "black") and (threatupdate(board,position,move,player) == True):
                return 2*value(board[move]) - value(board[position])
            else:
                # A development piece or no threat piece
                # Development of knight in opening position
                # Development of bishop in opening position
                # Development of queen in opening position
                if (position == 2 or position == 3 or position == 5) and (board[position] == 14 or board[position] == 12):
                    return 10.0
                elif (position == 1 or position == 6) and (board[position] == 11):
                    return 7.0
                elif (position == 8 or position == 9 or position == 10 or position == 11 or position == 12 or position == 13 or position == 14 or position == 15) and (board[move] == 0):
                    return 5.0
                else:
                    return float(randint(0,10))

    if player == 20:
        if (update_check(board, position, move, 10) == True) and (threatupdate(board, position, move, player) == False):
            return 4.0
            # Taking a piece computation: enemypieceval - 0 (if no threat) - mypieceval (if threat)
        else:
            if (board[move] == 20 or board[move] == 21 or board[move] == 22 or board[move] == 23 or board[move] == 24) and (threatupdate(board, position, move, player) == False):
                return 2*value(board[move])

            elif (board[move] == 20 or board[move] == 21 or board[move] == 22 or board[move] == 23 or board[move] == 24) and (threatupdate(board, position, move, player) == True):
                return 2*value(board[move]) - value(board[position])
            else:
                if (position == 58 or position == 59 or position == 61) and (board[position] == 24 or board[position] == 22):
                    return 10.0
                elif (position == 57 or position == 62) and (board[position] == 21):
                    return 7.0
                elif (position == 48 or position == 49 or position == 50 or position == 51 or position == 52 or position == 53 or position == 54 or position == 55) and (board[move] == 0):
                    return 5.0
                else:
                    return float(randint(0, 10))
# Eval tree class for decision making
class evalTree:
    def __init__(self,x):
        self.store = [x,[]]
    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True
    def depth(self,input,level):
        print ' ' * level * 3,  input[0]
        for subtree in input[1]:
                self.depth(subtree.store,level+1)
    def Print_DepthFirst(self):
        return self.depth(self.store,0)
    def levelOrder(self,input,list):
        Q = []
        Q.insert(0,input)
        while ((Q == []) == False):
                node = Q.pop()
                list = list + [node[0]]
                for i in node[1]:
                        Q.insert(0,i.store)
        return list
    def Get_LevelOrder(self):
        a = []
        return self.levelOrder(self.store,a)

def candidategeneration(board,player):
    candidatemoves = []
    pos = GetPlayerPositions(board, player)
    # Generate all moves for each piece
    for i in pos:
        moves = GetPieceLegalMoves(board, i)
        for j in moves:
            candidatemoves.append([[i, j], evaluate(board, i, j, player)])
    return candidatemoves

def board_update(board,position,move):
    image = list(board)
    piece = board[position]
    image[position] = 0
    image[move] = piece
    return image

def get_tree(board,player):
    out = []
    candidatemoves = []
    enemymoves = []
    # while True:
    #     try:
    if player == 10:
        pos = GetPlayerPositions(board, 10)
        # Generate all moves for each piece
        for i in pos:
            moves = GetPieceLegalMoves(board, i)
            for j in moves:
                candidatemoves.append([[i, j], evaluate(board, i, j, 10)])
        # Tree with root of [[0,0],0]
        evaltree = evalTree([[0, 0], 0])
        # Build first layer
        for i in candidatemoves:
            successor = evalTree(i)
            evaltree.AddSuccessor(successor)
        levelorder = evaltree.Get_LevelOrder()

        # # Build second layer
        for tree in evaltree.store[1]:
            new = board_update(board, tree.store[0][0][0], tree.store[0][0][1])
            enemymoves = candidategeneration(new, 20)
            for i in enemymoves:
                successor = evalTree(i)
                tree.AddSuccessor(successor)
                # for subtree in tree.store[1]:
                #     new2 = board_update(new,subtree.store[0][0][0],tree.store[0][0][1])
                #     candidatemoves2 = candidategeneration(new2,10)
                #     for j in candidatemoves2:
                #         successor2 = evalTree(j)
                #         subtree.AddSuccessor(successor2)
        mytree = evaltree.Get_LevelOrder()
        return mytree
    if player == 20:
        pos = GetPlayerPositions(board, 20)
        # Generate all moves for each piece
        for i in pos:
            moves = GetPieceLegalMoves(board, i)
            for j in moves:
                candidatemoves.append([[i, j], evaluate(board, i, j, 20)])
        # Tree with root of [[0,0],0]
        evaltree = evalTree([[0, 0], 0])
        # Build first layer
        for i in candidatemoves:
            successor = evalTree(i)
            evaltree.AddSuccessor(successor)
        levelorder = evaltree.Get_LevelOrder()

        # # Build second layer
        for tree in evaltree.store[1]:
            new = board_update(board, tree.store[0][0][0], tree.store[0][0][1])
            enemymoves = candidategeneration(new, 10)
            for i in enemymoves:
                successor = evalTree(i)
                tree.AddSuccessor(successor)
                # for subtree in tree.store[1]:
                #     new2 = board_update(new,subtree.store[0][0][0],tree.store[0][0][1])
                #     candidatemoves2 = candidategeneration(new2,10)
                #     for j in candidatemoves2:
                #         successor2 = evalTree(j)
                #         subtree.AddSuccessor(successor2)
        mytree = evaltree.Get_LevelOrder()
        return mytree

        # except Exception as e:
        #         return None

def tree_output(board,player):
    out = []
    candidatemoves = []
    enemymoves = []
    while True:
        try:

            if player == 10:
                pos = GetPlayerPositions(board, 10)
                # Generate all moves for each piece
                for i in pos:
                    moves = GetPieceLegalMoves(board, i)
                    for j in moves:
                        candidatemoves.append([[i, j], evaluate(board, i, j, 10)])
                # Tree with root of [[0,0],0]
                evaltree = evalTree([[0, 0], 0])
                # Build first layer
                for i in candidatemoves:
                    successor = evalTree(i)
                    evaltree.AddSuccessor(successor)
                levelorder = evaltree.Get_LevelOrder()
                # # Build second layer
                for tree in evaltree.store[1]:
                    new = board_update(board, tree.store[0][0][0], tree.store[0][0][1])
                    enemymoves = candidategeneration(new, 20)
                    for i in enemymoves:
                        successor = evalTree(i)
                        tree.AddSuccessor(successor)
                return evaltree

            if player == 20:
                pos = GetPlayerPositions(board, 20)
                # Generate all moves for each piece
                for i in pos:
                    moves = GetPieceLegalMoves(board, i)
                    for j in moves:
                        candidatemoves.append([[i, j], evaluate(board, i, j, 20)])
                # Tree with root of [[0,0],0]
                evaltree = evalTree([[0, 0], 0])
                # Build first layer
                for i in candidatemoves:
                    successor = evalTree(i)
                    evaltree.AddSuccessor(successor)
                levelorder = evaltree.Get_LevelOrder()
                # # Build second layer
                for tree in evaltree.store[1]:
                    new = board_update(board, tree.store[0][0][0], tree.store[0][0][1])
                    enemymoves = candidategeneration(new, 10)
                    for i in enemymoves:
                        successor = evalTree(i)
                        tree.AddSuccessor(successor)
                return evaltree

        except Exception as e:
            return None

def chessPlayer(board,player):
    rval = [0,0,0,0]
    good = []
    comparison = []
    exchange = []
    exchange_accum = []
    major_accumulator = []
    minor_accumulator = []
    comparison_set = []
    outtree = []
    index = 0
    valuetarget = 0
    valueme = 0
    # while True:
    #     try:
            # GENERATE THE OUTPUT
            # build the candidate move set
            #evaluate all candidate moves
    if player == 10:
        rval[0] = True
        rval[2] = candidategeneration(board, player)
        outtree = get_tree(board, player)
        rval[3] = outtree
        candidate = candidategeneration(board,player)
        for i in candidate:
            if getinfo(board,i[0][1],10) == "black":
                if IsPositionUnderThreat(board,i[0][1],20) == True:
                    valuetarget = valuepiece(board[i[0][1]])
                    valueme = valuepiece(board[i[0][1]])
                    if valuetarget >= valueme and threatupdate(board,i[0][0],i[0][1],player) == False:
                        exchange.append(i)
                    elif valuetarget < valueme and abs(valueme-valuetarget) <= 2.0:
                        exchange.append(i)

        if len(exchange) != 0:
            for i in exchange:
                exchange_accum.append(valuepiece(i[0][1])-valuepiece(i[0][0]))
            index, value = max(enumerate(exchange_accum),key=operator.itemgetter(1))
            rval[1] = exchange[index][0]
            return rval
        a = tree_output(board, player)

        for tree in a.store[1]:
            # reset minor_accumulator
            minor_accumulator = []
            for subtree in tree.store[1]:
                minor_accumulator.append(subtree.store[0][1])
            length= len(minor_accumulator)
            if length != 0:
                major_accumulator.append(sum(minor_accumulator) / length)
            else:
                major_accumulator.append(0)
        a = candidategeneration(board, player)
        for i in a:
            comparison.append(i[1])
        comparison_set = list(comparison)
        for i in range(0, len(comparison)):
            comparison_set[i] = comparison[i] - major_accumulator[i]
        for i in comparison_set:
            if i > 0.5:
                good.append(i)
        if len(good) != 0:
            index, value = max(enumerate(comparison_set), key=operator.itemgetter(1))
            rval[1] = [a[index][0][0], a[index][0][1]]
        if len(good) == 0:
            random = randint(0,len(a))
            rval[1] = [a[0][0][0], a[0][0][1]]
        return rval


    elif player == 20:
        rval[0] = True
        rval[2] = candidategeneration(board,player)
        outtree = get_tree(board, player)
        rval[3] = outtree
        candidate = candidategeneration(board, player)
        for i in candidate:
            if getinfo(board,i[0][1],20) == "white":
                if IsPositionUnderThreat(board,i[0][1],10) == True:
                    valuetarget = valuepiece(board[i[0][1]])
                    valueme = valuepiece(board[i[0][1]])
                    if valuetarget >= valueme and threatupdate(board,i[0][0],i[0][1],player) == False:
                        exchange.append(i)
                    elif valuetarget < valueme and abs(valueme-valuetarget) <= 2.0:
                        exchange.append(i)
        for i in exchange:
            exchange_accum.append(valuepiece(i[0][1]) - valuepiece(i[0][0]))
            index, value = max(enumerate(exchange_accum), key=operator.itemgetter(1))
            rval[1] = exchange[index][0]
            return rval

        a = tree_output(board, player)

        for tree in a.store[1]:
            # reset minor_accumulator
            minor_accumulator = []
            for subtree in tree.store[1]:
                minor_accumulator.append(subtree.store[0][1])
            length= len(minor_accumulator)
            if length != 0:
                major_accumulator.append(sum(minor_accumulator) / length)
            else:
                major_accumulator.append(0)
        a = candidategeneration(board, player)
        for i in a:
            comparison.append(i[1])
        comparison_set = list(comparison)
        for i in range(0, len(comparison)):
            comparison_set[i] = comparison[i] - major_accumulator[i]
        for i in comparison_set:
            if i > 0.5:
                good.append(i)
        if len(good) != 0:
            index, value = max(enumerate(comparison_set), key=operator.itemgetter(1))
            rval[1] = [a[index][0][0], a[index][0][1]]
        if len(good) == 0:
            random = randint(0,len(a))
            rval[1] = [a[0][0][0], a[0][0][1]]
        return rval

        # except Exception as e:
        #     return [False, [0, 0], [[[0, 0], 0]], None]



def main():
    test_board1 = list(init_board())
    image = list(init_image())
    piece = 0
    for i in range(0,50):
        a = chessPlayer(test_board1,10)
        beforea = a[1][0]
        aftera = a[1][1]
        piece = test_board1[beforea]
        test_board1[beforea] = 0
        test_board1[aftera] = piece
        PrintBoard(test_board1,image)
        print '                    '
        print '                    '
        print '                    '
        b = chessPlayer(test_board1,20)
        beforeb = b[1][0]
        afterb = b[1][1]
        piece = test_board1[beforeb]
        test_board1[beforeb] = 0
        test_board1[afterb] = piece
        PrintBoard(test_board1, image)
        print '                    '
        print '                    '
        print '                    '

main()