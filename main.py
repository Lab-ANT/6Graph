
from SpacePartition import *
from PatternMining import *


if __name__ == "__main__":

    data = np.load("./seeds.npy")
    patterns = []
    outliers = []
    results = DHC(data)

    for r in results:
        p, o = OutlierDetect(r)
        patterns += p
        outliers += o

    # your can seed the number of iter, usually < 5
    for _ in range(3):
        results = DHC(np.vstack(outliers))
        outliers = []
        for r in results:
            p, o = OutlierDetect(r)
            patterns += p
            outliers += o

    # display or directly use for yourself
    for index, p in zip(list(range(len(patterns))), patterns):
        Tarrs = p.T

        address_space = []

        for i in range(32):
            splits = np.bincount(Tarrs[i], minlength=16)
            if len(splits[splits > 0]) == 1:
                address_space.append(format(
                    np.argwhere(splits > 0)[0][0], "x"))
            else:
                address_space.append("*")
        print("No.", index, "address pattern")
        print("".join(address_space))
        print("-"*32)
        for iparr in p:
            print("".join([format(x, "x") for x in iparr]))
        print()
