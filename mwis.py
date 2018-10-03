def read_from_file_into_list(file_path="mwis.txt"):
    weights_of_vertices = []
    size = None
    with open(file_path) as f:
        for i, w in enumerate(f):
            if i == 0:
                size = int(w)
                continue
            weights_of_vertices.append(int(w))
    return weights_of_vertices, size


def to_keep_or_not(keeper, current_weight):
    if keeper[-1] > keeper[-2] + current_weight:
        keeper.append(keeper[-1])
    elif keeper[-1] < keeper[-2] + current_weight:
        keeper.append(keeper[-2] + current_weight)
    elif keeper[-1] == keeper[-2] + current_weight:
        keeper.append(keeper[-2] + current_weight)


def solve():
    keeper = [0, 4962786]
    in_or_not = []
    weights_of_vertices, size = read_from_file_into_list()
    for i, w in enumerate(weights_of_vertices):
        if i == 0:
            continue
        to_keep_or_not(keeper, w)

    i = size
    while i >= 1:
        if keeper[i-1] >= keeper[i-2] + weights_of_vertices[i-1]:
            i -= 1
        else:
            in_or_not.append(i)
            i -= 2
    return in_or_not


in_or_not = solve()

print 1 in in_or_not, 2 in in_or_not, 3 in in_or_not, 4 in in_or_not, 17 in in_or_not, 117 in in_or_not, 517 in in_or_not, 997 in in_or_not
