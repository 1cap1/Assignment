
#water jug

from heapq import heappush, heappop
from collections import deque

def pour(state, jug1, jug2):
    """Simulate pouring water from one jug to another."""
    amt = min(state[jug1], jug_caps[jug2] - state[jug2])
    new_state = list(state)
    new_state[jug1] -= amt
    new_state[jug2] += amt
    return tuple(new_state)

def get_successors(state):
    """Generate all possible successor states from the current state."""
    successors = []

    # Pour water between jugs
    for jug1, jug2 in [(0, 1), (1, 0)]:
        new_state = pour(state, jug1, jug2)
        if new_state != state:
            successors.append(new_state)

    # Fill each jug to its capacity
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = jug_caps[jug]
        successors.append(tuple(new_state))

    # Empty each jug
    for jug in [0, 1]:
        new_state = list(state)
        new_state[jug] = 0
        successors.append(tuple(new_state))

    return successors

def heuristic(state, goal):
    """Heuristic function: Manhattan distance between current and goal states."""
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))

def a_star(start, goal):
    """A* algorithm to find the shortest path to the goal state."""
    open_list = []  # Priority queue (min-heap)
    heappush(open_list, (0 + heuristic(start, goal), 0, start))  # (f, g, state)

    closed_list = set()  # Set of visited states
    parent = {start: None}  # To reconstruct the path

    while open_list:
        _, g, curr_state = heappop(open_list)  # Get state with lowest f

        if curr_state == goal:
            # Reconstruct the path
            path = deque()
            while curr_state is not None:
                path.appendleft(curr_state)
                curr_state = parent[curr_state]
            return list(path)

        closed_list.add(curr_state)

        for succ_state in get_successors(curr_state):
            if succ_state not in closed_list:
                new_g = g + 1  # Increment path cost
                f = new_g + heuristic(succ_state, goal)
                heappush(open_list, (f, new_g, succ_state))
                parent[succ_state] = curr_state

    return None  # No solution found

# Problem definition
jug_caps = (4, 3)  # Capacities of the jugs
start_state = (0, 0)  # Starting state (both jugs empty)
goal_state = (2, 0)  # Goal state

# Solve the problem
solution = a_star(start_state, goal_state)
if solution:
    print("Solution:")
    for state in solution:
        print(state)
else:
    print("No solution exists.")

# 8-puzzle

import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        idx_s = state.index(i)
        idx_g = goal.index(i)
        distance += abs(idx_s // 3 - idx_g // 3) + abs(idx_s % 3 - idx_g % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[blank_index]
            neighbors.append(tuple(new_state))
    return neighbors

def a_star_search(start, goal):
    frontier = []
    heapq.heappush(frontier, (0 + manhattan_distance(start, goal), 0, start, []))
    explored = set()
    while frontier:
        f, g, current_state, path = heapq.heappop(frontier)
        if current_state == goal:
            return path + [current_state]
        explored.add(current_state)
        for neighbor in get_neighbors(current_state):
            if neighbor not in explored:
                new_g = g + 1
                new_f = new_g + manhattan_distance(neighbor, goal)
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [current_state]))
    return None

start_state = (1, 2, 3, 4, 0, 5, 6, 7, 8)
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = a_star_search(start_state, goal_state)

if solution:
    print("Solution found in {} steps!".format(len(solution) - 1))
    for step in solution:
        print(step)
else:
    print("No solution found.")

# map-coloring

def is_valid(map, region, color, color_assignment):
    for neighbor in map[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True


def solve_map_coloring(map, regions, colors, color_assignment={}):
    if len(color_assignment) == len(regions):
        return color_assignment

    current_region = [r for r in regions if r not in color_assignment][0]

    for color in colors:
        if is_valid(map, current_region, color, color_assignment):
            color_assignment[current_region] = color
            result = solve_map_coloring(map, regions, colors, color_assignment)
            if result is not None:
                return result
            del color_assignment[current_region]

    return None


if __name__ == "__main__":
    map = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q", "NSW", "V"],
        "Q": ["NT", "SA", "NSW"],
        "NSW": ["Q", "SA", "V"],
        "V": ["SA", "NSW"],
    }
    regions = list(map.keys())
    colors = ["Red", "Green", "Blue"]

    coloring = solve_map_coloring(map, regions, colors)

    if coloring:
        print("Valid coloring:")
        for region, color in coloring.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.")

def is_valid_coloring(map,color,colorassignment,region):
  for i in map[region]:
    if i in colorassignment and colorassignment[i]==color:
      return False
  return True

