class xo_algorithm:
    common_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    user_input = 2
    pc_input = 1

    def find_position(self):
        rc = [0, 0]
        row = 0
        column = 0
        value = int(input("Enter the position:"))

        if value == 1:
            row = 0
            column = 0

        elif value == 2:
            row = 0
            column = 1

        elif value == 3:
            row = 0
            column = 2

        elif value == 4:
            row = 1
            column = 0

        elif value == 5:
            row = 1
            column = 1

        elif value == 6:
            row = 1
            column = 2

        elif value == 7:
            row = 2
            column = 0

        elif value == 8:
            row = 2
            column = 1

        elif value == 9:
            row = 2
            column = 2

        else:
            print("Give number between 1 to 9")
            self.find_position()

        rc[0] = row
        rc[1] = column

        return rc

    def fill_for_user(self):

        x = self.find_position()

        if self.common_board[x[0]][x[1]] == 0:
            self.common_board[x[0]][x[1]] = self.user_input
        else:
            print("Position is already occupied")
            self.fill_for_user()

    def check_row(self):

        chrow = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        r1 = int(((self.common_board[0][0] == 2) and (self.common_board[0][1] == 2)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))
        r2 = int(((self.common_board[0][1] == 2) and (self.common_board[0][2] == 2)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))
        r3 = int(((self.common_board[0][0] == 2) and (self.common_board[0][2] == 2)) and (
                (self.common_board[0][1] != 1) and self.common_board[0][1] != 2))
        r4 = int(((self.common_board[1][0] == 2) and (self.common_board[1][1] == 2)) and (
                (self.common_board[1][2] != 1) and self.common_board[1][2] != 2))
        r5 = int(((self.common_board[1][1] == 2) and (self.common_board[1][2] == 2)) and (
                (self.common_board[1][0] != 1) and self.common_board[1][0] != 2))
        r6 = int(((self.common_board[1][0] == 2) and (self.common_board[1][2] == 2)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))
        r7 = int(((self.common_board[2][0] == 2) and (self.common_board[2][1] == 2)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))
        r8 = int(((self.common_board[2][1] == 2) and (self.common_board[2][2] == 2)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))
        r9 = int(((self.common_board[2][0] == 2) and (self.common_board[2][2] == 2)) and (
                (self.common_board[2][1] != 1) and self.common_board[2][1] != 2))

        chrow[0] = r1
        chrow[1] = r2
        chrow[2] = r3
        chrow[3] = r4
        chrow[4] = r5
        chrow[5] = r6
        chrow[6] = r7
        chrow[7] = r8
        chrow[8] = r9

        return chrow

    def check_column(self):

        chcol = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        c1 = int(((self.common_board[0][0] == 2) and (self.common_board[1][0] == 2)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))

        c2 = int(((self.common_board[1][2] == 2) and (self.common_board[2][0] == 2)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))

        c3 = int(((self.common_board[0][0] == 2) and (self.common_board[2][0] == 2)) and (
                (self.common_board[1][0] != 1) and self.common_board[1][0] != 2))

        c4 = int(((self.common_board[0][1] == 2) and (self.common_board[1][1] == 2)) and (
                (self.common_board[2][1] != 1) and self.common_board[2][1] != 2))

        c5 = int(((self.common_board[1][1] == 2) and (self.common_board[2][1] == 2)) and (
                (self.common_board[0][1] != 1) and self.common_board[0][1] != 2))

        c6 = int(((self.common_board[0][1] == 2) and (self.common_board[2][1] == 2)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        c7 = int(((self.common_board[0][2] == 2) and (self.common_board[1][2] == 2)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))

        c8 = int(((self.common_board[1][2] == 2) and (self.common_board[2][2] == 2)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))

        c9 = int(((self.common_board[0][2] == 2) and (self.common_board[2][2] == 2)) and (
                (self.common_board[1][2] != 1) and self.common_board[1][2] != 2))

        chcol[0] = c1
        chcol[1] = c2
        chcol[2] = c3
        chcol[3] = c4
        chcol[4] = c5
        chcol[5] = c6
        chcol[6] = c7
        chcol[7] = c8
        chcol[8] = c9

        return chcol

    def check_horizontal(self):

        chhor = [0, 0, 0, 0, 0, 0]

        h1 = int(((self.common_board[0][0] == 2) and (self.common_board[1][1] == 2)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))

        h2 = int(((self.common_board[2][2] == 2) and (self.common_board[1][1] == 2)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))

        h3 = int(((self.common_board[0][0] == 2) and (self.common_board[2][2] == 2)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        h4 = int(((self.common_board[0][2] == 2) and (self.common_board[1][1] == 2)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))

        h5 = int(((self.common_board[1][1] == 2) and (self.common_board[2][0] == 2)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))

        h6 = int(((self.common_board[0][2] == 2) and (self.common_board[2][0] == 2)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        chhor[0] = h1
        chhor[1] = h2
        chhor[2] = h3
        chhor[3] = h4
        chhor[4] = h5
        chhor[5] = h6

        return chhor

    def row_pc(self):

        pcrow = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        pr1 = int(((self.common_board[0][0] == 1) and (self.common_board[0][1] == 1)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))
        pr2 = int(((self.common_board[0][1] == 1) and (self.common_board[0][2] == 1)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))
        pr3 = int(((self.common_board[0][0] == 1) and (self.common_board[0][2] == 1)) and (
                (self.common_board[0][1] != 1) and self.common_board[0][1] != 2))
        pr4 = int(((self.common_board[1][0] == 1) and (self.common_board[1][1] == 1)) and (
                (self.common_board[1][2] != 1) and self.common_board[1][2] != 2))
        pr5 = int(((self.common_board[1][1] == 1) and (self.common_board[1][2] == 1)) and (
                (self.common_board[1][0] != 1) and self.common_board[1][0] != 2))
        pr6 = int(((self.common_board[1][0] == 1) and (self.common_board[1][2] == 1)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))
        pr7 = int(((self.common_board[2][0] == 1) and (self.common_board[2][1] == 1)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))
        pr8 = int(((self.common_board[2][1] == 1) and (self.common_board[2][2] == 1)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))
        pr9 = int(((self.common_board[2][0] == 1) and (self.common_board[2][2] == 1)) and (
                (self.common_board[2][1] != 1) and self.common_board[2][1] != 2))

        pcrow[0] = pr1
        pcrow[1] = pr2
        pcrow[2] = pr3
        pcrow[3] = pr4
        pcrow[4] = pr5
        pcrow[5] = pr6
        pcrow[6] = pr7
        pcrow[7] = pr8
        pcrow[8] = pr9

        return pcrow

    def pc_column(self):

        pccol = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        pc1 = int(((self.common_board[0][0] == 1) and (self.common_board[1][0] == 1)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))

        pc2 = int(((self.common_board[1][2] == 1) and (self.common_board[2][0] == 1)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))

        pc3 = int(((self.common_board[0][0] == 1) and (self.common_board[2][0] == 1)) and (
                (self.common_board[1][0] != 1) and self.common_board[1][0] != 2))

        pc4 = int(((self.common_board[0][1] == 1) and (self.common_board[1][1] == 1)) and (
                (self.common_board[2][1] != 1) and self.common_board[2][1] != 2))

        pc5 = int(((self.common_board[1][1] == 1) and (self.common_board[2][1] == 1)) and (
                (self.common_board[0][1] != 1) and self.common_board[0][1] != 2))

        pc6 = int(((self.common_board[0][1] == 1) and (self.common_board[2][1] == 1)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        pc7 = int(((self.common_board[0][2] == 1) and (self.common_board[1][2] == 1)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))

        pc8 = int(((self.common_board[1][2] == 1) and (self.common_board[2][2] == 1)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))

        pc9 = int(((self.common_board[0][2] == 1) and (self.common_board[2][2] == 1)) and (
                (self.common_board[1][2] != 1) and self.common_board[1][2] != 2))

        pccol[0] = pc1
        pccol[1] = pc2
        pccol[2] = pc3
        pccol[3] = pc4
        pccol[4] = pc5
        pccol[5] = pc6
        pccol[6] = pc7
        pccol[7] = pc8
        pccol[8] = pc9

        return pccol

    def pc_horizontal(self):

        pchor = [0, 0, 0, 0, 0, 0]

        ph1 = int(((self.common_board[0][0] == 1) and (self.common_board[1][1] == 1)) and (
                (self.common_board[2][2] != 1) and self.common_board[2][2] != 2))

        ph2 = int(((self.common_board[2][2] == 1) and (self.common_board[1][1] == 1)) and (
                (self.common_board[0][0] != 1) and self.common_board[0][0] != 2))

        ph3 = int(((self.common_board[0][0] == 1) and (self.common_board[2][2] == 1)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        ph4 = int(((self.common_board[0][2] == 1) and (self.common_board[1][1] == 1)) and (
                (self.common_board[2][0] != 1) and self.common_board[2][0] != 2))

        ph5 = int(((self.common_board[1][1] == 1) and (self.common_board[2][0] == 1)) and (
                (self.common_board[0][2] != 1) and self.common_board[0][2] != 2))

        ph6 = int(((self.common_board[0][2] == 1) and (self.common_board[2][0] == 1)) and (
                (self.common_board[1][1] != 1) and self.common_board[1][1] != 2))

        pchor[0] = ph1
        pchor[1] = ph2
        pchor[2] = ph3
        pchor[3] = ph4
        pchor[4] = ph5
        pchor[5] = ph6

        return pchor

    def move_pc(self):

        row = self.check_row()
        column = self.check_column()
        horizontal = self.check_horizontal()
        prow = self.row_pc()
        pcolumn = self.pc_column()
        phorizontal = self.pc_horizontal()

        q = 0
        w = 0
        e = 0

        q1 = 0
        w1 = 0
        e1 = 0

        qh = False
        wh = False
        eh = False

        qp = False
        wp = False
        ep = False

        for r in row:
            q = q + 1
            if r == 1:
                qh = True
                break

        for c in column:
            w = w + 1
            if c == 1:
                wh = True
                break

        for h in horizontal:
            e = e + 1
            if h == 1:
                eh = True
                break

        for rp in prow:
            q1 = q1 + 1
            if rp == 1:
                qp = True
                break

        for cp in pcolumn:
            w1 = w1 + 1
            if cp == 1:
                wp = True
                break

        for hp in phorizontal:
            e1 = e1 + 1
            if hp == 1:
                ep = True
                break

        if qp:

            if q1 == 1:
                self.common_board[0][2] = self.pc_input
            elif q1 == 2:
                self.common_board[0][0] = self.pc_input
            elif q1 == 3:
                self.common_board[0][1] = self.pc_input
            elif q1 == 4:
                self.common_board[1][2] = self.pc_input
            elif q1 == 5:
                self.common_board[1][0] = self.pc_input
            elif q1 == 6:
                self.common_board[1][1] = self.pc_input
            elif q1 == 7:
                self.common_board[2][2] = self.pc_input
            elif q1 == 8:
                self.common_board[2][0] = self.pc_input
            elif q1 == 9:
                self.common_board[2][1] = self.pc_input

        elif wp:

            if w1 == 1:
                self.common_board[2][0] = self.pc_input
            elif w1 == 2:
                self.common_board[0][0] = self.pc_input
            elif w1 == 3:
                self.common_board[1][0] = self.pc_input
            elif w1 == 4:
                self.common_board[2][1] = self.pc_input
            elif w1 == 5:
                self.common_board[0][1] = self.pc_input
            elif w1 == 6:
                self.common_board[1][1] = self.pc_input
            elif w1 == 7:
                self.common_board[2][2] = self.pc_input
            elif w1 == 8:
                self.common_board[0][2] = self.pc_input
            elif w1 == 9:
                self.common_board[1][2] = self.pc_input

        elif ep:

            if e1 == 1:
                self.common_board[2][2] = self.pc_input
            elif e1 == 2:
                self.common_board[0][0] = self.pc_input
            elif e1 == 3:
                self.common_board[1][1] = self.pc_input
            elif e1 == 4:
                self.common_board[2][0] = self.pc_input
            elif e1 == 5:
                self.common_board[0][2] = self.pc_input
            elif e1 == 6:
                self.common_board[1][1] = self.pc_input

        elif qh:

            if q == 1:
                self.common_board[0][2] = self.pc_input
            elif q == 2:
                self.common_board[0][0] = self.pc_input
            elif q == 3:
                self.common_board[0][1] = self.pc_input
            elif q == 4:
                self.common_board[1][2] = self.pc_input
            elif q == 5:
                self.common_board[1][0] = self.pc_input
            elif q == 6:
                self.common_board[1][1] = self.pc_input
            elif q == 7:
                self.common_board[2][2] = self.pc_input
            elif q == 8:
                self.common_board[2][0] = self.pc_input
            elif q == 9:
                self.common_board[2][1] = self.pc_input

        elif wh:

            if w == 1:
                self.common_board[2][0] = self.pc_input
            elif w == 2:
                self.common_board[0][0] = self.pc_input
            elif w == 3:
                self.common_board[1][0] = self.pc_input
            elif w == 4:
                self.common_board[2][1] = self.pc_input
            elif w == 5:
                self.common_board[0][1] = self.pc_input
            elif w == 6:
                self.common_board[1][1] = self.pc_input
            elif w == 7:
                self.common_board[2][2] = self.pc_input
            elif w == 8:
                self.common_board[0][2] = self.pc_input
            elif w == 9:
                self.common_board[1][2] = self.pc_input

        elif eh:

            if e == 1:
                self.common_board[2][2] = self.pc_input
            elif e == 2:
                self.common_board[0][0] = self.pc_input
            elif e == 3:
                self.common_board[1][1] = self.pc_input
            elif e == 4:
                self.common_board[2][0] = self.pc_input
            elif e == 5:
                self.common_board[0][2] = self.pc_input
            elif e == 6:
                self.common_board[1][1] = self.pc_input

        else:
            z = 0
            for i in range(3):
                for j in range(3):
                    if self.common_board[i][j] == 0:
                        self.common_board[i][j] = self.pc_input
                        z = z+1
                    break
                if z == 1:
                    break


    def show(self):
        string_board = [["", "", ""], ["", "", ""], ["", "", ""]]

        for i in range(3):
            for j in range(3):
                if self.common_board[i][j] == 0:
                    string_board[i][j] = " "
                elif self.common_board[i][j] == 1:
                    string_board[i][j] = "O"
                elif self.common_board[i][j] == 2:
                    string_board[i][j] = "X"

        e1 = string_board[0][0]
        e2 = string_board[0][1]
        e3 = string_board[0][2]
        e4 = string_board[1][0]
        e5 = string_board[1][1]
        e6 = string_board[1][2]
        e7 = string_board[2][0]
        e8 = string_board[2][1]
        e9 = string_board[2][2]

        zero = f"""
            {e1}|{e2}|{e3}
            _____
            {e4}|{e5}|{e6}
            _____
            {e7}|{e8}|{e9}
            """
        print(zero)

    def checking(self):

        k = 0
        for i in range(3):
            for j in range(3):
                if self.common_board[i][j] != 0:
                    k = k + 1

        if k == 9:
            self.show()
            print("Draw")
            return False

        elif (((self.common_board[0][0] == self.common_board[0][1]) and (
                self.common_board[0][1] == self.common_board[0][2]) and
                self.common_board[0][2] != 0) or ((self.common_board[1][0] == self.common_board[1][1]) and (
                self.common_board[1][1] == self.common_board[1][2]) and self.common_board[1][2] != 0) or (
                (self.common_board[2][0] == self.common_board[2][1]) and (
                self.common_board[2][1] == self.common_board[2][2])) and
                self.common_board[2][2] != 0):

            self.show()
            print("Game over")
            return False

        elif (((self.common_board[0][0] == self.common_board[1][0]) and (
                self.common_board[1][0] == self.common_board[2][0]) and
                self.common_board[2][0] != 0) or ((self.common_board[0][1] == self.common_board[1][1]) and (
                self.common_board[1][1] == self.common_board[2][1]) and self.common_board[2][1] != 0) or (
                (self.common_board[0][2] == self.common_board[1][2]) and (self.common_board[1][2] == self.common_board[2][2])) and
                self.common_board[2][2] != 0):

            self.show()
            print("Game over")
            return False


        elif (((self.common_board[0][0] == self.common_board[1][1]) and (self.common_board[1][1] == self.common_board[2][2]) and self.common_board[2][2] != 0) or (
                (self.common_board[0][2] == self.common_board[1][1]) and (self.common_board[1][1] == self.common_board[2][0]) and self.common_board[2][0] != 0)):

            self.show()
            print("Game over")
            return False

        else:
            return True
