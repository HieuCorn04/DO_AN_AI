import streamlit as st
import random
import turtle

class EightQueens:
    def __init__(self):
        self.board_size = 8
        self.queens = []

    def reset_board(self):
        self.queens = []

    def check_solution(self):
        return self.is_valid_solution()

    def is_valid_solution(self):
        for queen in self.queens:
            row, col = queen
            for other_queen in self.queens:
                other_row, other_col = other_queen
                if queen != other_queen and (row == other_row or col == other_col or abs(row - other_row) == abs(col - other_col)):
                    return False
        return True

    def solve_problem(self):
        self.reset_board()
        solution = self.hill_climbing()
        self.queens = solution

    def hill_climbing(self):
        queens = [(i, random.randint(0, self.board_size - 1)) for i in range(self.board_size)]
        steps = 1000
        for _ in range(steps):
            attacked_queens = self.attacked_queens(queens)
            if not attacked_queens:
                return queens
            queen_to_move = random.choice(attacked_queens)
            new_col = random.randint(0, self.board_size - 1)
            queens[queen_to_move] = (queens[queen_to_move][0], new_col)
        return queens

    def attacked_queens(self, queens):
        attacked = set()
        for i, (r, c) in enumerate(queens):
            for j, (r2, c2) in enumerate(queens):
                if i != j and (r == r2 or c == c2 or abs(r - r2) == abs(c - c2)):
                    attacked.add(i)
                    attacked.add(j)
        return list(attacked)

def main():
    st.title("8 Queens Problem")

    eight_queens = EightQueens()

    if st.button("Reset"):
        eight_queens.reset_board()

    if st.button("Check"):
        if eight_queens.check_solution():
            st.success("Valid Solution")
        else:
            st.error("Invalid Solution")

    if st.button("Solve"):
        eight_queens.solve_problem()
        if eight_queens.is_valid_solution():
            st.success("Solution found!")
        else:
            st.error("No solution found.")

    # Draw the chessboard
    

    def draw_square(color):
        turtle.begin_fill()
        turtle.fillcolor(color)
        for _ in range(4):
            turtle.forward(50)
            turtle.right(90)
        turtle.end_fill()
        turtle.forward(50)

    def draw_chessboard():
        colors = ["white", "black"]
        for _ in range(8):
            for color in colors:
                draw_square(color)
            turtle.backward(400)
            turtle.right(90)
            turtle.forward(50)
            turtle.left(90)

        turtle.hideturtle()

if __name__ == "__main__":
    main()
