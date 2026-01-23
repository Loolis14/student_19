#!/usr/bin/env python3
# File: parser_maze.py
# Author: ebabun <ebabun@student.42belgium.be>
# Author: mmeurer <mmeurer@student.42belgium.be>
# Created: 2026/01/23 16:09:10
# Updated: 2026/01/23 16:09:10

from maze_generator import MazeGenerator


class MazeParser:
    def __init__(self, filename, maze_size):
        self.name = filename
        self.maze_size = maze_size
        self.maze: list = []
        self.entry: tuple = ()
        self.exit: tuple = ()
        self.path = ""

    def open_file(self):
        try:
            with open(self.name, "r") as f:
                lines = [line.rstrip("\n") for line in f.readlines()]
                return lines
        except FileNotFoundError:
            print(f"Erreur: le fichier {self.name} est introuvable")
            return

    def parse_lines(self):
        lines = self.open_file()
        self.maze = lines[:self.maze_size]
        self.entry = (int(lines[self.maze_size + 1][0]),
                      int(lines[self.maze_size + 1][2]))
        self.exit = (int(lines[self.maze_size + 2][0]),
                     int(lines[self.maze_size + 2][2]))
        self.path = lines[self.maze_size + 3]

    def display_maze_without_path(self):
        line_border = "+" + "---+" * len(self.maze[0])
        acc_line = 0

        print(line_border)
        for line in self.maze:
            line_walls = "|"
            line_bottom = "+"
            acc_hexa = 0
            for hexa in line:
                if (acc_hexa, acc_line) == self.entry:
                    cell_content = "\033[32m■\033[0m"
                elif (acc_hexa, acc_line) == self.exit:
                    cell_content = "\033[31m■\033[0m"
                elif hexa == "F":
                    cell_content = "■"
                else:
                    cell_content = " "

                if hexa == "F":
                    line_walls += f" {cell_content} |"
                    line_bottom += "---+"
                else:
                    if hexa in "2367ABE":
                        line_walls += f" {cell_content} |"
                    else:
                        line_walls += f" {cell_content}  "
                    if hexa in "4567CDE":
                        line_bottom += "---+"
                    else:
                        line_bottom += "   +"
                acc_hexa += 1
            print(line_walls)
            print(line_bottom)
            acc_line += 1

    def coordinates_path(self):
        path = []
        cx, cy = self.entry
        for direction in self.path:
            x, y = MazeGenerator.offset[direction]
            cx += x
            cy += y
            path.append((cx, cy))
        return path

    def display_maze_with_path(self):
        line_border = "+" + "---+" * len(self.maze[0])
        coor_path = self.coordinates_path()
        acc_line = 0

        print(line_border)
        for line in self.maze:
            line_walls = "|"
            line_bottom = "+"
            acc_hexa = 0
            for hexa in line:
                if (acc_hexa, acc_line) == self.entry:
                    cell_content = "\033[32m■\033[0m"
                elif (acc_hexa, acc_line) == self.exit:
                    cell_content = "\033[31m■\033[0m"
                elif (acc_hexa, acc_line) in coor_path:
                    cell_content = "\033[35m■\033[0m"
                elif hexa == "F":
                    cell_content = "■"
                else:
                    cell_content = " "

                if hexa == "F":
                    line_walls += f" {cell_content} |"
                    line_bottom += "---+"
                else:
                    if hexa in "2367ABE":
                        line_walls += f" {cell_content} |"
                    else:
                        line_walls += f" {cell_content}  "
                    if hexa in "4567CDE":
                        line_bottom += "---+"
                    else:
                        line_bottom += "   +"
                acc_hexa += 1
            print(line_walls)
            print(line_bottom)
            acc_line += 1

    @staticmethod
    def show_menu():
        print("\n=== A-Maze-ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path from entry to exit")
        print("3. Rotate maze colors")
        print("4. Quit")

    @staticmethod
    def get_choice():
        while True:
            choice = input("Choice? (1-4): ")
            if choice in {'1', '2', '3', '4'}:
                return choice
            print("Invalid choice, please enter a number from 1 to 4.")

    def display_ascii(self):
        self.parse_lines()
        show_path = False
        while True:
            if show_path:
                self.display_maze_with_path()
            else:
                self.display_maze_without_path()

            self.show_menu()
            choice = self.get_choice()

            if choice == '1':
                # regenerate maze
                print(1)
            elif choice == '2':
                show_path = not show_path
            elif choice == '3':
                print(3)
                # rotate_colors()
            elif choice == '4':
                print("Bye!")
                break
