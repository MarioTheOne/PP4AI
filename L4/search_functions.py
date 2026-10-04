def get_open_requests(requests):
    # Return the IDs for requests whose status is open.
    open_ids = []
    for request in requests:
        if request["status"] == "open":
            open_ids.append(request["id"])
    return open_ids


def breadth_first_search(tree, start):
    # Treat the list as a queue: remove the earliest pending node first.
    pending = [start]
    order = []
    while pending:
        node = pending.pop(0)
        order.append(node)
        for child in tree[node]:
            pending.append(child)
    return order


def depth_first_search(tree, start):
    # Treat the list as a stack: remove the most recently added node first.
    pending = [start]
    order = []
    while pending:
        node = pending.pop()
        order.append(node)
        # Reverse the children so the leftmost child is visited first.
        for child in reversed(tree[node]):
            pending.append(child)
    return order