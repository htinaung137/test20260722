"""Programming Lab I - Maze (Week 1 starter)

Move the player (P) to the goal (G).
Use W/A/S/D to move, or Q to quit.
"""

WALL = "#"
PLAYER = "P"
GOAL = "G"

# "#" is a wall and " " is a path.
maze = [
    "###############",
    "#     #       #",
    "# ### # ##### #",
    "#   #   #   # #",
    "### ##### # # #",
    "#   #     #   #",
    "# ### ####### #",
    "#     #       #",
    "###############",
]

start_x = 1
start_y = 1

goal_x = 13
goal_y = 7

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, maze, command):
        self.x, self.y = move_player(
            maze, self.x, self.y, command
        )

def show_maze(maze, player_x, player_y, goal_x, goal_y):
    print()
    for y in range(len(maze)):
        line = ""
        for x in range(len(maze[y])):
            if x == player_x and y == player_y:
                line = line + PLAYER
            elif x == goal_x and y == goal_y:
                line = line + GOAL
            else:
                line = line + maze[y][x]
        print(line)
    print()


def can_move(maze, x, y):
    if y < 0 or y >= len(maze):
        return False
    if x < 0 or x >= len(maze[y]):
        return False
    return maze[y][x] != WALL


def get_next_position(x, y, command):
    if command == "W":
        y = y - 1
    elif command == "S":
        y = y + 1
    elif command == "A":
        x = x - 1
    elif command == "D":
        x = x + 1
    return x, y


def move_player(maze, player_x, player_y, command):
    next_x, next_y = get_next_position(player_x, player_y, command)
    if can_move(maze, next_x, next_y):
        return next_x, next_y
    print("You cannot move into a wall.")
    return player_x, player_y


def is_goal(player_x, player_y, goal_x, goal_y):
    return player_x == goal_x and player_y == goal_y


def read_command():
    command = input("Move (W/A/S/D, Q to quit): ")
    return command.strip().upper()


def main():
    player = Player(start_x, start_y)

    print("Welcome to the Maze!")
    print("Move the player (P) to the goal (G).")

    while True:
        show_maze(maze, player.x, player.y, goal_x, goal_y)

        command = read_command()

        if command == "Q":
            print("Bye!")
            break

        if command not in ["W", "A", "S", "D"]:
            print("Use W/A/S/D to move, or Q to quit.")
            continue

        player.move(maze, command)

        if is_goal(player.x, player.y, goal_x, goal_y):
            show_maze(maze, player.x, player.y, goal_x, goal_y)
            print("Goal reached!")
            break


if __name__ == "__main__":
    main()
