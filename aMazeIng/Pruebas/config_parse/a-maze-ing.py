#!/usr/bin/env python3
import sys
from parse_script import parse_config, MazeConfigError
from mazegen.generate_maze import Maze

def a_maze_ing() -> None:
    """
    
    """
    if len(sys.argv) == 2:
        try:
            file = sys.argv[1]
            a_maze_ing = Maze(parse_config(file))
            a_maze_ing.print_maze()
            a_maze_ing.save_to_file()
        except MazeConfigError as e:
            print(f"Caught an error: {e}")
    else:
        print("No arguments recieved")

a_maze_ing()
