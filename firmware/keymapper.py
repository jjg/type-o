def get_map():

    # init keymap
    row_count = 4
    col_count = 12
    keymap = [[0 for x in range(col_count)] for y in range(row_count)]

    # map keys to characters ([row][column])
    # TODO: this can probaby be done with a literal, and
    # ideally would use some standard config file format
    # TODO: If the value were a tuple, we could define 
    # the modified values (uppercase, etc.) as well

    # row 1
    keymap[0][0] = "?"
    keymap[0][1] = "q"
    keymap[0][2] = "w"
    keymap[0][3] = "e"
    keymap[0][4] = "r"
    keymap[0][5] = "t"
    keymap[0][6] = "y"
    keymap[0][7] = "u"
    keymap[0][8] = "i"
    keymap[0][9] = "o"
    keymap[0][10] = "p"
    keymap[0][11] = "?"

    # row 2
    keymap[1][0] = "?"
    keymap[1][1] = "a"
    keymap[1][2] = "s"
    keymap[1][3] = "d"
    keymap[1][4] = "f"
    keymap[1][5] = "g"
    keymap[1][6] = "h"
    keymap[1][7] = "j"
    keymap[1][8] = "k"
    keymap[1][9] = "l"
    keymap[1][10] = ";"
    keymap[1][11] = "'"

    # row 3
    keymap[2][0] = "S"
    keymap[2][1] = "z"
    keymap[2][2] = "x"
    keymap[2][3] = "c"
    keymap[2][4] = "v"
    keymap[2][5] = "b"
    keymap[2][6] = "n"
    keymap[2][7] = "m"
    keymap[2][8] = ","
    keymap[2][9] = "."
    keymap[2][10] = "/"
    keymap[2][11] = "\n"

    # row 4
    keymap[3][0] = "F"
    keymap[3][1] = "C"
    keymap[3][2] = "U"
    keymap[3][3] = "A"
    keymap[3][4] = "L"
    keymap[3][5] = ""   # NC, space takes two columns
    keymap[3][6] = " "
    keymap[3][7] = "R"
    keymap[3][8] = "L"
    keymap[3][9] = "D"
    keymap[3][10] = "U"
    keymap[3][11] = "R"

    return keymap
