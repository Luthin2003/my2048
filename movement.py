from main import Tile

def LEFT_MOVEMENT(tiles , ROWS , COLS):
    ismove = False



    for i in range(ROWS):
        j_ = 0
        for j in range(1 , COLS):
            if tiles[i][j].value == 0:
                continue

            

            if tiles[i][j_].value == 0:
                tiles[i][j_] = Tile(tiles[i][j].value , i , j_)
                tiles[i][j] = Tile(0 , i , j)
                ismove = True

            elif tiles[i][j_].value != 0 and tiles[i][j].value == tiles[i][j_].value :
                tiles[i][j_] = Tile(2*tiles[i][j].value , i , j_)
                tiles[i][j] = Tile(0 , i , j)
                j_+=1
                ismove = True

            elif tiles[i][j_].value != 0 and tiles[i][j].value != tiles[i][j_].value :
                
                tiles[i][j_+1] = Tile(tiles[i][j].value , i , j_+1)
                if j_+1 != j : 
                    tiles[i][j] = Tile(0 , i , j)
                    ismove = True
                j_+=1

    return ismove

def RIGHT_MOVEMENT(tiles , ROWS , COLS):

    ismove = False

    for i in range(ROWS):
        j_ = COLS - 1
        for j in range(COLS - 2, -1, -1):
            if tiles[i][j].value == 0:
                continue


            if tiles[i][j_].value == 0:
                tiles[i][j_] = Tile(tiles[i][j].value , i , j_)
                tiles[i][j] = Tile(0 , i , j)
                ismove = True

            elif tiles[i][j_].value != 0 and tiles[i][j].value == tiles[i][j_].value :
                tiles[i][j_] = Tile(2*tiles[i][j].value , i , j_)
                tiles[i][j] = Tile(0 , i , j)
                j_-=1
                ismove = True

            elif tiles[i][j_].value != 0 and tiles[i][j].value != tiles[i][j_].value :
                tiles[i][j_-1] = Tile(tiles[i][j].value , i , j_-1)
                if j_-1 != j : 
                    tiles[i][j] = Tile(0 , i , j)
                    ismove = True
                j_-=1

    return ismove


def UP_MOVEMENT(tiles , ROWS , COLS):

    ismove = False

    for j in range(COLS):
        i_ = 0
        for i in range(1 , ROWS):
            if tiles[i][j].value == 0:
                continue


            if tiles[i_][j].value == 0:
                tiles[i_][j] = Tile(tiles[i][j].value , i_ , j)
                tiles[i][j] = Tile(0 , i , j)
                ismove = True

            elif tiles[i_][j].value != 0 and tiles[i][j].value == tiles[i_][j].value :
                tiles[i_][j] = Tile(2*tiles[i][j].value , i_ , j)
                tiles[i][j] = Tile(0 , i , j)
                i_+=1
                ismove = True

            elif tiles[i_][j].value != 0 and tiles[i][j].value != tiles[i_][j].value :
                tiles[i_+1][j] = Tile(tiles[i][j].value , i_+1 , j)
                if i_+1 != i : 
                    tiles[i][j] = Tile(0 , i , j)
                    ismove = True
                i_+=1

    return ismove

def DOWN_MOVEMENT(tiles , ROWS , COLS):

    ismove = False

    for j in range(COLS):
        i_ = ROWS-1
        for i in range(ROWS-2 , -1 , -1):
            if tiles[i][j].value == 0:
                continue


            if tiles[i_][j].value == 0:
                tiles[i_][j] = Tile(tiles[i][j].value , i_ , j)
                tiles[i][j] = Tile(0 , i , j)
                ismove = True

            elif tiles[i_][j].value != 0 and tiles[i][j].value == tiles[i_][j].value :
                tiles[i_][j] = Tile(2*tiles[i][j].value , i_ , j)
                tiles[i][j] = Tile(0 , i , j)
                i_-=1
                ismove = True

            elif tiles[i_][j].value != 0 and tiles[i][j].value != tiles[i_][j].value :
                tiles[i_-1][j] = Tile(tiles[i][j].value , i_-1 , j)
                if i_-1 != i : 
                    tiles[i][j] = Tile(0 , i , j)
                    ismove = True
                i_-=1

    return ismove
