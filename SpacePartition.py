import numpy as np
import queue


def DHC(arrs):
    q = queue.Queue()
    q.put(arrs)
    regions_arrs = []
    while not q.empty():
        arrs = q.get()
        if len(arrs) <= 16:
            regions_arrs.append(arrs)
            continue
        # len(arrs)<=16: not isolated seed's arrs
        splits = leftmost(arrs)

        for s in splits:
            q.put(arrs[s])
    return regions_arrs


def leftmost(arrs):
    Tarrs = arrs.T
    for i in range(32):
        splits = np.bincount(Tarrs[i], minlength=16)

        if len(splits[splits > 0]) > 1:
            split_index = i
            split_nibbles = np.where(splits != 0)[0]
            break

    return [
        np.where(Tarrs[split_index] == nibble)[0] for nibble in split_nibbles
    ]


# show the regions for test 

def show_regions(arrs):
    address_space = []
    Tarrs = arrs.T
    for i in range(32):
        splits = np.bincount(Tarrs[i], minlength=16)
        # print(i, splits, np.argwhere(splits > 0)[0][0])
        if len(splits[splits > 0]) == 1:

            address_space.append(format(np.argwhere(splits > 0)[0][0], "x"))
        else:
            address_space.append("*")

    print("********address region**********")
    print("".join(address_space))
    for i in range(len(arrs)):
        print("".join([format(x, "x") for x in arrs[i]]), " ", i)
    print()
