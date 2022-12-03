import numpy as np
import random as rd


def ald(grid: np.ndarray, size: int) -> np.ndarray:
    output_grid = np.empty([size * 3, size * 3], dtype=str)
    output_grid[:] = '0'
    c = size * size  # number of cells to be visited
    i = rd.randrange(size)
    j = rd.randrange(size)
    while np.count_nonzero(grid) < c:

        # visit this cell
        grid[i, j] = 1

        w = i * 3 + 1
        k = j * 3 + 1
        output_grid[w, k] = '1'

        can_go = [1, 1, 1, 1]

        if i == 0:
            can_go[0] = 0
        if i == size - 1:
            can_go[2] = 0
        if j == 0:
            can_go[3] = 0
        if j == size - 1:
            can_go[1] = 0

        # it makes sense to choose neighbour among available directions
        neighbour_idx = np.random.choice(np.nonzero(can_go)[0])  # n,e,s,w

        if neighbour_idx == 0:
            # has been visited?
            if grid[i - 1, j] == 0:
                # goto n
                output_grid[w - 1, k] = '3'
                output_grid[w - 2, k] = '1'
            i -= 1

        if neighbour_idx == 1:
            if grid[i, j + 1] == 0:
                # goto e
                output_grid[w, k + 1] = '1'
                output_grid[w, k + 2] = '1'
            j += 1

        if neighbour_idx == 2:
            if grid[i + 1, j] == 0:
                # goto s
                output_grid[w + 1, k] = '1'
                output_grid[w + 2, k] = '1'
            i += 1

        if neighbour_idx == 3:
            # goto w
            if grid[i, j - 1] == 0:
                output_grid[w, k - 1] = '1'
                output_grid[w, k - 2] = '1'
            j -= 1

    return output_grid


def main():
    size = 5

    # np.random.seed(42)
    grid = np.zeros(shape=(size, size))

    console_grid = ald(grid, size)

    console_grid[13][0] = '2'
    console_grid[13][14] = '4'

    f = open('map_gen.txt', 'w')
    f.write('15 15' + '\n')
    for elm in console_grid:
        f.write(' '.join(elm) + '\n')

    f.close()


if __name__ == '__main__':
    main()