from collections import deque

from search_functions import breadth_first_search, depth_first_search, get_open_requests


def main():
    # Example check for filtering open requests.
    requests = [
        {"id": "R1", "status": "open"},
        {"id": "R2", "status": "closed"},
        {"id": "R3", "status": "open"},
    ]
    requests.append({"id": "R4", "status": "open"})
    print("Open requests:", get_open_requests(requests))

    # A stack removes the most recently added action first (LIFO).
    history = ["Write the title", "Add a paragraph", "Insert an image"]
    print("Undo history:")
    while history:
        print("Undo:", history.pop())

    # A deque removes the earliest request first (FIFO).
    pending_requests = deque(["R1", "R2", "R3"])
    print("Requests in arrival order:")
    while pending_requests:
        print("Process:", pending_requests.popleft())

    # Each key maps to its children; an empty list marks a leaf node.
    tree = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [],
        "E": [],
        "F": [],
        "G": [],
    }
    print("BFS from A:", breadth_first_search(tree, "A"))
    print("DFS from A:", depth_first_search(tree, "A"))

    # Starting at B only visits B and its descendants.
    print("BFS from B:", breadth_first_search(tree, "B"))
    print("DFS from B:", depth_first_search(tree, "B"))

    # H and I extend the branch below D for the deeper-tree exercise.
    tree_with_extra_level = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": [],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
    }
    print("BFS with extra level:", breadth_first_search(tree_with_extra_level, "A"))
    print("DFS with extra level:", depth_first_search(tree_with_extra_level, "A"))


if __name__ == "__main__":
    main()