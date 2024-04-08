import tkinter as tk
import random

class EightQueensGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("8 Queens Problem")
        self.board_size = 8
        self.queens = []
        self.canvas = tk.Canvas(master, width=400, height=400, bg='white')
        self.canvas.pack()
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_board)
        self.reset_button.pack(side=tk.LEFT)
        self.check_button = tk.Button(master, text="Check", command=self.check_solution)
        self.check_button.pack(side=tk.LEFT)
        self.solve_button = tk.Button(master, text="Solve", command=self.solve_problem)
        self.solve_button.pack(side=tk.LEFT)
        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        square_size = 400 // self.board_size
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(col * square_size, row * square_size,
                                             (col + 1) * square_size, (row + 1) * square_size,
                                             fill=color)
        for queen in self.queens:
            self.place_queen(queen[0], queen[1])

    def color_queens(self, color):
        for queen in self.queens:
            row, col = queen
            self.place_queen(row, col, color)

    def place_queen(self, row, col, color="blue"):
        square_size = 400 // self.board_size
        self.canvas.create_oval(col * square_size + square_size // 4, row * square_size + square_size // 4,
                                (col + 1) * square_size - square_size // 4, (row + 1) * square_size - square_size // 4,
                                fill=color)

    def reset_board(self):
        self.queens = []
        self.draw_board()

    def check_solution(self):
        if self.is_valid_solution():
            self.color_queens("green")
        else:
            self.color_queens("red")

    def is_valid_solution(self):
        for queen in self.queens:
            row, col = queen
            for other_queen in self.queens:
                other_row, other_col = other_queen
                if queen != other_queen and (row == other_row or col == other_col or abs(row - other_row) == abs(col - other_col)):
                    return False
        return True

    def on_click(self, event):
        col = event.x // (400 // self.board_size)
        row = event.y // (400 // self.board_size)
        if (row, col) not in self.queens:
            self.queens.append((row, col))
            self.draw_board()

    def solve_problem(self):
        self.reset_board()
        solution = self.hill_climbing()
        self.queens = solution
        self.color_queens("green" if self.is_valid_solution() else "red")

    def hill_climbing(self):
        queens = [(i, random.randint(0, self.board_size - 1)) for i in range(self.board_size)]
        steps = 1000  # Số bước tối đa để tìm giải pháp
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

root = tk.Tk()
app = EightQueensGUI(root)
app.canvas.bind("<Button-1>", app.on_click)
root.mainloop()
